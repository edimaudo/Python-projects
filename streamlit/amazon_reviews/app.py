import streamlit as st
import pandas as pd
import plotly.express as px
import os, os.path
import datetime
import re, string


st.set_page_config( 
    page_title="Amazon reviews for Vitamin C Product",
)

# Load data
@st.cache(allow_output_mutation=True)
def load_data():
    data = pd.read_csv(DATA_URL)
    return data

DATA_URL = "Amazon_Reviews_Vitamin_C.csv"
df = load_data()



# Overview


# Summary


# Visualization


# Text Analysis