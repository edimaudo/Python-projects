# Load libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import os, os.path
import pandas as pd
import matplotlib.pyplot as plt

st.title('Toronto Public Library Insights')

st.header('Access to Youth Services')

@st.cache
def load_data(DATA_URL):
    data = pd.read_csv(DATA_URL)
    return data

# Load data
DATA_URL = "Youth_Advisory_Groups_Locations.csv"
youth_advisory_group_location = load_data(DATA_URL)
DATA_URL =  "Youth_Hubs_Locations.csv"
youth_hub_locations = load_data(DATA_URL)



st.write("TPL is interested in understanding the level of access, utilization and service availability of youth services across the city. This information will inform service gaps for Library Youth Hubs and youth services at the Library." + 
"How are youth services distributed across the city? What is the utilization of these services?")

# Data Munging
# Service Access for Youth

# dropdown will be an area

#Location of Youth Advisory Groups
#Location and operating hours of Youth Hubs 
# of youth programs & attendees by branch
#Location of designated youth spaces


