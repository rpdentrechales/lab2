
import streamlit as st

# --- PAGE SETUP ---
calculadora_page = st.Page(
    "views/caculadora.py",
    title="Consultoria - Pró-Corpo",
    icon=":material/overview:",
)

conversor_page = st.Page(
    "views/conversor.py",
    title="Área Logada",
    icon=":material/overview:",
)


# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Aplicativos": [calculadora_page,conversor_page]
    }
)


# --- SHARED ON ALL PAGES ---
# st.logo("assets/codingisfun_logo.png")

# --- RUN NAVIGATION ---
pg.run()
