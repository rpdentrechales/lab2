
import streamlit as st

# --- PAGE SETUP ---
calculadora_page = st.Page(
    "views/calculadora.py",
    title="Calculadora",
    icon=":material/overview:",
)

conversor_page = st.Page(
    "views/conversor.py",
    title="Conversor",
    icon=":material/overview:",
)

forca_page = st.Page(
    "views/forca.py",
    title="Forca",
    icon=":material/overview:",
)


# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Aplicativos": [calculadora_page,conversor_page,forca_page]
    }
)


# --- SHARED ON ALL PAGES ---
# st.logo("assets/codingisfun_logo.png")

# --- RUN NAVIGATION ---
pg.run()
