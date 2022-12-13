######################
# Load Libraries
######################
import streamlit as st
import pandas as pd
import plotly.express as px
import os, os.path
import datetime
import re, string
import numpy as np

######################
# Title
######################
st.set_page_config(
    page_title="Vitamin C Products Review",
)
st.set_option('deprecation.showPyplotGlobalUse', False)

######################
# Load data
######################
path = os.path.dirname(__file__)
@st.cache(allow_output_mutation=True)
def load_data():
    data = pd.read_csv(DATA_URL)
    return data
DATA_URL = path + "data.csv"
df = load_data()


######################
# Main Page
######################
st.title("Vitamin C Amazon Product reviews")
######################
# Sidebar 
######################
year_list = df['Year'].unique()
year_list  = year_list.astype('int')
year_list.sort()

month_list = df['Month'].unique()
month_list  = month_list.astype('str')
month_list = pd.DataFrame(month_list,columns = ['Month'])

month_dict = {'January':1,'February':2,'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 
'August':8, 'September':9, 'October':10, 'November':11, 'December':12}
month_list = month_list.sort_values('Month', key = lambda x : x.apply (lambda x : month_dict[x]))
month_list = month_list['Month'].values.tolist()

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

######################
# Output
######################
# Summary
st.subheader("Summary")
with st.expander(""):
    # Avg ratings
    st.metric("Avg. Rating", "{:.2f}".format(df["Rating"].mean()))
    # of countries
    st.metric("# of countries",  len(df['Country'].unique()))

# Visualization
st.subheader("Visualization")
with st.expander(""):
    df_info = df[(df.Country == country_input) 
    & (df.Year.isin(year_input)) 
    & (df.Month.isin(month_input)) 
    & (df.Rating.isin(rating_input))]

#Ratings by year
#Month rating



# Text Analysis
st.subheader("Text Analysis")
clicked = st.button("Generate Insights")