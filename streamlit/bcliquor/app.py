import streamlit as st
import pandas as pd
import numpy as np
import os, os.path
import plotly.express as px

######################
# Load data
######################
path = os.path.dirname(__file__)
def load_data():
    data = pd.read_csv(DATA_URL)
    return data
DATA_URL = path + "bcl-data.csv"
df = load_data()

######################
# Title
######################
st.set_page_config(
    page_title="BC Liquor Store Prices",
)
st.set_option('deprecation.showPyplotGlobalUse', False)
######################
# Main Page
######################
st.title("BC Liquor Store Prices")

######################
# Sidebar 
######################
# Input features
price_input = st.sidebar.slider("Price ($): ",min_value=0.0, max_value=100.0,step=5.0, value=(25.0,40.0))
product_input = st.sidebar.radio("Product ", ("BEER", "REFRESHMENT", "SPIRITS", "WINE"), index=3)

country_list = df['Country'].unique()
country_list  = country_list.astype('str')
country_list.sort()

country_input = st.sidebar.selectbox("Country",country_list)

######################
# Output
######################
store_analysis = df[(df.Price.isin(price_input)) |
                (df.Type == product_input) | 
                (df.Country == country_input)]

df_alchol_agg = df.groupby(['Alcohol_Content']).size().reset_index(name='count')
df_alchol_agg.columns = ['Alcohol Content', 'Count']
fig = px.bar(df_alchol_agg, x="Alcohol Content", y="Count")
st.plotly_chart(fig)

st.dataframe(store_analysis)

