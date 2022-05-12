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

#------------------
# Sales Analysis
#------------------
st.header("Sales Analysis")

st.subheader("Sales Trend")
#(Country and ItemCode selection)
# Sales trend

st.subheader("Country Sales Performance")
#Top 5 items by country
#bottom 5 items by country

st.subheader("Item Sales Performance")
#Top 5 Country
#bottom 5 Country

st.subheader("Sales Prediction")
# by Countr(y/ies) & Item(s)
# build using prophet


#------------------
# Supplier Analysis
#------------------
st.header("Supplier Analysis")
st.write("Provides an overview of supplier performance in every country")

# Generate country dropdown
country_info = suppliers['Country'].unique()
country_info = country_info.astype('str')
country_info = country_info.tolist()
country_info.sort()
country_info.insert(0, "All") #add All
supplier_country_choices = st.selectbox("Countries ", country_info)

st.subheader("Supplier Items by Country")
if choices == "All":
    supplier_df = suppliers
else:
    supplier_df = suppliers[suppliers['Country'] == supplier_country_choices]
supplier_agg = supplier_df.groupby(['Supplier'])['Item Code'].count().reset_index()
supplier_agg.columns = ['Supplier', 'Item Total']
supplier_agg = supplier_agg.sort_values("Item Total", ascending=False)

# Count of items provided by supplier by country (table)
st.dataframe(supplier_agg)
# Top & bottom 5 suppliers by count by country (graph)
st.write("top & bottom 5 suppliers")
supplier_agg_top5 = supplier_agg.head(5)
supplier_agg_top5_fig = px.bar(supplier_agg_top5, x="Supplier", y="Item Total")
st.caption("Top5")
st.plotly_chart(supplier_agg_top5_fig)
supplier_agg_top5 = supplier_agg.tail(5)
supplier_agg_top5_fig = px.bar(supplier_agg_top5, x="Supplier", y="Item Total")
st.caption("Bottom 5")
st.plotly_chart(supplier_agg_top5_fig)

