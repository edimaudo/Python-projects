#================
# Sales and Supplier Analysis
#================

#------------------
# Load libraries
#------------------
import streamlit as st
import pandas as pd
import plotly.express as px
import datetime
from pandas.io.json import json_normalize
import os, os.path

#------------------
# Load data
#------------------
@st.cache
def load_data(filename):
	data = pd.read_excel(filename)
	return data

itemfile = "Items.xlsx"
items = load_data(itemfile)
receiving_file = "Receivings.xlsx"
receiving = load_data(receiving_file)
sales_file = "Sales.xlsx"
sales = load_data(sales_file)
supplier_file = "Suppliers.xlsx"
suppliers = load_data(supplier_file)

st.title('Sales and Supplier Insights')



st.header("Supplier Analysis")
st.write("Provides an overview of supplier performance in every country")

st.subheader("Supplier Items by Country")
country_info = suppliers['Country'].unique()
country_info = country_info.astype('str')
country_info = country_info.tolist()
country_info.sort()
country_info.insert(0, "All") #add All
choices = st.selectbox("Countries ", country_info)