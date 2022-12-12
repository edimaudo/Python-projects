######################
# Load Libraries
######################
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
DATA_URL = path + "Olympics.csv"
df = load_data()

######################
# Title
######################
st.set_page_config(
    page_title="Olympic Trends",
)
st.set_option('deprecation.showPyplotGlobalUse', False)
######################
# Main Page
######################
st.title("Olympic Trends")

######################
# Sidebar 
######################
country_list = df['Country'].unique()
country_list  = country_list.astype('str')
country_list.sort()

country_input = st.sidebar.selectbox("Country",country_list)

######################
# Output
######################
df_analysis = df[(df.Country == country_input)]
with st.container():
    col1, col2, col3 = st.columns(3)
    # Country population
    with col1:
        st.metric("Country Population",df_analysis['Population'].head(1)) 
    # Country GDP 
    with col2:
        st.metric("GDP",df_analysis['GDP ($ per capita)'].head(1)) 
    # Area
    with col3:
        st.metric("Area",df_analysis['Area (sq. mi.)'].head(1)) 


st.subheader("**Sex breakdown**")
df_agg = df_analysis.groupby(['Sex']).size().reset_index(name='count')
df_agg.columns = ['Sex', 'Count']
df_agg.sort_values("Count", ascending=True)
fig = px.bar(df_agg, x="Sex", y="Count",orientation='h')
st.plotly_chart(fig)

st.subheader("**Age distribution**")
df_agg = df_analysis.groupby(['Age']).size().reset_index(name='count')
df_agg.columns = ['Age', 'Count']
fig = px.bar(df_agg, x="Age", y="Count")
st.plotly_chart(fig)

st.subheader("**Medals by Year**")
df_medal = df[(df.Country == country_input) & (df.Medal != 'NA')]
df_agg = df_medal.groupby(['Year','Medal']).agg(Total = ('Medal', 'count')).reset_index()
df_agg.columns = ['Year','Medal','Count']
fig = px.bar(df_agg, x="Year", y="Count",color='Medal')
st.plotly_chart(fig)
