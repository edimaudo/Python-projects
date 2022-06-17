#================
# Book Recommender
#================


# Load libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import os, os.path
import pandas as pd
import matplotlib.pyplot as plt

st.title('Book Overview')

@st.cache
def load_data(DATA_URL):
    data = pd.read_csv(DATA_URL)
    data.dropna(inplace=True)
    return data

# Load data
books = load_data("BX-Books_clean.csv")
users = load_data("BX-Users_clean.csv") 
ratings = load_data("BX-Book-Ratings_clean.csv") 

#====================
# Raw data
#====================
st.subheader("Book data")
with st.expander("Open to see more",expanded=False):
    st.dataframe(books)

st.header("Book Overview")
name = st.text_input("Book Search")

search_df = books.apply(lambda row: row.astype(str).str.contains('name').any(), axis=1)
#st.metric("User Count", 42)
#st.metric("Average Rating", 42)
















