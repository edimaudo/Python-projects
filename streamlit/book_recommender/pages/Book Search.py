import streamlit as st
import pandas as pd

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
metric1_column, metric2_column,metric3_column,metric4_column = st.columns(4)

search_df = books.apply(lambda row: row.astype(str).str.contains('name').any(), axis=1)
if search_df.empty:
    	metric1_column.metric("Title", search_df['bookTitle'])
		metric2_column.metric("Publisher", search_df['publisher'])
		metric3_column.metric("ISBN", search_df['ISBN'])
		metric1_column.metric("Publication Year", search_df['yearOfPublication']) 
		metric2_column.metric("Average Rating", ratings[ratings['ISBN'] == search-df['ISBN']]['bookRating'])
		metric3_column.metric("Author", search_df['bookAuthor'])
    


