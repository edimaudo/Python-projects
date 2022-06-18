#================
# Book Overview
#================
# Load libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import os, os.path
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

# Data aggregation
# books + ratings

st.subheader("Book Data Summary")

# Metrics
metric_container = st.container()
top_bottom_5_container = st.container()
book_year_container = st.container()

# AVERAGE RATING
average_rating = "{:.2f}".format(ratings['bookRating'].mean())

# NUMBER OF USERS
number_of_users = users['userID'].count()

# NUMBER OF BOOKS
number_of_books = books['ISBN'].count()

# TOP 5 PUBLISHERS AND BOTTOM 5 PUBLISHERS
top_5_publishers = ""
bottom_5_publishers = ""

# TOP 5 BOOKS AND BOTTOM 5 BOOKS
top_5_publishers = ""
bottom_5_publishers = ""

# TOP 5 AUTHORS and bottom 5 AUTHORS
top_5_publishers = ""
bottom_5_publishers = ""
# TOP AND BOTTOM 5 COUNTRIES
top_5_publishers = ""
bottom_5_publishers = ""
# NUMBER OF BOOKS BY YEAR COUNT GRAPH
number_books_year = ""






















