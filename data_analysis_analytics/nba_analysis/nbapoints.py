"""
Goal:predict how many points NBA players scored in the 2013-2014 season
Techinque: Use K-nearest neighbor
The k-nearest neighbors algorithm is based 
around the simple idea of predicting unknown 
values by matching them with the most similar known values.
"""

import pandas
import sys 
import numpy as np 
from scipy.spatial import distance
import random
from numpy.random import permutation
from sklearn.neighbors import KNeighborsRegressor

try:

	# read data
	nba = pandas.read_csv("nba_2013.csv")
	#check columns 
	#print(nba.columns.tolist())

	# Choose only the numeric columns (we'll use these to compute euclidean distance)
	distance_columns = ['age', 'g', 'gs', 'mp', 'fg', 'fga', 'fg.', 'x3p', 'x3pa', 'x3p.', 'x2p', 'x2pa', 'x2p.', 'efg.', 'ft', 'fta', 'ft.', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf', 'pts']

	def euclidean_distance(row):
	    """
	    A simple euclidean distance function
	    """
	    inner_value = 0
	    for k in distance_columns:
	        inner_value += (row[k] - selected_player[k]) ** 2
	    return math.sqrt(inner_value)

	# # Select only the numeric columns from the NBA dataset
	# nba_numeric = nba[distance_columns]

	# # Normalize all of the numeric columns
	# nba_normalized = (nba_numeric - nba_numeric.mean()) / nba_numeric.std()
	# # Fill in NA values in nba_normalized
	# nba_normalized.fillna(0, inplace=True)

	# # Find the normalized vector for lebron james.
	# lebron_normalized = nba_normalized[nba["player"] == "LeBron James"]

	# # Find the distance between lebron james and everyone else.
	# euclidean_distances = nba_normalized.apply(lambda row: distance.euclidean(row, lebron_normalized), axis=1)

	# # Create a new dataframe with distances.
	# distance_frame = pandas.DataFrame(data={"dist": euclidean_distances, "idx": euclidean_distances.index})
	# distance_frame.sort("dist", inplace=True)
	# # Find the most similar player to lebron (the lowest distance to lebron is lebron, the second smallest is the most similar non-lebron player)
	# second_smallest = distance_frame.iloc[1]["idx"]
	# most_similar_to_lebron = nba.loc[int(second_smallest)]["player"]

	#generate test and training data
	# Randomly shuffle the index of nba.
	random_indices = permutation(nba.index)
	# Set a cutoff for how many items we want in the test set (in this case 1/3 of the items)
	test_cutoff = math.floor(len(nba)/3)
	# Generate the test set by taking the first 1/3 of the randomly shuffled indices.
	test = nba.loc[random_indices[1:test_cutoff]]
	# Generate the train set with the rest of the data.
	train = nba.loc[random_indices[test_cutoff:]]


	# The columns that we will be making predictions with.
	x_columns = ['age', 'g', 'gs', 'mp', 'fg', 'fga', 'fg.', 'x3p', 'x3pa', 'x3p.', 'x2p', 'x2pa', 'x2p.', 'efg.', 'ft', 'fta', 'ft.', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf']
	# The column that we want to predict.
	y_column = ["pts"]


	# Create the knn model.
	# Look at the five closest neighbors.
	knn = KNeighborsRegressor(n_neighbors=5)
	# Fit the model on the training data.
	knn.fit(train[x_columns], train[y_column])
	# Make point predictions on the test set using the fit model.
	predictions = knn.predict(test[x_columns])

	# Get the actual values for the test set.
	actual = test[y_column]

	# Compute the mean squared error of our predictions.
	mse = (((predictions - actual) ** 2).sum()) / len(predictions)
except:
	e = sys.exc_info()
	print(e)
	sys.exit(1)