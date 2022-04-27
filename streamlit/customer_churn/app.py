#================
# Telco. Customer Insights
#================

# Load libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import os, os.path

st.title('Telco. Customer Insights')

@st.cache
def load_data():
	data = pd.read_csv(DATA_URL)
	return data

# Load data
DATA_URL = "customer_churn.csv"
df = load_data()

#====================
# Raw data
#====================


#====================
# Data
#====================
# Average Total charge

# Average Tenure

#====================
# Data visualization
#====================

# Payment Method

#Contract

# Internet Service

# Phone Service

# Paperless

# Gender

# Tenure

#====================
# Churn prediction using ML
#====================

# ML Models

# Fairness Information