
import streamlit as st
import requests
import json

url = "https://api.exchangerate-api.com/v4/latest/USD"
my_resquest = requests.get(url)

content = my_resquest.content
dados = json.loads(content)

st.title("Conversor de moeda")

col_1,col_2 = st.columns(2)

with col_1:
  seletor_moeda_1 = st.selectbox("Selecione uma moeda de",["moeda_1","moeda_2"])
  seletor_moeda_2 = st.selectbox("Selecione uma moeda para",["moeda_1","moeda_2"])
  valor_para_conversao = st.number_input("Selecione o valor para converter",value=float,min_value=0.0,format="%0.2f")

with col_2:
  st.markdown("## R$ 100")
