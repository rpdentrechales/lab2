import streamlit as st
import random

# Title for the app
st.title("Button Demonstration")

if "numero_aleatorio" in st.session_state:
  pass
else:
  st.session_state["numero_aleatorio"] = random.randint(1,10)


if st.button("Click Me"):
  st.markdown(f"# {st.session_state["numero_aleatorio"]}")
