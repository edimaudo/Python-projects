######################
# Load Libraries
######################
import streamlit as st
import pandas as pd
import plotly.express as px
import os, os.path
import datetime
import re, string
import numpy as np

######################
# Title
######################
st.set_page_config(
    page_title="Vitamin C Products Review",
)
st.set_option('deprecation.showPyplotGlobalUse', False)

######################
# Load data
######################
path = os.path.dirname(__file__)
@st.cache(allow_output_mutation=True)
def load_data():
    data = pd.read_csv(DATA_URL)
    return data
DATA_URL = path + "data.csv"
df = load_data()


######################
# Main Page
######################
st.title("Vitamin C Amazon Product reviews")
######################
# Sidebar 
######################
year_list = df['Year'].unique()
year_list  = year_list.astype('int')
year_list.sort()

month_list = df['Month'].unique()
month_list  = month_list.astype('str')
month_list = pd.DataFrame(month_list,columns = ['Month'])

month_dict = {'January':1,'February':2,'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 
'August':8, 'September':9, 'October':10, 'November':11, 'December':12}
month_list = month_list.sort_values('Month', key = lambda x : x.apply (lambda x : month_dict[x]))
month_list = month_list['Month'].values.tolist()

rating_list = df['Rating'].unique()
rating_list  = rating_list.astype('int')
rating_list.sort()

country_list = df['Country'].unique()
country_list  = country_list.astype('str')
country_list.sort()

country_input = st.sidebar.selectbox("Country",country_list)
year_input = st.sidebar.multiselect("Year",year_list, year_list)
month_input = st.sidebar.multiselect("Month",month_list, month_list)
rating_input = st.sidebar.multiselect("Rating",rating_list, rating_list)

######################
# Output
######################
# Summary
st.header("Summary")
with st.expander(""):
    # Avg ratings
    st.metric("Avg. Rating", "{:.2f}".format(df["Rating"].mean()))
    # of countries
    st.metric("# of countries",  len(df['Country'].unique()))

# Visualization
st.header("Visualization")
df_info = df[(df.Country == country_input) 
    & (df.Year.isin(year_input)) 
    & (df.Month.isin(month_input)) 
    & (df.Rating.isin(rating_input))]

#Ratings by year
st.markdown("Yearly Ratings Trend")
df_year = df_info[['Year','Rating']]
df_year_agg = df_year.groupby(['Year']).agg(Total = ('Rating', 'mean')).reset_index()
df_year_agg.columns = ['Year','Rating']
df_year_agg.sort_values("Year", ascending=True)
fig = px.line(df_year_agg, x="Year", y="Rating")
st.plotly_chart(fig)

# Text Analysis
st.header("Text Analysis")
nlp_analysis = df[(df.Country == country_input) 
    & (df.Year.isin(year_input)) 
    & (df.Month.isin(month_input)) 
    & (df.Rating.isin(rating_input))]
clicked = st.button("Run Text Analysis")
if nlp_analysis.empty:
    st.write("No data Available! Please try another combination from the dropdowns")
else:
    n = 30
    if nlp_analysis.shape[0] < 30:
        n = nlp_analysis.shape[0]
    #st.dataframe(nlp_analysis['Body'][:n])
if clicked and not nlp_analysis.empty:
    # Convert review into one large paragraph
    text = '. '.join(nlp_analysis['Body'][:n])
    # Text cleanup
    text = text.lower() # Lower case
    text = text.strip() # rid of leading/trailing whitespace with the following
    text = re.compile('<.*?>').sub('', text) # Remove HTML tags/markups:
    text = re.compile('[%s]' % re.escape(string.punctuation)).sub(' ', text) # Replace punctuation with space
    text = re.sub('\s+', ' ', text) # Remove extra space and tabs
    # Remove stop words
    stop_words = ["a", "an", "the", "this", "that", "is", "it", "to", "and"]
    filtered_sentence = []
    words = text.split(" ")
    for w in words:
        if w not in stop_words:
            filtered_sentence.append(w)
    text = " ".join(filtered_sentence)
    # ExpertAI Credentials
    os.environ["EAI_USERNAME"] = 'edimaudo@gmail.com'
    os.environ["EAI_PASSWORD"] = '3XpeRtA!L0g1n'
    from expertai.nlapi.cloud.client import ExpertAiClient
    client = ExpertAiClient()
    language = 'en'
    try:
        # Document analysis 
        output_keyword = client.specific_resource_analysis(body={"document": {"text": text}}, 
        params={'language': language, 'resource': 'relevants'})
        output_named_entity = client.specific_resource_analysis(body={"document": {"text": text}},
        params={'language': language, 'resource': 'entities'})
        output_sentiment = client.specific_resource_analysis(body={"document": {"text": text}}, 
        params={'language': language, 'resource': 'sentiment'})
        output_emotional_trait = client.classification(body={"document": {"text": text}}, 
        params={'taxonomy': 'emotional-traits', 'language': language})
        output_behavior = client.classification(body={"document": {"text": text}}, 
        params={'taxonomy': 'behavioral-traits', 'language': language})
        st.subheader("Document Analysis")
        st.markdown("**Keyphrase extraction**")
        for lemma in output_keyword.main_lemmas:
            st.write("- " + lemma.value)
        st.write(" ")
        st.markdown("**Named Entity recognition**")
        for entity in output_named_entity.entities:
            st.write(f' - {entity.lemma:{50}} {entity.type_:{10}}')
        st.write(" ")
        st.markdown("**Sentiment analysis**")
        if (output_sentiment.sentiment.overall > 0):
            st.write("Positive Sentiment: " + str(output_sentiment.sentiment.overall))
        st.write("Negative sentiment: " + str(output_sentiment.sentiment.overall))
        # Document classification
        st.subheader("Document Classification")
        st.markdown("**Emotional Traits**")
        for category in output_emotional_trait.categories:
            st.write("- ", category.hierarchy[0], " -> ", category.hierarchy[1])
        st.write(" ")
        st.markdown("**Behavorial traits**")   
        for category in output_behavior.categories:
            st.write("- ", category.hierarchy[0], ": ", category.hierarchy[1]," -> ", category.hierarchy[2])
    except:
        st.write(" ")
        st.error("Issue retrieving data from the API")

