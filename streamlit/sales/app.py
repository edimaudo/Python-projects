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


sales_file = "Sales.xlsx"
sales = load_data(sales_file)
supplier_file = "Suppliers.xlsx"
suppliers = load_data(supplier_file)

st.title('Sales and Supplier Insights')

#------------------
# Sales Analysis
#------------------
st.header("Sales Analysis")
st.write("Provides an overview of sales performance in every country")
#(Country and ItemCode selection)
item_info = sales['Item Code'].unique()
#item_info = item_info.astype('int64')
item_info = item_info.tolist()
item_info.sort()
sales_item_choices = st.selectbox("Items ", item_info, index=461)

country_info = sales['Country'].unique()
country_info = country_info.astype('str')
country_info = country_info.tolist()
country_info.sort()
sales_country_choices = st.selectbox("Countries ", country_info,index=9)
sales_df = sales[(sales['Country'] == sales_country_choices) & (sales['Item Code'] == sales_item_choices)]
# Sales trend
st.subheader("Sales Trend")
sales_agg = sales_df.groupby(['Date'])['Quantity'].sum().reset_index()
sales_agg.columns = ['Date', 'Total Quantity']
sales_agg = sales_agg.sort_values("Date", ascending=False)
fig = px.line(sales_agg, x="Date", y="Total Quantity")
st.plotly_chart(fig)





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
if supplier_country_choices == "All":
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
st.caption("Top 5")
st.plotly_chart(supplier_agg_top5_fig)
supplier_agg_top5 = supplier_agg.tail(5)
supplier_agg_top5_fig = px.bar(supplier_agg_top5, x="Supplier", y="Item Total")
st.caption("Bottom 5")
st.plotly_chart(supplier_agg_top5_fig)

