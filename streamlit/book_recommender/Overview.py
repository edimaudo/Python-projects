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

st.subheader("Book Data Summary")

# AVERAGE RATING
average_rating = "{:.2f}".format(ratings['bookRating'].mean())

# AVERAGE AGE
average_age= "{:.2f}".format(users['Age'].mean())

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

# TOP 5 AUTHORS AND BOTTOM 5 AUTHORS
author_info = books.groupby(["bookAuthor"]).size().reset_index(name='count')
author_info.columns = ['Author','Count']
author_info = author_info.sort_values("Count", ascending=False)
top_5_authors = author_info.head(5)
bottom_5_authors = author_info.tail(5)

# NUMBER OF BOOKS BY YEAR
book_year_info = books.groupby(["yearOfPublication"]).size().reset_index(name='count')
book_year_info.columns = ['Year','Count']
book_year_info = book_year_info.sort_values("Year", ascending=False)

# TOP AND BOTTOM 5 COUNTRIES
country_info = users.groupby(["Country"]).size().reset_index(name='count')
country_info.columns = ['Country','Count']
country_info = country_info.sort_values("Count", ascending=False)
top_5_countries = country_info.head(5)
bottom_5_countries = country_info.tail(5)

# Metrics
metric1_column, metric2_column,metric3_column,metric4_column = st.columns(4)
metric1_column.metric("Avg. Rating", average_rating)
metric2_column.metric("# of Users", number_of_users)
metric3_column.metric("# of Books", number_of_books)
metric4_column.metric("Avg. Age", average_age)

# Publisher
st.subheader("Top and Bottom 5 Publishers")
st.write("Top 5 Publishers")
output = px.bar(top_5_publishers, x="Publisher", y="Count")
st.plotly_chart(output)
st.write("Bottom 5 Publishers")
output = px.bar(bottom_5_publishers, x="Publisher", y="Count")
st.plotly_chart(output)

# Author
st.subheader("Top and Bottom 5 Authors")
st.write("Top 5 Authors")
output = px.bar(top_5_authors, x="Author", y="Count")
st.plotly_chart(output)
st.write("Bottom 5 Authors")
output = px.bar(bottom_5_authors, x="Author", y="Count")
st.plotly_chart(output)

# Country
st.subheader("Top and Bottom 5 Countries")
st.write("Top 5 Countries")
output = px.bar(top_5_countries, x="Country", y="Count")
st.plotly_chart(output)
st.write("Bottom 5 Countries")
output = px.bar(bottom_5_countries, x="Country", y="Count")
st.plotly_chart(output)

# books by year
st.subheader("Books by Year Trend")
output = px.line(book_year_info, x="Year", y="Count")
st.plotly_chart(output)
























