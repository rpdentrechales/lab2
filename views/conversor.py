
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
  seletor_moeda_1 = st.selectbox("Selecione uma moeda",["moeda_1","moeda_2"])
  seletor_moeda_2 = st.selectbox("Selecione uma moeda",["moeda_1","moeda_2"])

