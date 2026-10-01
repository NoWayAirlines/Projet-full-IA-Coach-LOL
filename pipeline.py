"""
pipeline.py — Pipeline du chatbot LoL coach.

  1. SCRAPE : récupère les stats réelles op.gg (Emerald+, tous les champions, tous les rôles,
              matchups) et génère contexte_opgg.json — l'UNIQUE fichier de données du projet
              (builds, runes, counters, synergies, matchups, tier lists, guides, noms des champions).
  2. INDEX  : indexe ChromaDB (contexte_opgg.json + sorts Data Dragon + patch notes).

Usage :
    python pipeline.py           # etape 1 + etape 2
    python pipeline.py --scrape  # etape 1 seulement (nouveau patch)
    python pipeline.py --index   # etape 2 seulement

Prerequis :
    pip install httpx requests ollama chromadb streamlit
    ollama pull nomic-embed-text
"""

import sys
import os
import re
import json
import time
import requests
import httpx
from concurrent.futures import ThreadPoolExecutor, as_completed

# ══════════════════════════════════════════════════════════════════════════════
# CONFIG
# ══════════════════════════════════════════════════════════════════════════════

CONTEXTE_FILE = "contexte_opgg.json"
CACHE_DIR     = "opgg_cache"      # réponses brutes op.gg, par patch (permet la reprise)
DB_PATH       = "./lol_db"
EMBED_MODEL   = "nomic-embed-text"
TIER          = "emerald_plus"    # rang des games analysées
N_MATCHUPS    = 10                # adversaires les plus fréquents détaillés par champion/rôle
WORKERS       = 5                 # requêtes op.gg en parallèle (rester raisonnable)

OPGG_API = "https://lol-api-champion.op.gg/api/global/champions/ranked"  # stats JSON
OPGG_MCP = "https://mcp-api.op.gg/mcp"                                   # guides de matchup

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

POSITIONS = {"TOP": "Top", "JUNGLE": "Jungle", "MID": "Mid", "ADC": "ADC (Bot)", "SUPPORT": "Support"}
POS_MCP   = {"TOP": "top", "JUNGLE": "jungle", "MID": "mid", "ADC": "adc", "SUPPORT": "support"}
TIERS     = {1: "S (OP)", 2: "A", 3: "B", 4: "C", 5: "D"}
SHARDS    = {5008: "Adaptive Force", 5005: "Attack Speed", 5007: "Ability Haste", 5001: "Health Scaling",
             5011: "Health", 5013: "Tenacity/Slow Resist", 5010: "Move Speed", 5002: "Armor", 5003: "Magic Resist"}

# ══════════════════════════════════════════════════════════════════════════════
# CONNAISSANCES ÉCRITES À LA MAIN (ajoutées telles quelles au contexte)
# Rédigées au patch 16.19 : n'y citer que des items/runes qui existent encore.
# ══════════════════════════════════════════════════════════════════════════════

GUIDES = [
    ("guide_items_antiheal",
     "ITEMS COUNTER — ANTI-HEAL (Grievous Wounds / Wounds)\n"
     "Quand l'ennemi a du sustain (Soraka, Yuumi, Aatrox, Vladimir, Dr. Mundo, Warwick, Sylas, Swain, Fiddlesticks, Briar, "
     "Olaf, Illaoi, Nami, Sona, Seraphine, Milio, Renata Glasc, Kayn rouge, lifesteal ADC) → acheter l'anti-heal TÔT "
     "(composant dès le 1er/2e back).\n"
     "- ADC / AD crit : Executioner's Calling → Mortal Reminder (Armor Pen + 40% Wounds).\n"
     "- Fighter / bruiser AD : Executioner's Calling → Chempunk Chainsword (HP + 40% Wounds).\n"
     "- Mage / AP : Oblivion Orb → Morellonomicon (HP + 40% Wounds sur magic damage).\n"
     "- Tank / support : Bramble Vest → Thornmail (armure + Wounds quand on te frappe, idéal vs auto-attackers qui "
     "lifesteal : Master Yi, Tryndamere, Vayne, Kog'Maw, Bel'Veth).\n"
     "- Ignite applique aussi Grievous Wounds : bon spell en lane vs champion à heal.\n"
     "Règle : 1 anti-heal par joueur de dégâts suffit souvent. Le composant seul est déjà efficace en early."),

    ("guide_items_antishield",
     "ITEMS COUNTER — ANTI-SHIELD\n"
     "Vs boucliers massifs (Lulu, Janna, Karma, Seraphine, Milio, Renata Glasc, Sett W, Yasuo/Yone passif, Rell, Ivern, "
     "Locket of the Iron Solari, Sterak's Gage, Immortal Shieldbow, Eclipse) :\n"
     "- Serpent's Fang (AD lethality) : réduit les shields sur la cible touchée. Achat standard pour assassins AD / "
     "supports AD (Pyke) vs enchanteuses.\n"
     "- Pas d'équivalent AP : les mages jouent plutôt burst + Void Staff / Cryptbloom pour percer."),

    ("guide_items_vs_tanks",
     "ITEMS COUNTER — VS TANKS (Malphite, Ornn, Sion, Cho'Gath, Zac, Rammus, Sejuani, K'Sante, Dr. Mundo, Poppy, Maokai...)\n"
     "AD crit (ADC) : Lord Dominik's Regards (35% Armor Pen + bonus dégâts vs bonus HP), Kraken Slayer (dégâts selon HP "
     "manquants), Blade of The Ruined King (% HP actuels, top vs HP stack), Terminus.\n"
     "AD fighter : Black Cleaver (-armure empilable, aide toute l'équipe AD), Serylda's Grudge (Armor Pen), "
     "Blade of The Ruined King, Titanic Hydra / Overlord's Bloodmail pour les bruisers HP.\n"
     "AP : Void Staff (40% Magic Pen), Liandry's Torment (brûlure %HP max), Cryptbloom (30% Magic Pen), "
     "Bloodletter's Curse (réduit la MR de l'ennemi).\n"
     "Runes : Cut Down (dégâts bonus vs cibles à plus de HP max), Conqueror pour combats longs.\n"
     "Évite la lethality (Youmuu's Ghostblade, Hubris, Profane Hydra) vs 3+ tanks : pénétration plate, faible vs grosse armure."),

    ("guide_items_vs_assassins_burst",
     "ITEMS COUNTER — VS ASSASSINS / BURST (Zed, Talon, Qiyana, Kha'Zix, Rengar, Naafiri, Katarina, Akali, Fizz, LeBlanc, "
     "Evelynn, Kayn bleu, Syndra, Veigar...)\n"
     "- Vs burst AD : Zhonya's Hourglass (mage : stasis 2.5s, annule Zed R / Talon all-in), Guardian Angel (ADC/fighter AD), "
     "Death's Dance (fighter AD : étale les dégâts), Plated Steelcaps, Seeker's Armguard (composant armure AP).\n"
     "- Vs burst AP : Banshee's Veil (mage : spell shield), Edge of Night (AD : spell shield), Maw of Malmortius "
     "(AD : shield magique), Mercury's Treads, Negatron Cloak / Spectre's Cowl en early.\n"
     "- ADC : Immortal Shieldbow (shield sous 30% HP), Guardian Angel, Phantom Dancer (Ghosted, meilleur kite).\n"
     "- Vision : Control Ward + Oracle Lens contre Evelynn, Kha'Zix, Rengar, Talon, Twitch, Shaco.\n"
     "Runes défensives : Bone Plating (réduit les 3 prochaines instances de dégâts), Second Wind (vs poke), Nimbus Cloak / Celerity.\n"
     "Spells : Barrier (mid vs burst), Cleanse (ADC vs CC lourd), Exhaust (vs assassin qui dive : Zed, Katarina, Master Yi, "
     "Kha'Zix, Rengar)."),

    ("guide_items_vs_cc",
     "ITEMS COUNTER — VS CROWD CONTROL LOURD (Leona, Nautilus, Morgana, Lissandra, Sejuani, Amumu, Malzahar suppression, "
     "Skarner suppression, Warwick R, Twisted Fate...)\n"
     "- Mercury's Treads : tenacity + MR, bottes standard vs équipe à gros CC.\n"
     "- Quicksilver Sash → Mercurial Scimitar (ADC/AD : active qui retire tout CC sauf airborne, purge la suppression).\n"
     "- Sterak's Gage (fighter : 20% tenacity), Wit's End (attack speed : tenacity + MR), Endless Hunger (20% tenacity).\n"
     "- Support : Mikael's Blessing pour cleanse un allié (ne retire ni airborne ni suppression).\n"
     "- Rune Unflinching (tenacity + slow resist), shard Tenacity/Slow Resist. Spell Cleanse (ADC vs Leona/Nautilus/Morgana/Lux/Ashe)."),

    ("guide_items_vs_ad_ap",
     "ITEMS COUNTER — ÉQUIPE FULL AD ou FULL AP\n"
     "Ennemis majoritairement AD : Plated Steelcaps, Randuin's Omen (-30% dégâts crit), Frozen Heart (-20% attack speed ennemi), "
     "Thornmail, Dead Man's Plate, Iceborn Gauntlet, Sunfire Aegis, Death's Dance (fighter), Zhonya's Hourglass (mage). "
     "Vs crit hypercarry (Yasuo, Yone, Tryndamere, Jinx, Kai'Sa, Yunara) : Randuin's Omen obligatoire pour les tanks.\n"
     "Ennemis majoritairement AP : Mercury's Treads, Force of Nature, Kaenic Rookern (shield magique), Spirit Visage, "
     "Hollow Radiance, Abyssal Mask, Banshee's Veil (mage), Maw of Malmortius / Wit's End (AD).\n"
     "Équipe mixte : Jak'Sho, The Protean (armor + MR) pour les tanks."),

    ("guide_items_vs_poke",
     "ITEMS / RUNES — VS POKE, KITE, SIEGE (Xerath, Vel'Koz, Ziggs, Jayce, Varus, Ezreal, Lux, Zoe, Hwei, Caitlyn)\n"
     "- Runes : Second Wind, Revitalize, Conditioning, Font of Life ; départ Doran's Shield (top/mid/ADC).\n"
     "- Items : Spirit Visage / Hollow Radiance, Kaenic Rookern (bloque le poke magique), Dead Man's Plate / "
     "Boots of Swiftness pour recoller sur les kiteurs.\n"
     "- Compo : prévoir un engage fort (Malphite, Ornn, Leona, Rell, Nautilus)."),

    ("guide_items_vs_invisible",
     "VS CHAMPIONS INVISIBLES / CAMOUFLÉS (Evelynn, Twitch, Kha'Zix, Rengar, Shaco, Pyke, Akali, Vayne R, Talon R, Wukong, Neeko)\n"
     "- Oracle Lens (trinket rouge) + Control Ward permanente. Support et jungle passent en Oracle Lens.\n"
     "- Umbral Glaive (AD lethality) : révèle/désactive les wards et pièges (Teemo, Shaco, Jhin, Nidalee, Caitlyn, Maokai).\n"
     "- Horizon Focus (mage) : révèle les ennemis touchés à longue portée."),

    ("guide_runes_situationnelles",
     "RUNES — ADAPTATION SELON LA GAME\n"
     "Eyeball Collection, Zombie Ward, Ghost Poro, Ingenious Hunter, Nullifying Orb, Galeforce, Everfrost ont été retirés du "
     "jeu — ne jamais les recommander.\n"
     "- Lane dure / poke : secondaire Resolve Second Wind + Bone Plating ou Revitalize. Doran's Shield.\n"
     "- Vs burst all-in (Darius, Renekton, Pantheon, Zed) : Bone Plating.\n"
     "- Vs beaucoup de CC : Unflinching / Legend: Haste, Mercury's Treads.\n"
     "- Vs tanks : Cut Down, Conqueror, Demolish (siège tour).\n"
     "- Vs squishies : Coup de Grace, Electrocute / Dark Harvest / Hail of Blades.\n"
     "- Combat long (bruisers) : Conqueror + Triumph + Last Stand.\n"
     "- Kite / range : Fleet Footwork (sustain lane), Lethal Tempo / Press the Attack (ADC).\n"
     "- Mages : Manaflow Band, Presence of Mind.\n"
     "- Jungle : Relentless Hunter / Treasure Hunter / Ultimate Hunter, Cosmic Insight / Approach Velocity.\n"
     "Les runes exactes par champion et par matchup (win rate réel op.gg) sont dans les fiches BUILD et MATCHUP."),

    ("guide_spells",
     "SUMMONER SPELLS — CHOIX SELON LA GAME\n"
     "- Flash : quasi obligatoire. Smite : jungle obligatoire.\n"
     "- Ignite : kill pressure en lane, applique Grievous Wounds ; vs heal en lane.\n"
     "- Teleport : top/mid farm, lane dure, splitpush, champions qui scale.\n"
     "- Heal : ADC standard. Exhaust : vs assassin ou hypercarry (Zed, Katarina, Master Yi, Draven, Samira, Kha'Zix, Rengar).\n"
     "- Barrier : mid vs burst (Zed, Syndra, Veigar, Fizz). Cleanse : vs CC lourd (Leona, Nautilus, Morgana, Ashe, Lux).\n"
     "- Ghost : juggernauts (Darius, Garen, Nasus, Hecarim, Olaf, Udyr) pour coller.\n"
     "Le spell le plus joué et le plus gagnant par champion et par matchup est dans les fiches BUILD / MATCHUP."),

    ("guide_compo",
     "ADAPTER SON BUILD À LA COMPO (alliés + ennemis) — méthode pro\n"
     "1. Compte les sources de dégâts ennemies : 3+ AD → armure (Plated Steelcaps, Randuin's Omen, Frozen Heart, Thornmail) ; "
     "3+ AP → MR (Mercury's Treads, Force of Nature, Kaenic Rookern, Spirit Visage).\n"
     "2. Menace principale = le carry fed : défense spécifique contre lui (Zhonya's Hourglass vs Zed, Randuin's Omen vs crit, "
     "Maw of Malmortius vs mage, Mercurial Scimitar vs suppression).\n"
     "3. Heal/shield ennemi → anti-heal / Serpent's Fang dès que le composant est dispo.\n"
     "4. Tanks ennemis → pénétration % (Lord Dominik's Regards, Black Cleaver, Void Staff, Liandry's Torment) ; "
     "squishies → lethality/burst (Youmuu's Ghostblade, Hubris, Profane Hydra, Shadowflame, Stormsurge).\n"
     "5. Ta compo : si ton équipe manque de frontline, top/jungle/support passent tank (Sunfire Aegis, Heartsteel, Jak'Sho) ; "
     "si elle manque de dégâts, build full damage.\n"
     "6. Allié enchanteur (Lulu, Janna, Milio, Nami, Yuumi) → ADC hypercarry/on-hit (Kog'Maw, Jinx, Kai'Sa, Twitch, Zeri) ; "
     "allié engage (Leona, Nautilus, Rell, Alistar) → ADC lane bully (Draven, Samira, Lucian, Kalista).\n"
     "7. Beaucoup d'engage ennemi → peel : Janna/Lulu, Locket of the Iron Solari, Knight's Vow, Mikael's Blessing.\n"
     "Les meilleures synergies par champion (win rate duo réel) sont dans les fiches SYNERGIES."),

    ("guide_counterpick",
     "COMMENT COUNTERPICK — méthode\n"
     "- Vs champion immobile / sans dash (Xerath, Vel'Koz, Ziggs, Veigar) : assassins/dive (Zed, Fizz, Katarina, Kassadin, Qiyana).\n"
     "- Vs assassins : mages avec CC/zhonya (Lissandra, Malzahar, Anivia, Galio) ou tanks.\n"
     "- Vs tanks top : Fiora, Vayne, Gwen, Kayle, Cho'Gath, Mordekaiser (true damage / %HP).\n"
     "- Vs bruisers melee : tops ranged (Quinn, Teemo, Kennen, Jayce, Vayne) ou tanks à armure (Malphite).\n"
     "- Vs dash (Yasuo, Yone, Irelia, Akali) : CC point-and-click (Annie, Malzahar, Renekton W, Pantheon W, Poppy W).\n"
     "- Vs heal (Soraka, Aatrox, Vladimir) : Ignite + anti-heal.\n"
     "Les counters CHIFFRÉS (win rate réel op.gg) sont dans les fiches COUNTERS et MATCHUP : toujours les privilégier."),
]

META = [
    ("meta_wave",
     "Wave management : FREEZE = garder vague juste devant sa tour pour affamer l'ennemi. "
     "SLOW PUSH = laisser grossir la vague pour creer une grosse vague. "
     "FAST PUSH = push rapide avant de roam. "
     "CRASH WAVE = envoyer grosse vague sur la tour juste avant de roam ou TP. "
     "6 CS = 1 kill en or. Farm prioritaire."),
    ("meta_macro",
     "Macro LoL : priorite objectifs — Dragon (ame apres 4 drakes = avantage massif), "
     "Baron Nashor (buff 3 min, empower minions), Rift Herald (detruit tours), "
     "Tourelles (or + pression carte), Inhibiteurs (super minions). "
     "Regle : ne pas mourir pour rien. Jouer autour objectifs pas kills."),
    ("meta_roles",
     "Roles : Top = duel / split push / tanks ou fighters. "
     "Jungle = ganks / objectifs / vision / tempo. "
     "Mid = roam / pression centrale / mages ou assassins. "
     "ADC = DPS constant late / se positionner loin en teamfight. "
     "Support = engage ou peel / vision / proteger ADC."),
    ("meta_vision",
     "Vision : toujours avoir wards actives. Placer avant 5 min en riviere. "
     "Control ward sur objectif (dragon/baron) avant le combat. "
     "DEWARDER / SWEEPER = trinket rouge, nettoyer wards ennemies avant d'engager."),
    ("meta_laning",
     "Laning : POKE = harcelement a distance pour user le HP. "
     "ALL-IN = engagement total quand ennemi est bas HP ou overextended. "
     "SHORT TRADE = echange court favorise les burst champs (Electrocute). "
     "EXTENDED TRADE = echange long favorise les sustain champs (Conqueror). "
     "LANE BULLY = champion qui domine par l'agression. "
     "FREEZE = starve l'ennemi en gardant la vague sous sa tour."),
    ("meta_teamfight",
     "Teamfight : Assassin = attendre que tank engage puis tuer le carry adverse. "
     "Tank/Engage = initier quand ennemi mal positionne (overextended). "
     "ADC = rester a portee max, tirer en continu, NE PAS S'AVANCER. "
     "Mage = zone de controle, AoE sur groupes ennemis. "
     "Support = coller son ADC ou PEEL le carry allie."),
    ("meta_jargon",
     "Vocabulaire pro LoL : "
     "KITE/KITING = se deplacer en attaquant pour maintenir la distance. "
     "PEEL = proteger son carry des dives/engages ennemis. "
     "DIVE = attaquer un ennemi sous sa propre tour. "
     "ENGAGE COMP = compo axee engage/CC (Malphite R, Amumu R). "
     "POKE COMP = compo axee harcelement a distance (Jayce, Ezreal). "
     "PICK COMP = compo axee sur les picks/kill isoles (Blitzcrank, Ahri). "
     "POWERSPIKE = moment ou un champion devient tres fort (item cle, niveau 6). "
     "SNOWBALL = augmenter progressivement son avantage. "
     "RESET = retourner en base pour acheter des items. "
     "COUNTER-JUNGLE = voler les camps du jungler adverse. "
     "INVADE = entrer dans la jungle ennemie pour fight ou voler. "
     "TP TRADE = utiliser Teleport pour rejoindre une fight apres avoir push. "
     "SPLITPUSH = pousser seul une side lane pendant que l'equipe tient ailleurs. "
     "HARD COUNTER = champion qui ecrase le matchup (ex: Malphite vs ADC). "
     "GANK = attaque soudaine d'une lane par le jungler."),
    ("meta_items",
     "Items LoL : LETHALITY = perce l'armure a plat (Serrated Dirk, Youmuu's Ghostblade). "
     "ARMOR PEN = % armor penetration (Lord Dominik's Regards, Serylda's Grudge). "
     "MAGIC PEN = perce la MR (Void Staff, Sorcerer's Shoes). "
     "GRIEVOUS WOUNDS = reduit les soins (Thornmail, Mortal Reminder, Morellonomicon). "
     "SHIELDS = bouclier qui absorbe les degats (Sterak's Gage, Immortal Shieldbow). "
     "ON-HIT = effets declenches par les autos (Kraken Slayer, Blade of The Ruined King). "
     "CRIT = coups critiques (Infinity Edge augmente les degats critiques)."),
]

# ══════════════════════════════════════════════════════════════════════════════
# CLIENTS HTTP (op.gg + Data Dragon)
# ══════════════════════════════════════════════════════════════════════════════

http = httpx.Client(timeout=60, headers=HEADERS)


def get_json(url: str, retries: int = 4):
    """GET JSON avec quelques essais (op.gg coupe parfois une requête)."""
    for i in range(retries):
        try:
            r = http.get(url)
            r.raise_for_status()
            return r.json()
        except Exception:
            if i == retries - 1:
                raise
            time.sleep(2 * (i + 1))


def call_mcp(tool: str, args: dict, retries: int = 4):
    """Appelle un outil du serveur MCP officiel d'op.gg (JSON-RPC)."""
    payload = {"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": {"name": tool, "arguments": args}}
    for i in range(retries):
        try:
            r = http.post(OPGG_MCP, json=payload,
                          headers={"Content-Type": "application/json", "Accept": "application/json, text/event-stream"})
            j = r.json()
        except Exception:
            if i == retries - 1:
                raise
            time.sleep(2 * (i + 1))
            continue
        if "error" in j:   # réponse claire d'op.gg (ex : pas de données) : inutile de réessayer
            raise RuntimeError(j["error"].get("message", j["error"]))
        texte = j["result"]["content"][0]["text"]
        try:
            return json.loads(texte)
        except json.JSONDecodeError:
            return texte   # certains outils répondent en format texte compact


def load_dd_data():
    """Data Dragon (Riot) : version du patch + noms des champions, items, runes, spells."""
    version = get_json("https://ddragon.leagueoflegends.com/api/versions.json")[0]
    base = f"https://ddragon.leagueoflegends.com/cdn/{version}/data/en_US"
    champs = get_json(f"{base}/champion.json")["data"]
    items  = get_json(f"{base}/item.json")["data"]
    runes  = get_json(f"{base}/runesReforged.json")
    spells = get_json(f"{base}/summoner.json")["data"]

    champ_names = {int(c["key"]): c["name"] for c in champs.values()}
    champ_names[20] = "Nunu"   # "Nunu & Willump" : nom court, celui qu'on tape dans une question
    rune_names = {}
    for tree in runes:
        rune_names[tree["id"]] = tree["name"]
        for slot in tree["slots"]:
            for r in slot["runes"]:
                rune_names[r["id"]] = r["name"]
    return {
        "version": version,
        "champ_list": [(c["name"], c["id"]) for c in champs.values()],   # (nom affiché, id Data Dragon)
        "champ_keys": {int(c["key"]): c["id"] for c in champs.values()},  # id numérique → id Data Dragon
        "champ_names": champ_names,
        "item_names": {int(k): v["name"] for k, v in items.items()},
        "rune_names": rune_names,
        "spell_names": {int(v["key"]): v["name"] for v in spells.values()},
    }

# ══════════════════════════════════════════════════════════════════════════════
# ETAPE 1a — COLLECTE op.gg (réponses brutes en cache, reprise automatique)
# ══════════════════════════════════════════════════════════════════════════════

def save_json(path: str, obj, indent=None):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=indent)


def load_json(path: str):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def collect(dd: dict, cache: str) -> dict:
    """Télécharge : liste méta, 1 page par champion/rôle, synergies, et les guides de matchup."""
    os.makedirs(cache, exist_ok=True)
    keys = dd["champ_keys"]

    meta = get_json(f"{OPGG_API}?tier={TIER}")
    save_json(f"{cache}/meta.json", meta)

    # Rôles vraiment joués par chaque champion (>= 8% de ses games, assez de données)
    pairs = [(c["id"], p["name"]) for c in meta["data"] for p in c["positions"]
             if p["stats"]["role_rate"] >= 0.08 and p["stats"]["play"] >= 800 and c["id"] in keys]
    print(f"    {len(pairs)} couples champion/rôle")

    def page(cid, pos):   # builds, runes, items, counters (win rate par adversaire)
        f = f"{cache}/rest_{cid}_{pos}.json"
        if not os.path.exists(f):
            save_json(f, get_json(f"{OPGG_API}/{cid}/{pos.lower()}?tier={TIER}"))

    def synergies(cid, pos):   # meilleurs alliés par rôle (réponse en texte compact)
        f = f"{cache}/syn_{cid}_{pos}.txt"
        if not os.path.exists(f):
            champs = [f"data.synergies.{p}[].{{synergy_champion_name,synergy_position,win_rate,play}}"
                      for p in POS_MCP.values()]
            r = call_mcp("lol_get_champion_analysis", {
                "champion": keys[cid].upper(), "position": POS_MCP[pos], "game_mode": "ranked", "tier": TIER,
                "desired_output_fields": ["data.damage_type", "data.skill_combos[].{name}"] + champs})
            with open(f, "w", encoding="utf-8") as fh:
                fh.write(str(r))

    inutiles = {"trends", "game_lengths", "rune_pages", "skill_masteries", "skill_evolves",
                "mythic_items", "single_runes", "summary", "counters"}

    def matchup(cid, oid, pos):   # build + conseils spécifiques contre un adversaire
        f = f"{cache}/mu_{cid}_{oid}_{pos}.json"
        if not os.path.exists(f):
            r = call_mcp("lol_get_lane_matchup_guide", {
                "my_champion": keys[cid].upper(), "opponent_champion": keys[oid].upper(),
                "position": POS_MCP[pos], "lang": "en_US"})
            if isinstance(r, dict):
                r["data"] = {k: v for k, v in r["data"].items() if k not in inutiles}
            save_json(f, r)

    def run(tasks, label):
        erreurs = 0
        with ThreadPoolExecutor(WORKERS) as ex:
            futures = [ex.submit(fn, *args) for fn, *args in tasks]
            for i, fut in enumerate(as_completed(futures), 1):
                try:
                    fut.result()
                except Exception:
                    erreurs += 1   # op.gg n'a pas de données pour quelques couples rares
                if i % 100 == 0 or i == len(futures):
                    print(f"    {label} : {i}/{len(futures)}")
        if erreurs:
            print(f"    {erreurs} requêtes sans données (ignorées)")

    print("[1] Builds + synergies par champion/rôle...")
    run([(page, c, p) for c, p in pairs] + [(synergies, c, p) for c, p in pairs], "champions")

    # Les N adversaires les plus fréquents de chaque champion/rôle
    matchups = []
    for cid, pos in pairs:
        f = f"{cache}/rest_{cid}_{pos}.json"
        if not os.path.exists(f):
            continue
        adversaires = [o for o in load_json(f)["data"].get("counters", []) if o["play"] >= 100 and o["champion_id"] in keys]
        adversaires.sort(key=lambda o: -o["play"])
        matchups += [(matchup, cid, o["champion_id"], pos) for o in adversaires[:N_MATCHUPS]]
    print(f"[2] Guides de matchup ({len(matchups)}, ~1h la première fois)...")
    run(matchups, "matchups")
    return meta

# ══════════════════════════════════════════════════════════════════════════════
# ETAPE 1b — GÉNÉRATION DU CONTEXTE (fiches texte lisibles par le modèle)
# ══════════════════════════════════════════════════════════════════════════════

def slug(name: str) -> str:
    """Même règle que lol_rag.py pour retrouver une fiche par son ID."""
    return name.lower().replace(" ", "_").replace("'", "").replace(".", "")


def pct(x: float) -> str:
    return f"{x * 100:.1f}%"


def win_rate(o: dict) -> float:
    return o["win"] / o["play"] if o.get("play") else 0


def parse_synergies(texte: str):
    """Lit la réponse texte compacte du MCP : Top("Thresh","SUPPORT",7917,0.55)..."""
    syn = {}
    for nom, pos, play, wr in re.findall(r'Top\("([^"]+)","([A-Z]+)",(\d+),([\d.]+)\)', texte):
        syn.setdefault(pos, []).append((nom, int(play), float(wr)))
    degats = re.search(r'Data\("([A-Z]+)"', texte)
    combos = re.findall(r'SkillCombo\("([^"]+)"\)', texte)
    return syn, (degats.group(1) if degats else ""), combos


def build_contexte(dd: dict, cache: str, meta: dict) -> dict:
    CH, ITEM, RUNE, SPELL = dd["champ_names"], dd["item_names"], dd["rune_names"], dd["spell_names"]
    patch, nb_games = meta["meta"]["version"], meta["meta"]["match_count"]
    chunks = []

    def add(id_: str, lignes: list):
        chunks.append({"id": id_, "lignes": [l for l in lignes if l]})   # 1 ligne JSON par ligne de fiche

    def noms(ids, table=ITEM):
        return " + ".join(table.get(i, str(i)) for i in ids)

    def options(lst, n, table=ITEM):
        return " ; ".join(f"{noms(o['ids'], table)} [{pct(o['pick_rate'])} pick, {pct(win_rate(o))} WR]" for o in lst[:n])

    def page_runes(r):
        prim = [RUNE.get(i, str(i)) for i in r["primary_rune_ids"]]
        sec = [RUNE.get(i, str(i)) for i in r["secondary_rune_ids"]]
        shards = ", ".join(SHARDS.get(i, str(i)) for i in r["stat_mod_ids"])
        return (f"{RUNE.get(r['primary_page_id'])}: {prim[0]} ({', '.join(prim[1:])}) | "
                f"{RUNE.get(r['secondary_page_id'])}: {', '.join(sec)} | Shards: {shards}")

    stats = {(c["id"], p["name"]): p["stats"] for c in meta["data"] for p in c["positions"]}
    pages = {}
    for f in os.listdir(cache):
        if f.startswith("rest_"):
            _, cid, pos = f[:-5].split("_")
            pages[(int(cid), pos)] = load_json(f"{cache}/{f}")["data"]

    # Win rate de chaque champion contre chaque adversaire (assez de games pour être fiable)
    wr_vs = {}
    for (cid, pos), d in pages.items():
        seuil = max(60, stats[(cid, pos)]["play"] * 0.004)
        wr_vs[(cid, pos)] = {o["champion_id"]: (win_rate(o), o["play"]) for o in d.get("counters", [])
                             if o["play"] >= seuil and o["champion_id"] in CH}

    roles = {}
    for cid, pos in pages:
        roles.setdefault(cid, []).append(pos)

    # ── Fiches champion : build par rôle, counters, bons matchups, synergies ──
    for cid, positions in roles.items():
        nom = CH[cid]
        s = slug(nom)
        positions.sort(key=lambda p: -stats[(cid, p)]["role_rate"])   # rôle principal en premier
        resume = [f"BUILD COMPLET — {nom} — patch {patch} (op.gg Emerald+, stats réelles)"]

        for i, pos in enumerate(positions):
            d, st = pages[(cid, pos)], stats[(cid, pos)]
            td = st.get("tier_data") or {}
            f_syn = f"{cache}/syn_{cid}_{pos}.txt"
            syn, degats, combos = parse_synergies(open(f_syn, encoding="utf-8").read()) if os.path.exists(f_syn) else ({}, "", [])
            runes, core, skills = d.get("runes", []), d.get("core_items", []), d.get("skill_masteries", [])
            ordre = ""
            if skills:
                ordre = "max " + " > ".join(skills[0]["ids"])
                if skills[0].get("builds"):
                    ordre += " | niveaux 1-6 : " + "-".join(skills[0]["builds"][0]["order"][:6])
            premier_core = set(core[0]["ids"]) if core else set()

            add(f"build_{s}_standard" if i == 0 else f"build_{s}_{pos.lower()}", [
                f"BUILD {nom} {POSITIONS[pos]} — patch {patch} (op.gg Emerald+)",
                f"{nom} {POSITIONS[pos]} — Tier {TIERS.get(td.get('tier'), '?')} (rang {td.get('rank', '?')} du rôle) | "
                f"WR {pct(st['win_rate'])} | pick {pct(st['pick_rate'])} | ban {pct(st.get('ban_rate', 0))} | "
                f"joué {pct(st['role_rate'])} du temps dans ce rôle" + (f" | dégâts {degats}" if degats else ""),
                f"Summoner Spells : {options(d.get('summoner_spells', []), 2, SPELL)}",
                f"Runes #1 : {page_runes(runes[0])} [{pct(runes[0]['pick_rate'])} pick, {pct(win_rate(runes[0]))} WR]" if runes else "",
                f"Runes #2 (alternative) : {page_runes(runes[1])} [{pct(runes[1]['pick_rate'])} pick, {pct(win_rate(runes[1]))} WR]" if len(runes) > 1 else "",
                f"Ordre sorts : {ordre}" if ordre else "",
                f"Départ : {options(d.get('starter_items', []), 2)}",
                f"Bottes : {options(d.get('boots', []), 3)}",
                f"Core build (3 items, ordre d'achat) : {options(core, 3)}",
                "Items situationnels / fin de build : " + ", ".join(
                    f"{noms(o['ids'])} ({pct(o['pick_rate'])})" for o in d.get("last_items", [])[:12] if o["ids"][0] not in premier_core),
                ("Combos : " + " | ".join(combos[:4])) if combos else "",
            ])

            vs = wr_vs[(cid, pos)]
            if vs:
                pires = sorted(vs.items(), key=lambda x: x[1][0])[:10]
                meilleurs = sorted(vs.items(), key=lambda x: -x[1][0])[:10]
                suffixe = "" if i == 0 else f"_{pos.lower()}"
                add(f"counters_{s}{suffixe}", [
                    f"COUNTERS de {nom} {POSITIONS[pos]} (patch {patch}, op.gg Emerald+) — champions à pick CONTRE {nom} "
                    f"(win rate de {nom} dans le matchup, plus bas = meilleur counter) : " +
                    ", ".join(f"{CH[o]} ({nom} {pct(w)} WR, {n} games)" for o, (w, n) in pires)])
                add(f"strong_{s}{suffixe}", [
                    f"{nom} {POSITIONS[pos]} est FORT contre (patch {patch}, op.gg Emerald+) — bons matchups pour pick {nom} : " +
                    ", ".join(f"{CH[o]} ({nom} {pct(w)} WR, {n} games)" for o, (w, n) in meilleurs)])
            if syn:
                add(f"synergie_{s}_{pos.lower()}", [
                    f"SYNERGIES {nom} {POSITIONS[pos]} — meilleurs alliés (win rate en duo, op.gg Emerald+, patch {patch}) : " +
                    " | ".join(f"{POSITIONS.get(p, p)} : " + ", ".join(f"{n} ({pct(w)}, {pl} games)" for n, pl, w in v)
                               for p, v in syn.items())])

            keystone = RUNE.get(runes[0]["primary_rune_ids"][0]) if runes else "?"
            spells = noms(d["summoner_spells"][0]["ids"], SPELL) if d.get("summoner_spells") else "?"
            resume.append(f"- {POSITIONS[pos]} ({pct(st['role_rate'])} des games) : Tier {TIERS.get(td.get('tier'), '?')}, "
                          f"WR {pct(st['win_rate'])} | keystone {keystone} | spells {spells} | core {noms(core[0]['ids']) if core else '?'}")
        resume.append(f"Détail dans BUILD {nom} <rôle>, COUNTERS de {nom}, MATCHUP {nom} vs ...")
        add(f"build_main_{s}", resume)

    # ── Fiches matchup : build et conseils contre un adversaire précis ──
    def pick_rates(lst):
        return {tuple(o["ids"]): o["pick_rate"] for o in lst or []}

    for f in os.listdir(cache):
        if not f.startswith("mu_"):
            continue
        _, cid, oid, pos = f[:-5].split("_")
        cid, oid = int(cid), int(oid)
        r = load_json(f"{cache}/{f}")
        if not isinstance(r, dict) or not (r.get("data") or {}).get("core_items") or cid not in CH or oid not in CH:
            continue
        d, general = r["data"], pages.get((cid, pos), {})
        nom, adv = CH[cid], CH[oid]
        wr = wr_vs.get((cid, pos), {}).get(oid)
        runes = d.get("runes", [])
        # Ce qui est acheté nettement plus souvent dans CE matchup que dans le build général
        adaptations = []
        for cle, table, label in [("summoner_spells", SPELL, "spells"), ("boots", ITEM, "bottes"),
                                  ("starter_items", ITEM, "départ"), ("last_items", ITEM, "item")]:
            ref = pick_rates(general.get(cle))
            for o in (d.get(cle) or [])[:10]:
                avant = ref.get(tuple(o["ids"]), 0)
                if o["pick_rate"] >= 0.12 and o["pick_rate"] >= avant * 1.4 + 0.05:
                    adaptations.append(f"{label} {noms(o['ids'], table)} {pct(o['pick_rate'])} dans ce matchup (vs {pct(avant)} en général)")
        premiers = (d.get("single_items") or [{}])[0].get("items", [])
        avantage = d.get("lane_advantage_champion")
        add(f"matchup_{slug(nom)}_vs_{slug(adv)}_{pos.lower()}", [
            f"MATCHUP {nom} vs {adv} ({POSITIONS[pos]}) — patch {patch} — Tu joues {nom} contre {adv}.",
            f"Win rate de {nom} dans ce matchup : {pct(wr[0])} sur {wr[1]} games (op.gg Emerald+)." if wr else "",
            f"Avantage en lane : {'égal' if avantage == 'EVEN' else avantage} | avantage solo-kill : "
            f"{d.get('lane_solo_kill_advantage_champion', '?')} | style recommandé : {d.get('recommended_play_style', '?')}",
            f"Conseil vs {adv} : {d['opponent_champion_tip']}" if d.get("opponent_champion_tip") else "",
            f"Spells : {options(d.get('summoner_spells', []), 2, SPELL)}",
            f"Runes : {page_runes(runes[0])} [{pct(runes[0]['pick_rate'])} pick]" if runes else "",
            f"Runes alt : {page_runes(runes[1])} [{pct(runes[1]['pick_rate'])} pick]" if len(runes) > 1 else "",
            f"Départ : {options(d.get('starter_items', []), 2)}",
            f"Bottes : {options(d.get('boots', []), 2)}",
            ("Premier item : " + ", ".join(f"{noms(o['ids'])} ({pct(o['pick_rate'])})" for o in premiers[:3])) if premiers else "",
            f"Core build vs {adv} : {options(d['core_items'], 2)}",
            ("Adaptations spécifiques à ce matchup : " + " ; ".join(adaptations[:6])) if adaptations else "",
        ])

    # ── Tier list par rôle ──
    for pos, label in POSITIONS.items():
        lignes = []
        for c in meta["data"]:
            for p in c["positions"]:
                st = p["stats"]
                if p["name"] == pos and st["role_rate"] >= 0.08 and st["play"] >= 800 and c["id"] in CH:
                    td = st.get("tier_data") or {}
                    lignes.append((td.get("rank", 999), CH[c["id"]], td.get("tier"), st))
        lignes.sort()
        add(f"meta_tierlist_{pos.lower()}",
            [f"TIER LIST {label} — patch {patch} (op.gg Emerald+, {nb_games} games analysées). Meilleurs picks du moment :"] +
            [f"{i}. {n} — Tier {TIERS.get(t, '?')}, WR {pct(st['win_rate'])}, pick {pct(st['pick_rate'])}, ban {pct(st.get('ban_rate', 0))}"
             for i, (_, n, t, st) in enumerate(lignes[:30], 1)])

    for id_, texte in GUIDES + META:
        add(id_, texte.split("\n"))

    return {
        "patch": patch,
        "source": f"op.gg ({TIER}, global) + Data Dragon",
        "games": nb_games,
        "champions": sorted(set(CH.values())),   # utilisé par lol_rag.py pour détecter les champions
        "chunks": chunks,
    }


def run_scrape():
    print("\n" + "=" * 60)
    print("  ETAPE 1 — SCRAPE op.gg -> " + CONTEXTE_FILE)
    print("=" * 60)
    dd = load_dd_data()
    cache = f"{CACHE_DIR}/{dd['version']}"   # un cache par patch : un nouveau patch repart de zéro
    print(f"Data Dragon v{dd['version']} — {len(dd['champ_list'])} champions")
    meta = collect(dd, cache)
    contexte = build_contexte(dd, cache, meta)
    save_json(CONTEXTE_FILE, contexte, indent=2)   # indenté : lisible à l'œil
    print(f"\nOK {CONTEXTE_FILE} : {len(contexte['chunks'])} fiches, patch {contexte['patch']}")

# ══════════════════════════════════════════════════════════════════════════════
# ETAPE 2 — INDEXATION CHROMADB
# ══════════════════════════════════════════════════════════════════════════════

def clean(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def run_index():
    import ollama
    import chromadb

    print("\n" + "=" * 60)
    print("  ETAPE 2 — INDEXATION CHROMADB")
    print("=" * 60)

    client = chromadb.PersistentClient(path=DB_PATH)
    try: client.delete_collection("lol")
    except Exception: pass
    collection = client.create_collection("lol")

    chunks, ids = [], []
    def add(id_: str, text: str):
        if text.strip() and id_ not in ids:
            chunks.append(text.strip()); ids.append(id_)

    # 1. contexte_opgg.json — builds, counters, matchups, synergies, tier lists, guides, méta
    contexte = load_json(CONTEXTE_FILE)
    print(f"[1] {CONTEXTE_FILE} (patch {contexte['patch']})...")
    for c in contexte["chunks"]:
        add(c["id"], "\n".join(c["lignes"]))
    print(f"    {len(chunks)} chunks")

    # 2. Data Dragon — descriptions des sorts (Q/W/E/R)
    #    Utile pour répondre à "comment fonctionne le Q de X ?"
    print("[2] Sorts Data Dragon...")
    dd = load_dd_data()
    spells_ok = 0
    for name, dd_id in dd["champ_list"]:
        try:
            detail = get_json(
                f"https://ddragon.leagueoflegends.com/cdn/{dd['version']}/data/en_US/champion/{dd_id}.json"
            )["data"][dd_id]
            passif = detail["passive"]
            sorts_txt = "\n".join(
                f"  {['Q','W','E','R'][i]}: {s['name']} — {clean(s['description'])[:200]}"
                for i, s in enumerate(detail["spells"])
            )
            add(f"spells_{dd_id}", (
                f"Abilities de {name} :\n"
                f"  Passif: {passif['name']} — {clean(passif['description'])[:200]}\n"
                + sorts_txt
            ))
            spells_ok += 1
        except Exception:
            pass
    print(f"    {spells_ok}/{len(dd['champ_list'])} sorts OK")

    # 3. Patch notes récents : les 2 derniers listés sur le site de Riot
    print("[3] Patch notes...")
    liste = requests.get("https://www.leagueoflegends.com/en-us/news/tags/patch-notes/", headers=HEADERS, timeout=15).text
    patchs = sorted({(int(a), int(b)) for a, b in re.findall(r"league-of-legends-patch-(\d+)-(\d+)-notes", liste)})
    for a, b in patchs[-2:]:
        pid = f"{a}.{b}"
        url = f"https://www.leagueoflegends.com/en-us/news/game-updates/league-of-legends-patch-{a}-{b}-notes/"
        try:
            r = requests.get(url, headers=HEADERS, timeout=15)
            if r.status_code == 200:
                raw = re.sub(r"<script[^>]*>.*?</script>", "", r.text, flags=re.DOTALL)
                raw = re.sub(r"<style[^>]*>.*?</style>", "", raw, flags=re.DOTALL)
                add(f"patch_{pid}", f"Patch {pid} notes :\n{clean(raw)[500:4000]}")
                print(f"    Patch {pid} OK")
        except Exception:
            pass

    # Embedding (par lots de 32 : bien plus rapide qu'un appel par chunk)
    print(f"\nEmbedding {len(chunks)} chunks...")
    errors, LOT = 0, 32
    for i in range(0, len(chunks), LOT):
        try:
            embs = ollama.embed(model=EMBED_MODEL, input=chunks[i:i + LOT])["embeddings"]
            collection.add(ids=ids[i:i + LOT], documents=chunks[i:i + LOT], embeddings=embs)
        except Exception:
            errors += len(chunks[i:i + LOT])
        if (i // LOT) % 10 == 0:
            print(f"  {min(i + LOT, len(chunks))}/{len(chunks)}...")

    print(f"\nBase prete : {len(chunks)-errors} chunks ({errors} erreurs).")
    print("Lance : streamlit run app.py")


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    args = sys.argv[1:]
    do_scrape = "--index" not in args
    do_index  = "--scrape" not in args

    if do_scrape:
        run_scrape()
    if do_index:
        run_index()
