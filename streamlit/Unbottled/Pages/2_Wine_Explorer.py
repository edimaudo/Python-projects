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

st.header("Wine Explorer")
country_list = df['country'].unique()
country_list  = country_list.astype('str')
country_list.sort()
variety_list = df['variety'].unique()
variety_list  = variety_list.astype('str')
variety_list.sort()

country_choice = st.selectbox("Select a Country",country_list)
variety_choice = st.selectbox("Select a Variety",variety_list)
price_choice = st.slider('Select a Price Range', 0, 2500, 100)
points_choice = st.slider('Select a Points Range', 80, 100, 5)

choice_df = df[(df.country == country_choice) | (df.variety == variety_choice) | (df.price.le(price_choice)) | (df.points.le(points_choice))]
choice_df = choice_df[['country','variety','price','points','description','designation','winery']]
st.dataframe(choice_df)





 

    

    