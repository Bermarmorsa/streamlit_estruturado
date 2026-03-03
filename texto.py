import streamlit as st



def app_texto():
    st.title('Texto')
    texto = st.text_input('Añade un texto',width=500)
    st.write(texto)
