import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.decomposition import PCA
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
import sys

data = pd.read_csv("predict_score.csv")
try:
	#print(data.columns)
	columns = data.columns.tolist()
	# Filter the columns to remove ones we don't want.
	columns = [c for c in columns if c not in ["Categorical_Attribute_1","Categorical_Attribute_2","Categorical_Attribute_3","Categorical_Attribute_4","Categorical_Attribute_5","Numerical_Attribute_1","Score"]]
	# Store the variable we'll be predicting on.
	target = "Score"

	#split data into test and training
	# Generate the training set.  Set random_state to be able to replicate results.
	train = data.sample(frac=0.8, random_state=1)
	# Select anything not in the training set and put it in the testing set.
	test = data.loc[~data.index.isin(train.index)]
	# Print the shapes of both sets.
	print(train.shape)
	print(test.shape)

	#model using linear regression
	# Initialize the model class.
	model = LinearRegression()
	# Fit the model to the training data.
	model.fit(train[columns], train[target])

	#predict error
	# Generate our predictions for the test set.
	predictions = model.predict(test[columns])

	# Compute error between our test predictions and the actual values.
	mean_squared_error(predictions, test[target])

	#model using random forest
	# Initialize the model with some parameters.
	model = RandomForestRegressor(n_estimators=100, min_samples_leaf=10, random_state=1)
	# Fit the model to the data.
	model.fit(train[columns], train[target])
	# Make predictions.
	predictions = model.predict(test[columns])
	# Compute the error.
	mean_squared_error(predictions, test[target])

except:
	e = sys.exc_info()
	print(e)
	sys.exit(1)
