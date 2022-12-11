import streamlit as st
import pandas as pd
import numpy as np
import os, os.path


######################
# Load data
######################
path = os.path.dirname(__file__)
DATA_URL = path + "/bcl-data.csv"


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
st.title("BC Liquor Store Prices)

######################
# Sidebar 
######################
st.sidebar.title("Loan Applicant Information")
st.sidebar.image("ab.png", width=100)
st.sidebar.write("Please choose parameters that descibe the applicant")

# Input features
loan_amnt =st.sidebar.slider("Select the loan amount: ",min_value=1000, max_value=40000,step=500)
term = st.sidebar.radio("Select Loan term: ", ('36 months', '60 months'))
int_rate = st.sidebar.slider("Select the interest rate: ",min_value=0.05, max_value=1.00,step=0.05)
installment = st.sidebar.slider("Select the installment amount: ",min_value=10, max_value=400,step=50)

######################
# Output
######################

