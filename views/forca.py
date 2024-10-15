
import streamlit as st
import random

lista_palavras = []

# Abrir o arquivo de palavras
with open('dados/palavras.txt', 'r') as palavras_file:
    for line in palavras_file:
        lista_palavras.append(line.strip())

st.title("Jogo da Forca")


if "palavra_secreta" not in st.session_state:
  palavra_secreta = random.choice(lista_palavras) # Selecionar uma palavra aleatória
  st.session_state["palavra_secreta"] = palavra_secreta
  palavra_chutada = [] # Criar uma lista com os chutes

  for letra in palavra_secreta:
    # Iniciar a palavra de chutes com um monte de traço
    palavra_chutada.append("_")
  
  st.session_state["palavra_chutada"] = palavra_chutada

st.write(st.session_state["palavra_secreta"])

chute = st.text_input("Chute uma letra",max_chars=1)

acertos = 0
tentativas = 5
acertou = False

if st.button("chutar"):
  palavra_secreta = st.session_state["palavra_secreta"]
  palavra_chutada = st.session_state["palavra_chutada"]

  for index, letra in enumerate(palavra_secreta):
    # Verificando se a letra está na palavra
    if chute == letra:
      palavra_chutada[index] = letra

  palavra_chutada_print = " ".join(palavra_chutada)

  st.write(f"{palavra_chutada_print}")
