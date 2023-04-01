import streamlit as st
import os

st.set_page_config(layout='wide')# to change the layout of the page

# Interface

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png" )

with col2:
    st.title("Qasem Saif")
    content = " I am a sustainability consultant working in Europe"
    st.info(content)


