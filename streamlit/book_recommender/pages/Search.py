import streamlit as st
import pandas as pd
import plotly.express as px
import os, os.path
import matplotlib.pyplot as plt

@st.cache
def load_data(DATA_URL):
    data = pd.read_csv(DATA_URL)
    data.dropna(inplace=True)
    return data

# Load data
books = load_data("BX-Books_clean.csv")
users = load_data("BX-Users_clean.csv") 
ratings = load_data("BX-Book-Ratings_clean.csv") 

st.header("Book Overview")
name = st.text_input("Search by Author or Book Title")
search_df = books.apply(lambda row: row.astype(str).str.contains('name').any(), axis=1)

if search_df.empty:
	st.metric("User Count", 42)
	st.metric("Average Rating", 42)
else:
	# get ratings data
	st.metric("User Count", 42)
	st.metric("Average Rating", 42)	

# user count
# average rating
# top countries & bottom countries