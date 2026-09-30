"""
lol_rag.py — Cerveau de l'assistant LoL.
Récupération intelligente : détecte les champions mentionnés et force la récupération
de leurs builds en plus de la recherche sémantique classique.
"""

import json
import ollama
import chromadb

# Base persistante (remplie par pipeline.py --index)
client = chromadb.PersistentClient(path="./lol_db")


def get_collection():
    """Récupère la collection à chaque appel (évite les références périmées
    quand la base est reconstruite par pipeline.py pendant que l'app tourne)."""
    try:
        col = client.get_collection("lol")
        if col.count() == 0:
            raise ValueError("collection vide")
        return col
    except Exception:
        raise RuntimeError(
            "Base ChromaDB 'lol' introuvable ou vide. "
            "Lance d'abord :  python pipeline.py --index  "
            "(et ne relance pas l'app pendant l'indexation)."
        )

# Noms de tous les champions (générés par pipeline.py --scrape dans contexte_opgg.json)
with open("contexte_opgg.json", encoding="utf-8") as f:
    CHAMPIONS_CONNUS = set(json.load(f)["champions"])

SYSTEM_PROMPT = """Tu es un coach LoL niveau Challenger. Style : pro, direct, dense. Langue de l'utilisateur = langue de la réponse.

RÈGLES :
1. Réponses courtes par défaut. Si l'utilisateur demande plus de détails, développe.
2. Noms de champions, items, sorts, runes : TOUJOURS en anglais. Ne traduis jamais.
3. Items et données : UNIQUEMENT ce qui est dans le CONTEXTE. Si absent, dis "pas de data sur ça".
4. N'invente rien. Jamais.
5. Précise toujours qui joue qui : "Tu joues X vs Y en [lane]." Si ambigu, demande.
6. Chaque item = justification pro en 5 mots max entre parenthèses.
7. MATCHUP : le CONTEXTE peut contenir des conseils de matchup contre un AUTRE adversaire que celui demandé (ex: data "vs Urgot" alors que tu joues vs Aatrox). IGNORE ces conseils hors-sujet. N'utilise QUE les infos pertinentes pour l'adversaire réellement demandé. Ne cite JAMAIS un nom de champion adverse qui n'est pas Y.
8. PRIX DES ITEMS : ne donne un coût en or QUE s'il est écrit dans le CONTEXTE. Sinon n'invente AUCUN prix. Ne mets pas de "(Xg)" inventé.
9. SORTS ≠ ITEMS : Q/W/E/R sont des sorts (abilities), PAS des items à acheter. Ex: "Fishbones", "Pow-Pow", "Flame Chompers" sont les sorts de Jinx, jamais dans le build. Ne mélange jamais sorts et items.
10. Ne parle JAMAIS d'"énergie" sauf si le champion utilise vraiment l'Énergie (Energy) comme ressource (Zed, Akali, Lee Sin...). La plupart des champions utilisent la Mana.
11. Recopie les items EXACTEMENT comme dans le CONTEXTE. N'invente pas d'items (pas de "Zephyr", "Sorcery Shoes" s'ils ne sont pas dans le contexte).

VOCABULAIRE PRO OBLIGATOIRE (utilise ces termes, ne les traduis pas) :
- Wave management : freeze (geler la vague devant sa tour), slow push (faire grossir la vague), fast push (push rapide), crash wave / crashwave (envoyer grosse vague sur tour avant de roam)
- Lane : kite / kiting (se déplacer en attaquant pour maintenir la distance), poke (harcèlement à distance), all-in (engagement total), trading pattern (pattern d'échange), lane bully (champion qui domine par l'agression), short trade / extended trade
- Jungle : gank (attaque soudaine d'une lane), invade (envahir la jungle adverse), counter-jungle, path (chemin de jungle), leash (aide au premier camp), objective control
- Vision : deward / dewarder (retirer les wards ennemies avec sweeper), ward (placer une ward), control ward
- Macro : roam (quitter sa lane), TP trade, splitpush, 1-3-1, grouper (group up), rotation
- Combat : burst (dégâts instantanés), peel (protéger son carry), engage / disengage, dive (attaquer sous tower), hard CC, interrupt, outplay
- Scaling : powerspike (moment de pic de puissance), hypercarry, snowball, reset (retour base)
- Champion class : frontline / backline, engage comp, poke comp, pick comp, dive comp
- Counter : hard counter, counter-pick, favored matchup / losing matchup
- Misc : CS (creep score), itemisation, 6 CS = 1 kill (or), tilt, mental

FORMAT build :
👤 Tu joues : X | vs : Y | Lane : Z
🟢 Départ : ...
🔵 Build :
  1. Item1 (justification)
  2. Item2 (justification)
  3. Item3 (justification)
  4. Item4 (justification)
  5. Item5 (justification)
  6. Item6 (justification)
🔑 Runes : keystone | arbre secondaire
⚡ Spells : ...
📈 Ordre sorts : ...
⚔️ Tips matchup : ..."""


def detecter_champions(texte: str) -> list[str]:
    """Retourne les noms de champions présents dans le texte (insensible à la casse)."""
    texte_lower = texte.lower()
    found = []
    for c in CHAMPIONS_CONNUS:
        # Cherche le nom complet ET version sans caractères spéciaux
        slug = c.lower().replace("'", "").replace(".", "").replace(" ", "")
        if c.lower() in texte_lower or slug in texte_lower.replace(" ", ""):
            found.append(c)
    return found


def recuperer_contexte(question: str, historique: list, n_semantic: int = 5) -> tuple[str, dict]:
    """
    Récupère le contexte en deux étapes :
    1. Force la récupération des builds des champions mentionnés (par ID exact)
    2. Complète avec une recherche sémantique classique
    """
    docs_forces = []
    ids_deja_vus = set()
    collection = get_collection()  # rechargée à chaque requête (évite cache périmé)

    # Cherche les champions dans la question ET toute la conversation
    texte_complet = question + " " + " ".join(
        m["content"] for m in historique if m["role"] == "user"
    )
    champions_detectes = detecter_champions(texte_complet)

    # Force la récupération des fiches de chaque champion détecté (ID exact)
    slugs = [c.lower().replace(" ", "_").replace("'", "").replace(".", "") for c in champions_detectes]
    ids_a_chercher = []
    for slug in slugs:
        ids_a_chercher += [f"build_main_{slug}", f"build_{slug}_standard", f"counters_{slug}", f"strong_{slug}"]
    # Deux champions cités ("Aatrox vs Darius") : fiche matchup, quelle que soit la lane
    for a in slugs:
        for b in slugs:
            if a != b:
                ids_a_chercher += [f"matchup_{a}_vs_{b}_{lane}" for lane in ("top", "jungle", "mid", "adc", "support")]
    try:
        res = collection.get(ids=ids_a_chercher)
        for doc in (res.get("documents") or []):
            if doc and doc not in ids_deja_vus:
                docs_forces.append(doc)
                ids_deja_vus.add(doc)
    except Exception:
        pass

    # Recherche sémantique classique
    q_emb = ollama.embed(model="nomic-embed-text", input=question)["embeddings"][0]
    resultats = collection.query(query_embeddings=[q_emb], n_results=n_semantic)

    # Fusionne sans doublons (builds forcés en premier = prioritaires)
    docs_finaux = list(docs_forces)
    for doc in resultats["documents"][0]:
        if doc not in ids_deja_vus:
            docs_finaux.append(doc)
            ids_deja_vus.add(doc)

    contexte = "\n\n---\n\n".join(docs_finaux)
    return contexte, resultats


def repondre(question: str, historique: list):
    contexte, resultats = recuperer_contexte(question, historique)

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages += historique
    messages.append({
        "role": "user",
        "content": f"CONTEXTE (données réelles LoL — utilise UNIQUEMENT ceci) :\n{contexte}\n\nQUESTION : {question}",
    })

    reponse = ollama.chat(
        model="llama3.1:8b",  # modèle 8B : moins d'hallucinations que llama3.2 3B
        messages=messages,
        options={"temperature": 0.2},  # bas = réponses fidèles au contexte, moins d'inventions
    )["message"]["content"]
    return reponse, resultats
