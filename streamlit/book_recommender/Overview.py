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

# AVERAGE RATING
average_rating = "{:.2f}".format(ratings['bookRating'].mean())

# NUMBER OF USERS
number_of_users = users['userID'].count()

# NUMBER OF BOOKS
number_of_books = books['ISBN'].count()

# TOP 5 PUBLISHERS AND BOTTOM 5 PUBLISHERS
book_info = books.groupby(["publisher"]).size().reset_index(name='count')
book_info.columns = ['Publisher','Count']
book_info = book_info.sort_values("Count", ascending=False)

top_5_publishers = book_info.head(5)
bottom_5_publishers = book_info.tail(5)

# TOP 5 BOOKS AND BOTTOM 5 BOOKS
top_5_books = ""
bottom_5_books = ""

# TOP 5 AUTHORS AND BOTTOM 5 AUTHORS
author_info = books.groupby(["bookAuthor"]).size().reset_index(name='count')
author_info.columns = ['Author','Count']
author_info = author_info.sort_values("Count", ascending=False)

top_5_authors = author_info.head(5)
bottom_5_authors = author_info.tail(5)
# TOP AND BOTTOM 5 COUNTRIES
top_5_countries = ""
bottom_5_countries = ""
# NUMBER OF BOOKS BY YEAR
number_books_year = ""


metric_container = st.container()
metric_container.metric("Avg. Rating", average_rating)
metric_container.metric("# of Users", number_of_users)
metric_container.metric("# of Books", number_of_books)
publisher_column, books_column,country_column = st.columns(3)
publisher_column.write("this is column 1")
publisher_column
books_column
country_column
























