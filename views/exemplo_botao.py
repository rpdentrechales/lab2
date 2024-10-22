import streamlit as st
import random

# Title for the app
st.title("Button Demonstration")

numero_aleatorio = random.randint(1,10)


if st.button("Click Me"):
  st.markdown(f"# {numero_aleatorio}")
