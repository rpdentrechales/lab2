
import streamlit as st

numero_1 = st.text_input("escreve um número 1")
operacao = st.selectbox(
    "Selecione a operação",
    ("Soma", "Subtração", "Multiplicação","Divisão")
)
numero_2 = st.text_input("escreve um número 2")

if numero_1 and numero_2:
  numero_1 = int(numero_1)
  numero_2 = int(numero_2)
  
  if operacao == "Soma":
    st.write(f"{numero_1} + {numero_2} = {numero_1 + numero_2}")
  elif operacao == "Subtração":
    st.write(f"{numero_1} - {numero_2} = {numero_1 - numero_2}")
  elif operacao == "Multiplicação":
    st.write(f"{numero_1} * {numero_2} = {numero_1 * numero_2}")
  elif operacao == "Divisão":
    st.write(f"{numero_1} / {numero_2} = {numero_1 / numero_2}")
