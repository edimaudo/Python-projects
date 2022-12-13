######################
# Load Libraries
######################
import streamlit as st
import pandas as pd
import plotly.express as px
import os, os.path
import datetime
import re, string

######################
# Load data
######################
@st.cache(allow_output_mutation=True)
def load_data():
    #used to fix utf-8 error (https://stackoverflow.com/questions/46000191/utf-8-codec-cant-decode-byte-0x92-in-position-18-invalid-start-byte)
    data = pd.read_csv(DATA_URL,encoding='cp1252') 
    return data
DATA_URL = path + "data.csv"
df = load_data()

######################
# Title
######################
st.set_page_config(
    page_title="Amazon reviews for Vitamin C Products",
)
st.set_option('deprecation.showPyplotGlobalUse', False)

######################
# Main Page
######################
st.title("Amazon reviews for Vitamin C Products")

######################
# Sidebar 
######################
year_list = df['Year'].unique()
year_list  = year_list.astype('int')
year_list.sort()

month_dict = {'January':1,'February':2,'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 
'August':8, 'September':9, 'October':10, 'November':11, 'December':12}
month_list = month_list.sort_values('Month', key = lambda x : x.apply (lambda x : month_dict[x]))

rating_list = df['Rating'].unique()
rating_list  = rating_list.astype('int')
rating_list.sort()


country_list = df['Country'].unique()
country_list  = country_list.astype('str')
country_list.sort()

country_input = st.sidebar.selectbox("Country",country_list)
year_input = st.sidebar.multiselect("Year",year_list, year_list)
month_input = st.sidebar.multiselect("Month",month_list, month_list)
rating_input = st.sidebar.multiselect("Rating",rating_list, rating_list)

# Summary
# Avg ratings
# of countries
# of verified accounts
# of ratings


# Visualization
#Ratings by year
#Month rating
#top 5 countries by avg rating
#bottom 5 countries by avg rating


# Text Analysis