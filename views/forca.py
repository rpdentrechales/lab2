
import streamlit as st
import random

lista_palavras = []

# Abrir o arquivo de palavras
with open('dados/palavras.txt', 'r') as palavras_file:
    for line in palavras_file:
        lista_palavras.append(line.strip())

st.title("Jogo da Forca")
palavra_secreta = random.choice(lista_palavras) # Selecionar uma palavra aleatória
st.write(palavra_secreta)

st.button("TESTE")
