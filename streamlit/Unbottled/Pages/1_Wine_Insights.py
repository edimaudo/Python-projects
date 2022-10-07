# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache
def load_data():
    data = pd.read_csv(DATA_URL)
    return data

# Load data
DATA_URL = "winemag-data_first150k.csv"
df = load_data()

st.title('Unbottled')
