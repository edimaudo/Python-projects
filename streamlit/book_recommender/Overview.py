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

c = st.container()


# Data aggregation
# books + ratings

















