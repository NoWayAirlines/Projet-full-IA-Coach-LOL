"""
app.py — Interface Streamlit de l'assistant LoL.
Lance avec : streamlit run app.py
"""

import streamlit as st
from lol_rag import repondre

st.set_page_config(page_title="LoL Coach IA", page_icon="⚔️", layout="centered")
st.title("⚔️ LoL Coach IA")
st.caption(
    "Coach IA niveau Challenger — builds, matchups, wave management, macro, counters. "
    "Ex: *build teemo vs vi top*, *comment freeze wave vs darius*, *counter vi jungle*"
)

# ── Historique de la conversation ───────────────────────────────────────────
if "historique" not in st.session_state:
    st.session_state.historique = []   # liste de {"role": ..., "content": ...}
if "sources" not in st.session_state:
    st.session_state.sources = []      # sources de la dernière réponse

# ── Affichage du chat ────────────────────────────────────────────────────────
for msg in st.session_state.historique:
    role = "🧑 Toi" if msg["role"] == "user" else "⚔️ Coach"
    # On affiche la version "propre" (sans le bloc CONTEXTE RAG)
    contenu = msg["content"]
    if msg["role"] == "user" and "CONTEXTE RAG" in contenu:
        contenu = contenu.split("QUESTION :")[-1].strip()
    with st.chat_message(msg["role"]):
        st.write(contenu)

# ── Zone de saisie ───────────────────────────────────────────────────────────
question = st.chat_input("Ta question...")

if question:
    # Affiche la question de l'utilisateur
    with st.chat_message("user"):
        st.write(question)

    # Génère la réponse
    with st.chat_message("assistant"):
        with st.spinner("Le coach réfléchit..."):
            reponse, resultats = repondre(question, st.session_state.historique)
        st.write(reponse)

    # Sauvegarde dans l'historique
    # Note : on sauvegarde la version avec CONTEXTE pour que le modèle ait le contexte,
    # mais on affiche la version propre
    st.session_state.historique.append({
        "role": "user",
        "content": question,   # version affichée propre
    })
    st.session_state.historique.append({
        "role": "assistant",
        "content": reponse,
    })
    st.session_state.sources = resultats

# ── Sources de la dernière réponse ───────────────────────────────────────────
if st.session_state.sources:
    with st.expander("📄 Sources utilisées pour la dernière réponse"):
        for morceau in st.session_state.sources["documents"][0]:
            st.markdown(f"- {morceau[:300]}...")

# ── Bouton reset ─────────────────────────────────────────────────────────────
if st.session_state.historique:
    if st.button("🗑️ Nouvelle conversation"):
        st.session_state.historique = []
        st.session_state.sources = []
        st.rerun()