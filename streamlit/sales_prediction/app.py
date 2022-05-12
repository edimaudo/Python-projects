#------------------
# Load libraries
#------------------
import streamlit as st
import pandas as pd
import plotly.express as px
import datetime
import matplotlib.pyplot as plt
import os, os.path

#------------------
# Load data
#------------------
@st.cache
def load_data(filename):
	data = pd.read_excel(filename)
	return data

sales_file = "Sales.xlsx"
sales = load_data(sales_file)

st.title('Sales Insights & Prediction')
#------------------
# Sales Analysis
#------------------
st.header("Sales Analysis")

#Sidebar
#geo_area_selectbox = st.sidebar.selectbox('Organization',organization_info)
#submit_checkbox = st.sidebar.checkbox('UPDATE')
st.sidebar.button("Run")


st.subheader("Data")
# Review the data
with st.expander("Open to see more"):
    st.dataframe(sales)

st.subheader("Sales Trend")
#(Country and ItemCode selection)
# Sales trend

st.subheader("Country Sales Performance")
#Top 5 
#bottom 5 

st.subheader("Item Sales Performance")
#Top 5 Country
#bottom 5 Country

st.header("Sales Prediction")
# by Countr(y/ies) & Item(s)
# build using prophet