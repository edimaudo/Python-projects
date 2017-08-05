"""
Warm Up: Predict Blood Donations
Goal: We want to predict whether or not a donor will give blood the next time the vehicle comes to campus
"""

import csv
import pandas as pd
import numpy as np
import sys
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression

#data import
path = "https://archive.ics.uci.edu/ml/machine-learning-databases/blood-transfusion/transfusion.data"
data = pd.read_csv(path)

#get column info
columns = data.columns.tolist()
#print(columns)

column_data = ['Recency (months)', 'Frequency (times)', 'Monetary (c.c. blood)', 'Time (months)', 'whether he/she donated blood in March 2007']

#use all columns for first prediction step
# Store the variable we'll be predicting on.
target = column_data[-1]

#split data into test and training
# Generate the training set.  Set random_state to be able to replicate results.
train = data.sample(frac=0.8, random_state=1)
# Select anything not in the training set and put it in the testing set.
test = data.loc[~data.index.isin(train.index)]
# Print the shapes of both sets.
#print("Shape of data set")
#print(train.shape)
#print(test.shape)

#model using linear regression
# Initialize the model class.
model = LogisticRegression()
# # Fit the model to the training data.
model.fit(data[columns], train[target])
# #predict error
# # Generate our predictions for the test set.
predictions = model.predict(test[columns])
#print(predictions)

#print(model.predict_proba(data))
























