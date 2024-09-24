
import streamlit as st
import requests
import json

url = "https://api.exchangerate-api.com/v4/latest/USD"
my_resquest = requests.get(url)

content = my_resquest.content
dados = json.loads(content)

siglas_moedas = list(dados["rates"].keys())

st.title("Conversor de moeda")

col_1,col_2 = st.columns(2)

with col_1:
  seletor_moeda_1 = st.selectbox("Selecione uma moeda de",siglas_moedas,index=0)
  valor_para_conversao = st.number_input("Selecione o valor para converter",format="%0.2f")

with col_2:

  seletor_moeda_2 = st.selectbox("Selecione uma moeda para",siglas_moedas,index=20)
  
  conversao_moeda_1 = dados["rates"][seletor_moeda_1]
  conversao_moeda_2 = dados["rates"][seletor_moeda_2]
  
  valor_convertido = (valor_para_conversao * conversao_moeda_2)/conversao_moeda_1
  st.markdown(f"## {seletor_moeda_2} {valor_convertido:0.2f}")
