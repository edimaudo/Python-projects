# Load libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import os, os.path
import pandas as pd
import matplotlib.pyplot as plt

st.title('Program insights')


@st.cache
def load_data(DATA_URL):
    data = pd.read_csv(DATA_URL)
    return data

# Load data
DATA_URL = "Annual_Visits.csv"
annual_visits = load_data(DATA_URL)
DATA_URL = "Computer_Learning_Centres.csv"
computer_learning_centres = load_data(DATA_URL)
DATA_URL = "Digital_Innovation_Hubs.csv"
digital_innovation_hub = load_data(DATA_URL)
DATA_URL = "Workstation_Users.csv"
workstation_users = load_data(DATA_URL)
DATA_URL = "Youth_Advisory_Groups_Locations.csv"
youth_advisory_group_location = load_data(DATA_URL)
DATA_URL = "Youth_Hubs_Locations.csv"
youth_hub_locations = load_data(DATA_URL)