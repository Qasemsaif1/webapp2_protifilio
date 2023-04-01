import streamlit as st
import os

# Interface
st.header("Qasem Saif")

col1, col2 = st.column(2)
with col1:
    st.image("images/photo.png")

with col2:
    st.info(" I am a sustainability consultant working in Europe")
