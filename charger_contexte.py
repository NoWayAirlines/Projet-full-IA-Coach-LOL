"""
charger_contexte.py — Injecte contexte_opgg.json (builds, runes, counters, matchups, synergies,
tier lists, guides d'itemisation — patch actuel, op.gg Emerald+) dans la base ChromaDB existante.

Remplace les anciens builds écrits à la main (items/runes obsolètes) et les stats U.GG.
Pas besoin de relancer scrapper.py. Lance :  python charger_contexte.py
"""

import json
import ollama
import chromadb

DB_PATH     = "./lol_db"
EMBED_MODEL = "nomic-embed-text"
FICHIER     = "contexte_opgg.json"

# Préfixes des anciens chunks périmés à supprimer avant l'injection
PREFIXES_OBSOLETES = ("build_", "matchup_", "counters_", "strong_", "ugg_")

data = json.load(open(FICHIER, encoding="utf-8"))
chunks = data["chunks"]
print(f"Contexte patch {data['patch']} — {len(chunks)} chunks ({data['source']})")

client = chromadb.PersistentClient(path=DB_PATH)
collection = client.get_or_create_collection("lol")

# ── Nettoyage des données périmées ───────────────────────────────────────────
anciens = [i for i in collection.get(include=[])["ids"] if i.startswith(PREFIXES_OBSOLETES)]
for k in range(0, len(anciens), 500):
    collection.delete(ids=anciens[k:k + 500])
print(f"{len(anciens)} anciens chunks supprimés")

# ── Embedding + insertion par lots ───────────────────────────────────────────
LOT = 32
for k in range(0, len(chunks), LOT):
    lot = chunks[k:k + LOT]
    textes = [c["text"] for c in lot]
    embs = ollama.embed(model=EMBED_MODEL, input=textes)["embeddings"]
    collection.upsert(ids=[c["id"] for c in lot], documents=textes, embeddings=embs)
    if (k // LOT) % 10 == 0:
        print(f"   {k + len(lot)}/{len(chunks)} chunks indexés...")

print(f"\nBase à jour : {collection.count()} chunks au total. Lance : streamlit run app.py")
