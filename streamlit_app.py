
import streamlit as st

numero_1 = st.text_input("escreve um número 1")
st.write("+")
numero_2 = st.text_input("escreve um número 2")

if numero_1 and numero_2:
  st.write(f"{numero_1} + {numero_2} = {numero_1 + numero_1}")


