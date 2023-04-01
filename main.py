import pandas
import streamlit as st
import pandas as pd   # This library helps reading the data in the csv

st.set_page_config(layout='wide')# to change the layout of the page

# Interface

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png" )

with col2:
    st.title("Qasem Saif")
    content = " I am a sustainability consultant working in Europe"
    st.info(content)


col3,  col4 = st.columns(2)

data = pandas.read_csv('data.csv', sep=";") # storing the data in this variabale. Sep is the columns divider


with col3:
    for index, row in data[:10].iterrows():     # iterrows() function eterates on every raw of the file
        titles = st.header(row['title'])
        images = st.image(f"images/{row['image'][:10]}")



with col4:
    for index, row in data[10:].iterrows():  # iterrows() function eterates on every raw of the file
        titles = st.header(row['title'])
        images = st.image(f"images/{row['image']}")


