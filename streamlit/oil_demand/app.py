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
DATA_URL = path + "applemobilitytrends-2020-07-23.csv"
df = load_data()

######################
# Title
######################
st.set_page_config(
    page_title="Mobility Trends",
)
st.set_option('deprecation.showPyplotGlobalUse', False)
######################
# Main Page
######################
st.title("Mobility Trends")

######################
# Sidebar 
######################

region_list = df['region'].unique()
region_list  = region_list.astype('str')
region_list.sort()

geo_list = df['geo_type'].unique()
geo_list  = geo_list.astype('str')
geo_list.sort()

transportation_list = df['transportation_type'].unique()
transportation_list = transportation_list.astype('str')
transportation_list.sort()

geography_input = st.sidebar.selectbox("Geography",geo_list)
region_input = st.sidebar.selectbox("Region", region_list)
transportation_input = st.sidebar.multiselect("Transportation Type",transportation_list,transportation_list)

######################
# Output
######################
df_analysis = df[(df.transportation_type.isin(transportation_input)) |
                (df.geo_type == geography_input) | 
                (df.region == region_input)]

df_pivot = df.melt(id_vars=['geo_type', 'region','transportation_type'], var_name='quantity')
df_pivot = df_pivot[['quantity','value', 'transportation_type']]
df_pivot_agg = df_pivot.groupby(['quantity','transportation_type']).agg(Total = ('value', 'sum')).reset_index()
df_pivot_agg.columns = ['Date','Transportation Type', 'Distance']
df_pivot_agg.sort_values("Date", ascending=True)
fig = px.line(df_pivot_agg, x="Date", y="Distance",color='Transportation Type')
#px.line(df_total_grants_agg, x='Fiscal_year', y='Total_Amount_Awarded', color='Budget_fund')
st.plotly_chart(fig)