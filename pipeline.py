"""
pipeline.py — Pipeline du chatbot LoL coach.

builds.py contient deja 161 champions avec de bons builds (runes, items, conseils).
Ce pipeline :
  1. SCRAPE  : scrape op.gg pour les champions manquants dans builds.py → builds_opgg.py
  2. INDEX   : indexe ChromaDB (builds.py + builds_opgg.py + sorts Data Dragon + meta/strategie)

Usage :
    python pipeline.py           # etape 1 + etape 2
    python pipeline.py --scrape  # etape 1 seulement (scrape les manquants)
    python pipeline.py --index   # etape 2 seulement

Prerequis :
    pip install playwright requests ollama chromadb
    playwright install chromium
    ollama pull nomic-embed-text
"""

import sys
import json
import re
import time
import asyncio
import requests
from pathlib import Path

# ══════════════════════════════════════════════════════════════════════════════
# CONFIG
# ══════════════════════════════════════════════════════════════════════════════

BUILDS_OPGG_FILE = "builds_opgg.py"
PARTIAL_FILE     = "builds_opgg_partial.json"
DB_PATH          = "./lol_db"
EMBED_MODEL      = "nomic-embed-text"
SCRAPE_DELAY     = 2.5
HEADLESS         = True

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

# ══════════════════════════════════════════════════════════════════════════════
# DATA DRAGON (nécessaire pour : liste champions, ID→nom item, coût item)
# ══════════════════════════════════════════════════════════════════════════════

def load_dd_data():
    version = requests.get(
        "https://ddragon.leagueoflegends.com/api/versions.json", headers=HEADERS, timeout=10
    ).json()[0]
    items_raw = requests.get(
        f"https://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/item.json",
        headers=HEADERS, timeout=10
    ).json()["data"]
    item_names, item_costs = {}, {}
    for k, v in items_raw.items():
        if v.get("name"):
            item_names[int(k)] = v["name"]
            item_costs[int(k)] = v.get("gold", {}).get("total", 0)
    champs_raw = requests.get(
        f"https://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion.json",
        headers=HEADERS, timeout=10
    ).json()["data"]
    # (nom_affiche, dd_id, tags)
    champ_list = [(c["name"], c["id"], c.get("tags", [])) for c in champs_raw.values()]
    print(f"Data Dragon v{version} — {len(champ_list)} champions")
    return version, item_names, item_costs, champ_list

# ══════════════════════════════════════════════════════════════════════════════
# RUNES
# ══════════════════════════════════════════════════════════════════════════════

RUNE_NAMES = {
    8005: "Press the Attack", 8008: "Lethal Tempo", 8021: "Fleet Footwork", 8010: "Conqueror",
    8112: "Electrocute", 8124: "Predator", 8128: "Dark Harvest", 9923: "Hail of Blades",
    8214: "Summon Aery", 8229: "Arcane Comet", 8230: "Phase Rush",
    8437: "Grasp of the Undying", 8439: "Aftershock", 8465: "Guardian",
    8351: "Glacial Augment", 8360: "Unsealed Spellbook", 8369: "First Strike",
    9101: "Overheal", 9111: "Triumph", 8009: "Presence of Mind",
    9104: "Legend: Alacrity", 9105: "Legend: Tenacity", 9103: "Legend: Bloodline",
    8014: "Coup de Grace", 8017: "Cut Down", 8299: "Last Stand",
    8126: "Cheap Shot", 8139: "Taste of Blood", 8143: "Sudden Impact",
    8136: "Zombie Ward", 8120: "Ghost Poro", 8138: "Eyeball Collection",
    8135: "Treasure Hunter", 8134: "Ingenious Hunter", 8105: "Relentless Hunter", 8106: "Ultimate Hunter",
    8224: "Nullifying Orb", 8226: "Manaflow Band", 8275: "Nimbus Cloak",
    8210: "Transcendence", 8234: "Celerity", 8233: "Absolute Focus",
    8237: "Scorch", 8232: "Waterwalking", 8236: "Gathering Storm",
    8242: "Demolish", 8446: "Font of Life", 8463: "Shield Bash", 8473: "Nullifying Orb",
    8401: "Conditioning", 8429: "Second Wind", 8444: "Bone Plating",
    8451: "Overgrowth", 8453: "Revitalize", 8440: "Unflinching",
    8306: "Hextech Flashtraption", 8304: "Magical Footwear", 8321: "Perfect Timing",
    8313: "Future's Market", 8352: "Time Warp Tonic", 8345: "Biscuit Delivery",
    8347: "Cosmic Insight", 8410: "Approach Velocity", 8316: "Jack of All Trades",
    5008: "Adaptive Force", 5005: "Attack Speed", 5007: "Ability Haste",
    5002: "Armor", 5003: "Magic Resist", 5001: "Health",
    5010: "Armor (shard)", 5011: "Health (shard)", 5013: "Tenacity (shard)",
}
TREE_NAMES = {8000: "Precision", 8100: "Domination", 8200: "Sorcery", 8400: "Resolve", 8300: "Inspiration"}
KEYSTONES   = {8005, 8008, 8021, 8010, 8112, 8124, 8128, 9923, 8214, 8229, 8230, 8437, 8439, 8465, 8351, 8360, 8369}
KEYSTONE_TO_TREE = {
    8005: 8000, 8008: 8000, 8021: 8000, 8010: 8000,
    8112: 8100, 8124: 8100, 8128: 8100, 9923: 8100,
    8214: 8200, 8229: 8200, 8230: 8200,
    8437: 8400, 8439: 8400, 8465: 8400,
    8351: 8300, 8360: 8300, 8369: 8300,
}

# ══════════════════════════════════════════════════════════════════════════════
# ROLES ET PLAYSTYLES
# ══════════════════════════════════════════════════════════════════════════════

POSITION_DISPLAY = {"top": "Top Lane", "jungle": "Jungle", "mid": "Mid Lane", "adc": "Bot Lane (ADC)", "support": "Support"}
SUMMONER_SPELLS  = {"top": "Flash + Teleport", "jungle": "Flash + Smite", "mid": "Flash + Ignite", "adc": "Flash + Heal", "support": "Flash + Ignite"}
PLAYSTYLES = {
    "top":     "Duel, split push, pression side lane. Farm early, crash wave puis TP ou fight.",
    "jungle":  "Objectifs + ganks. Path optimal, counter-jungle, dewarder avant objectif.",
    "mid":     "Roam + pression centrale. Freeze ou fast push, roam top/bot, snowball.",
    "adc":     "DPS constant late game. Kite, rester a portee max, jamais s'avancer.",
    "support": "Vision, engage/peel, proteger carry. Control ward sur chaque objectif.",
}

# Role par dd_id.lower() (slug op.gg)
CHAMP_ROLE = {
    "chogath": "top", "volibear": "top", "monkeyking": "top", "trundle": "top",
    "poppy": "top", "shen": "top", "yorick": "top", "olaf": "top", "renekton": "top",
    "riven": "top", "pantheon": "top", "quinn": "top", "rumble": "top",
    "kled": "top", "ambessa": "top", "drmundo": "top", "gangplank": "top",
    "tahmkench": "top", "singed": "top", "aatrox": "top", "darius": "top",
    "fiora": "top", "camille": "top", "irelia": "top", "malphite": "top",
    "ornn": "top", "sion": "top", "urgot": "top", "mordekaiser": "top",
    "nasus": "top", "tryndamere": "top", "gnar": "top", "jayce": "top",
    "kennen": "top", "jax": "top", "illaoi": "top", "garen": "top",
    "teemo": "top", "ksante": "top",
    "leesin": "jungle", "vi": "jungle", "amumu": "jungle", "hecarim": "jungle",
    "khazix": "jungle", "graves": "jungle", "lillia": "jungle", "nidalee": "jungle",
    "evelynn": "jungle", "kayn": "jungle", "kindred": "jungle", "warwick": "jungle",
    "elise": "jungle", "nunu": "jungle", "shyvana": "jungle", "fiddlesticks": "jungle",
    "udyr": "jungle", "xinzhao": "jungle", "ivern": "jungle", "viego": "jungle",
    "reksai": "jungle", "briar": "jungle", "belveth": "jungle", "nocturne": "jungle",
    "jarvaniv": "jungle", "gragas": "jungle", "diana": "jungle", "masteryi": "jungle",
    "rammus": "jungle", "sejuani": "jungle", "zac": "jungle", "shaco": "jungle",
    "naafiri": "jungle", "taliyah": "jungle", "ekko": "jungle",
    "ahri": "mid", "akali": "mid", "lux": "mid", "orianna": "mid", "zed": "mid",
    "katarina": "mid", "yasuo": "mid", "yone": "mid", "viktor": "mid", "syndra": "mid",
    "zoe": "mid", "leblanc": "mid", "kassadin": "mid", "azir": "mid",
    "velkoz": "mid", "vex": "mid", "hwei": "mid", "qiyana": "mid",
    "twistedfate": "mid", "corki": "mid", "ryze": "mid", "fizz": "mid",
    "talon": "mid", "xerath": "mid", "ziggs": "mid", "lissandra": "mid",
    "neeko": "mid", "sylas": "mid", "aurora": "mid", "aurelionsol": "mid",
    "veigar": "mid", "karthus": "jungle", "malzahar": "mid",
    "jinx": "adc", "caitlyn": "adc", "jhin": "adc", "kaisa": "adc", "ezreal": "adc",
    "ashe": "adc", "draven": "adc", "samira": "adc", "tristana": "adc", "sivir": "adc",
    "aphelios": "adc", "varus": "adc", "missfortune": "adc", "xayah": "adc",
    "lucian": "adc", "nilah": "adc", "kalista": "adc", "kogmaw": "adc", "twitch": "adc",
    "smolder": "adc", "mel": "adc", "zeri": "adc", "yunara": "adc",
    "thresh": "support", "lulu": "support", "nami": "support", "janna": "support",
    "soraka": "support", "yuumi": "support", "leona": "support", "blitzcrank": "support",
    "nautilus": "support", "morgana": "support", "karma": "support", "sona": "support",
    "taric": "support", "rell": "support", "rakan": "support", "pyke": "support",
    "seraphine": "support", "maokai": "support", "alistar": "support", "braum": "support",
    "renataglasc": "support", "senna": "support", "zilean": "support", "milio": "support",
    "zaahen": "support",
}

# Items a exclure (composants, potions, trinkets)
EXCLUDED_IDS = {
    1001, 1004, 1006, 1011, 1018, 1026, 1027, 1028, 1029, 1031, 1033,
    1036, 1037, 1038, 1042, 1043, 1044, 1045, 1052, 1053, 1054, 1055, 1056,
    1057, 1058, 1082, 1083, 1086, 1101, 1102, 1103,
    2003, 2010, 2031, 2033, 2138, 2139, 2140,
    3340, 3363, 3364, 4638, 4641, 4642, 4643,
    223010, 223031, 223044, 223057,
}

# Override slug op.gg (exceptions au pattern dd_id.lower())
OPGG_SLUG_OVERRIDES = {"Nunu & Willump": "nunu"}

# ══════════════════════════════════════════════════════════════════════════════
# SCRAPER OP.GG
# ══════════════════════════════════════════════════════════════════════════════

async def scrape_champion(page, slug: str, item_names: dict, item_costs: dict) -> dict:
    url = f"https://www.op.gg/lol/champions/{slug}/build"
    result = {"slug": slug}
    captured = []

    async def on_req(r):
        if "opgg-static.akamaized.net" in r.url:
            captured.append(r.url)

    page.on("request", on_req)
    try:
        await page.goto(url, wait_until="networkidle", timeout=35000)
        await asyncio.sleep(2)

        # Runes
        perk_styles, perks = [], []
        for img in captured:
            m = re.search(r"/perkStyle/(\d+)\.png", img)
            if m:
                t = int(m.group(1))
                if t in TREE_NAMES and t not in perk_styles:
                    perk_styles.append(t)
            m2 = re.search(r"/perk/(\d+)\.png", img)
            if m2:
                p = int(m2.group(1))
                if p not in perks:
                    perks.append(p)

        ks_id    = next((p for p in perks if p in KEYSTONES), None)
        ks_name  = RUNE_NAMES.get(ks_id, "?") if ks_id else "?"
        pri_tid  = KEYSTONE_TO_TREE.get(ks_id)
        pri_tree = TREE_NAMES.get(pri_tid, "")
        sec_tree = next((TREE_NAMES[t] for t in perk_styles if t != pri_tid and t in TREE_NAMES), "")
        minors   = [RUNE_NAMES[p] for p in perks if p not in KEYSTONES and p in RUNE_NAMES and p < 9000]

        # Items (filtres par coût > 1400g)
        items_seen = []
        for img in captured:
            m = re.search(r"/item/(\d+)\.png", img)
            if m:
                i = int(m.group(1))
                if i not in items_seen:
                    items_seen.append(i)

        starters = [item_names[i] for i in items_seen if i in EXCLUDED_IDS and i in item_names][:3]
        build_items = []
        for i in items_seen:
            if i in EXCLUDED_IDS or i not in item_names or item_costs.get(i, 0) < 1400:
                continue
            build_items.append(item_names[i])
            if len(build_items) >= 6:
                break

        # Win rate via DOM ciblé
        win_rate = await page.evaluate("""
        () => {
            const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
            const pat = /(4[4-9]|5[0-9]|6[0-2])\\.(\\d{1,2})%/;
            let node;
            while ((node = walker.nextNode())) {
                const m = node.textContent.trim().match(pat);
                if (m) return m[0];
            }
            return '';
        }
        """)

        # Skill order via éléments DOM
        skill_labels = await page.evaluate("""
        () => {
            const labels = [];
            document.querySelectorAll('[class*="skill"], [class*="Skill"], [class*="ability"], [class*="Ability"]').forEach(el => {
                const t = el.textContent.trim();
                if (/^[QWER]$/.test(t)) labels.push(t);
            });
            return labels;
        }
        """)

        skill_order = "R des que possible. Q > W > E."
        if skill_labels and len(skill_labels) >= 3:
            from collections import Counter
            counts = Counter(s for s in skill_labels if s != "R")
            if counts:
                pri = " > ".join(k for k, _ in counts.most_common())
                f5  = "-".join(skill_labels[:5])
                skill_order = f"R des que possible. {pri}. Niveaux 1-5 : {f5}"

        pos = CHAMP_ROLE.get(slug, "mid")
        result.update({
            "role":            POSITION_DISPLAY[pos],
            "playstyle":       PLAYSTYLES[pos],
            "summoner_spells": SUMMONER_SPELLS[pos],
            "runes": {
                "primary_keystone": f"{ks_name} ({pri_tree})" if pri_tree else ks_name,
                "primary_tree":     pri_tree,
                "secondary_tree":   sec_tree,
                "minor_runes":      " | ".join(minors[:4]),
            },
            "skill_order":    skill_order,
            "starting_items": " + ".join(starters) if starters else _default_starter(pos),
            "build_items":    build_items,
            "win_rate":       win_rate,
        })
        page.remove_listener("request", on_req)
        print(f"  OK {slug} ({pos}) | {' > '.join(build_items[:3]) or '?'} | {ks_name} | WR {win_rate}")
        return result
    except Exception as e:
        try: page.remove_listener("request", on_req)
        except Exception: pass
        print(f"  ERR {slug}: {e}")
        result["error"] = str(e)
        return result


async def scrape_counters(page, slug: str) -> dict:
    url = f"https://www.op.gg/lol/champions/{slug}/counters"
    imgs = []

    async def on_req(r):
        if "opgg-static.akamaized.net" in r.url and "/champion/" in r.url:
            m = re.search(r"/champion/([A-Za-z]+)\.png", r.url)
            if m and m.group(1).lower() != slug.replace("-", "").lower():
                imgs.append(m.group(1))

    page.on("request", on_req)
    try:
        await page.goto(url, wait_until="networkidle", timeout=25000)
        await asyncio.sleep(2)
        unique = list(dict.fromkeys(c for c in imgs if 2 < len(c) < 20))
        mid = max(len(unique) // 2, 1)
        page.remove_listener("request", on_req)
        return {"counters": unique[:mid][:6], "strong_vs": unique[mid:mid+6]}
    except Exception as e:
        try: page.remove_listener("request", on_req)
        except Exception: pass
        return {"counters": [], "strong_vs": []}


def _default_starter(pos: str) -> str:
    return {"jungle": "Gustwalker Hatchling + Refillable Potion",
            "support": "Spellthief's Edge + Health Potion x2"}.get(pos, "Doran's Blade + Health Potion")


def generate_builds_opgg(all_data: dict):
    lines = [
        '"""',
        'builds_opgg.py - Champions manquants scrapes depuis op.gg.',
        'Genere par pipeline.py — NE PAS MODIFIER MANUELLEMENT.',
        '"""', "", "BUILDS = {",
    ]
    n = 0
    for slug, d in sorted(all_data.items()):
        if not d.get("role"):
            continue
        name = slug[0].upper() + slug[1:]  # capitalise le slug pour le nom

        def esc(s):
            return str(s).replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ")

        items = d.get("build_items", [])
        lines += [f'    "{name}": {{',
                  f'        "role": "{esc(d["role"])}",',
                  f'        "playstyle": "{esc(d["playstyle"])}",',
                  f'        "summoner_spells": "{esc(d["summoner_spells"])}",',
                  f'        "runes": {{']
        for k, v in d["runes"].items():
            lines.append(f'            "{k}": "{esc(v)}",')
        lines += [f'        }},',
                  f'        "skill_order": "{esc(d["skill_order"])}",',
                  f'        "starting_items": "{esc(d["starting_items"])}",',
                  f'        "win_rate": "{esc(d.get("win_rate", ""))}",']
        if items:
            wr = d.get("win_rate", "")
            items_str = '", "'.join(esc(i) for i in items)
            lines += [f'        "build_paths": {{',
                      f'            "standard": {{',
                      f'                "ordre": ["{items_str}"],',
                      f'                "chemins": {{}},',
                      f'                "note": "Win Rate {esc(wr)} (op.gg).",',
                      f'            }},',
                      f'        }},']
        else:
            lines.append(f'        "build_paths": {{}},')
        if d.get("counters"):
            lines.append(f'        "counters": "{esc(", ".join(d["counters"]))}",')
        if d.get("strong_vs"):
            lines.append(f'        "strong_vs": "{esc(", ".join(d["strong_vs"]))}",')
        if items:
            lines += [f'        "tips": ["{esc("Build : " + " > ".join(items[:4]))}",],']
        lines.append(f'    }},')
        n += 1

    lines += ["}", "", """
def builds_opgg_to_chunks() -> list[tuple[str, str]]:
    result = []
    for champ, d in BUILDS.items():
        slug = champ.lower().replace(" ", "_").replace("'", "").replace(".", "")
        wr = d.get("win_rate", "")
        parts = [
            f"BUILD -- {champ} ({d['role']}) :",
            f"Win Rate (taux de victoire) de {champ} : {wr if wr else 'non disponible'} (source op.gg)",
            f"Keystone : {d['runes'].get('primary_keystone', '?')}",
            f"Arbre 2 : {d['runes'].get('secondary_tree', '')}",
            f"Runes : {d['runes'].get('minor_runes', '')}",
            f"Sorts : {d['skill_order']}",
            f"Depart : {d['starting_items']}",
        ]
        for vn, vd in d.get("build_paths", {}).items():
            ordre = vd.get("ordre", [])
            if ordre:
                parts.append(f"Build : {' > '.join(ordre)}")
        if d.get("counters"):
            parts.append(f"Counters : {d['counters']}")
        if d.get("strong_vs"):
            parts.append(f"Fort contre : {d['strong_vs']}")
        result.append((f"build_main_{slug}", "\\n".join(parts)))
        # Chunk dedie au win rate (pour les questions "winrate de X")
        if wr:
            result.append((f"winrate_{slug}", f"Le win rate (taux de victoire) de {champ} est de {wr} selon op.gg."))
    return result
"""]
    with open(BUILDS_OPGG_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"OK {BUILDS_OPGG_FILE} : {n} champions")


# ══════════════════════════════════════════════════════════════════════════════
# ETAPE 1 — SCRAPE CHAMPIONS MANQUANTS
# ══════════════════════════════════════════════════════════════════════════════

async def run_scrape():
    from playwright.async_api import async_playwright

    print("\n" + "=" * 60)
    print("  ETAPE 1 — SCRAPE OP.GG (172 champions)")
    print("=" * 60)

    version, item_names, item_costs, champ_list = load_dd_data()

    # Charge partial si existe (reprise automatique)
    all_data = {}
    partial = Path(PARTIAL_FILE)
    if partial.exists():
        with open(partial, encoding="utf-8") as f:
            all_data = json.load(f)
        print(f"Reprise : {len(all_data)} / 172 deja scrapes.")

    already_done = set(all_data.keys())

    # Tous les 172 champions, slug = dd_id.lower()
    to_scrape = []
    for name, dd_id, tags in champ_list:
        slug = OPGG_SLUG_OVERRIDES.get(name) or dd_id.lower()
        if slug not in already_done:
            to_scrape.append((name, slug))

    if not to_scrape:
        print("172/172 champions deja scrapes.")
        generate_builds_opgg(all_data)
        return

    print(f"Reste a scraper : {len(to_scrape)} / 172\n")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=HEADLESS, args=["--no-sandbox", "--disable-dev-shm-usage"])
        context = await browser.new_context(
            user_agent=HEADERS["User-Agent"], viewport={"width": 1440, "height": 900}, locale="en-US"
        )
        page = await context.new_page()

        for i, (name, slug) in enumerate(to_scrape):
            print(f"[{i+1}/{len(to_scrape)}] {name} ({slug})...")
            data = await scrape_champion(page, slug, item_names, item_costs)
            counters = await scrape_counters(page, slug)
            data.update(counters)
            all_data[slug] = data

            # Sauvegarde toutes les 5 champions
            if (i + 1) % 5 == 0 or (i + 1) == len(to_scrape):
                with open(partial, "w", encoding="utf-8") as f:
                    json.dump(all_data, f, ensure_ascii=False, indent=2)
                generate_builds_opgg(all_data)
                print(f"  [SAVE] {len(all_data)}/172")
            await asyncio.sleep(SCRAPE_DELAY)

        await browser.close()

    print(f"\nScrape termine : {len(all_data)} champions dans {BUILDS_OPGG_FILE}")


# ══════════════════════════════════════════════════════════════════════════════
# ETAPE 2 — INDEXATION CHROMADB
# ══════════════════════════════════════════════════════════════════════════════

def clean(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def run_index():
    import ollama
    import chromadb
    from builds import builds_to_chunks

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

    # 1. builds.py — 161 champions avec builds complets
    print("[1] builds.py...")
    for id_, txt in builds_to_chunks():
        add(id_, txt)
    print(f"    {len(chunks)} chunks")

    # 2. builds_opgg.py — champions manquants scrapes
    try:
        from builds_opgg import builds_opgg_to_chunks
        before = len(chunks)
        for id_, txt in builds_opgg_to_chunks():
            add(id_, txt)
        print(f"[2] builds_opgg.py : {len(chunks)-before} chunks supplémentaires")
    except ImportError:
        print("[2] builds_opgg.py absent (pas grave, builds.py couvre 161 champions)")

    # 3. Data Dragon — descriptions des sorts (Q/W/E/R) uniquement
    #    Utile pour répondre à "comment fonctionne le Q de X ?"
    print("[3] Sorts Data Dragon...")
    version, _, _, champ_list = load_dd_data()
    spells_ok = 0
    for name, dd_id, tags in champ_list:
        try:
            detail = requests.get(
                f"https://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion/{dd_id}.json",
                headers=HEADERS, timeout=10
            ).json()["data"][dd_id]
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
    print(f"    {spells_ok}/{len(champ_list)} sorts OK")

    # 4. Meta / stratégie / vocabulaire pro
    print("[4] Meta & vocabulaire pro...")
    meta = [
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
         "Items LoL : LETHALITY = perce l'armure (Serrated Dirk, Youmuu's). "
         "ARMOR PEN = % armor penetration (Lord Dominik's, Last Whisper). "
         "MAGIC PEN = perce la MR (Void Staff, Sorcerer's Shoes). "
         "GRIEVOUS WOUNDS = reduit les soins de 40-60% (Thornmail, Mortal Reminder). "
         "SHIELDS = bouclier qui absorbe les degats (Sterak's Gage, Immortal Shieldbow). "
         "ON-HIT = effets declenches par les autos (Kraken Slayer, Statikk Shiv). "
         "CRIT = coups critiques x2 degats (Infinity Edge necessite 60% crit)."),
    ]
    for id_, txt in meta:
        add(id_, txt)
    print(f"    {len(meta)} chunks meta OK")

    # 5. Patch notes recents
    print("[5] Patch notes...")
    for pid, url in [
        ("26.12", "https://www.leagueoflegends.com/en-us/news/game-updates/patch-26-12-notes/"),
        ("26.11", "https://www.leagueoflegends.com/en-us/news/game-updates/patch-26-11-notes/"),
    ]:
        try:
            r = requests.get(url, headers=HEADERS, timeout=15)
            if r.status_code == 200:
                raw = re.sub(r"<script[^>]*>.*?</script>", "", r.text, flags=re.DOTALL)
                raw = re.sub(r"<style[^>]*>.*?</style>", "", raw, flags=re.DOTALL)
                add(f"patch_{pid}", f"Patch {pid} notes :\n{clean(raw)[500:4000]}")
                print(f"    Patch {pid} OK")
        except Exception:
            pass

    # Embedding
    print(f"\nEmbedding {len(chunks)} chunks...")
    errors = 0
    for i, (txt, id_) in enumerate(zip(chunks, ids)):
        try:
            emb = ollama.embed(model=EMBED_MODEL, input=txt)["embeddings"][0]
            collection.add(ids=[id_], documents=[txt], embeddings=[emb])
        except Exception:
            errors += 1
        if (i + 1) % 100 == 0:
            print(f"  {i+1}/{len(chunks)}...")

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
        asyncio.run(run_scrape())
    if do_index:
        run_index()
