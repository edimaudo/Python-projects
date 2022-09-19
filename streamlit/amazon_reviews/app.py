import streamlit as st
import pandas as pd
import plotly.express as px
import os, os.path
import datetime
import re, string


st.set_page_config( 
    page_title="Amazon reviews for Vitamin C Products",
)

# Load data
@st.cache(allow_output_mutation=True)
def load_data():
    #used to fix utf-8 error (https://stackoverflow.com/questions/46000191/utf-8-codec-cant-decode-byte-0x92-in-position-18-invalid-start-byte)
    data = pd.read_csv(DATA_URL,encoding='cp1252') 
    return data

DATA_URL = "data.csv"
df = load_data()



# Overview


# Summary


# Visualization


# Text Analysis