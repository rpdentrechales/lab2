
import streamlit as st
import random

lista_palavras = []

# Abrir o arquivo de palavras
with open('dados/palavras.txt', 'r') as palavras_file:
    for line in palavras_file:
        lista_palavras.append(line.strip())

st.title("Jogo da Forca")
palavra_secreta = random.choice(lista_palavras) # Selecionar uma palavra aleatória


if "palavra_secreta" in st.session_state:
  pass
else:
  st.session_state["palavra_secreta"] = palavra_secreta

st.write(st.session_state["palavra_secreta"])

st.button("TESTE")
