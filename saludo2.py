import streamlit as st

st.set_page_config(page_title="Hola Streamlit", page_icon="👋", layout="centered")

st.title("Hola, Streamlit Cloud")

st.write("Esta es una app mínima desplegada en Streamlit Community Cloud.")

name = st.text_input("¿Cómo te llamas?")

if name:
    st.success(f"¡Encantado, {name}!")