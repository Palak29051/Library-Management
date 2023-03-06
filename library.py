import streamlit as st
import pandas as pd
from lb_func import *
from PIL import Image

st.set_page_config(page_title="Library management system",page_icon="lb_logo.png",layout="wide")
create_table()

img = Image.open('lb_logo.png')
header = Image.open('lb_header.png')

st.image(header,width=600)
st.title("Library Management System")

st.sidebar.image(img)
st.sidebar.header("Add a new book")
st.sidebar.write("---")

new_title = st.sidebar.text_input("Title")
new_author = st.sidebar.text_input("Author")
available = st.sidebar.selectbox("Available",("Yes","No"))

if st.sidebar.button("Add book"):
    add_data(new_title, new_author, available)
    st.success("Book added!")
    st.balloons()


# Show the list of books
st.write("---")
result = view_all_data()
clean_df = pd.DataFrame(result, columns=["Books", "Author", "Available"])
st.dataframe(clean_df)

st.sidebar.markdown("<br><hr><center>Created by <strong>Palak Raghuwanshi</strong></center><hr>", unsafe_allow_html=True)
