#================
# Toronto Public Library Analysis
#================


# Load libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import os, os.path
import pandas as pd
import matplotlib.pyplot as plt

st.title('Toronto Public Library Insights')


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


#Key Issue - Bridging digital divide

#How can TPL measure the reach of access to TPL’s technology services to ensure the technological needs of all residents and communities are met?
#How can the City of Toronto measure the level of access of residents and communities to internet and technology?

# # of computer workstations by branch
# # of computer workstation sessions by branch
# Location of computer learning centres & enhanced learning centres
# Location of Digital Innovation Hubs






#Key issue - Access to Youth Services
#TPL is interested in understanding the level of access, utilization and service availability of youth services across the city. This information will inform service gaps for Library Youth Hubs and youth services at the Library.
#How are youth services distributed across the city? What is the utilization of these services?
# Service Access for Youth

# dropdown will be an area

#Location of Youth Advisory Groups
#Location and operating hours of Youth Hubs 
# of youth programs & attendees by branch
#Location of designated youth spaces





