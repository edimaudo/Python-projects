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

st.header("Data Preview")
with st.expander(" "):
    st.dataframe(df.head(30))

st.header("Data Summary")
with st.expander(""):
    container = st.container()
    metric_column1, metric_column2,metric_column3,metric_column4, metric_column5,metric_column6 = st.columns(6)
    with container:
        metric_column1.metric("# of Countries",str( len(df['country'].unique())))
        metric_column2.metric("# of Varieties",str(len(df['variety'].unique())))
        metric_column3.metric("# of Wineries",str(len(df['winery'].unique())))
        metric_column4.metric("Avg. Point",str((df['points'].mean())))
        metric_column5.metric("Avg. Price",str(df['price'].mean()))

st.header("Data Visualization")
with st.expander(""):
    st.write("Which countries have the most reviewed wine?")
    country_review = df[['country','description']]
    country_review_agg = country_review.groupby('country').agg(Total_reviews = 
                                                                        ('description', 'count')).reset_index()
    country_review_agg.columns = ['Country', 'Reviews']
    country_review_agg = country_review_agg.sort_values("Reviews", ascending=False).reset_index(drop=True)
    country_review_agg = country_review_agg.head(10)
    fig = px.bar(country_review_agg, x="Country", y="Reviews")
    st.plotly_chart(fig)

    
    st.write("Where are the world’s best wines from?")
    country_review = df[['country','points']]
    country_review_agg = country_review.groupby('country').agg(Total_reviews = 
                                                                        ('points', 'mean')).reset_index()
    country_review_agg.columns = ['Country', 'Avg. Points']
    country_review_agg = country_review_agg.sort_values("Avg. Points", ascending=False).reset_index(drop=True)
    country_review_agg = country_review_agg.head(10)
    fig = px.bar(country_review_agg, x="Country", y="Avg. Points")
    st.plotly_chart(fig)
    st.write("Where does the priciest wine come from?")
    country_review = df[['country','price']]
    country_review_agg = country_review.groupby('country').agg(Total_reviews = 
                                                                        ('price', 'mean')).reset_index()
    country_review_agg.columns = ['Country', 'Avg. Price']
    country_review_agg = country_review_agg.sort_values("Avg. Price", ascending=False).reset_index(drop=True)
    country_review_agg = country_review_agg.head(10)
    fig = px.bar(country_review_agg, x="Country", y="Avg. Price")
    st.plotly_chart(fig)
        






