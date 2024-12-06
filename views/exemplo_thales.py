import streamlit as st
import random
import pandas as pd


# Title for the app
st.title("Exemplo Thales")

dados_exemplo = {"Coluna_1": [1,2,3,4,5,6,7,8],
                "Coluna_2": [1,2,3,4,5,6,7,8],
                "Coluna_3": [1,2,3,4,5,6,7,8],
                "Coluna_4": [1,2,3,4,5,6,7,8]}

df = pd.DataFrame(dados_exemplo)

colunas = df.columns.unique()

colunas_groupby = st.multiselect("Selecione a coluna",colunas)

groupby_df = pd.DataFrame(df.groupby(colunas_groupby).sum())

colunas_2 = groupby_df.columns.unique()
colunas_groupby = st.multiselect("Selecione a coluna",colunas)

st.dataframe(groupby_df[colunas_2])
