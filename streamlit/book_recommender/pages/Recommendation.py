# Load libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import os, os.path
import pandas as pd
import matplotlib.pyplot as plt

#scikit-surprise
st.title('Book Recommender')

from surprise import Reader, Dataset, SVD
from surprise.model_selection.validation import cross_validate
reader = Reader()
data = Dataset.load_from_df(df[['Cust_Id', 'Movie_Id', 'Rating']], reader)
svd = SVD()

# Run 5-fold cross-validation and print results
cross_validate(svd, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)


trainset = data.build_full_trainset()
svd.fit(trainset)

titles = titles.sort_values(by=['Estimate_Score'], ascending=False)
titles.head(10)