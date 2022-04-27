#================
# Customer Churn
#================

# Load libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import os, os.path

st.title('Customer Insights')

@st.cache
def load_data():
	data = pd.read_excel(DATA_URL)
	return data

# Load data
DATA_URL = "otf.xlsx"
df = load_data()
df_backup = df
INPUT_TEXT = "test.txt"


#====================
# Side bar
#====================

#====================
# Raw data
#====================

# Average Total charge

# Average Tenure

#====================
# Data visualization
#====================

# Payment Method

#Contract

# Internet Service

# Gender

#====================
# Machine learning
#====================

# ML Models

# Fairness Information