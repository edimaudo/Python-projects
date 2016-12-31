"""
goal: explore cluster US Senators in the 114 Congress
technique: k-means clustering
In k-means clustering, we divide data up into a fixed number of clusters while trying to ensure that the items in each cluster are as similar as possible.
"""

import sys
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

try:

	# Read in the csv file
	votes = pd.read_csv("114_congress.csv")
	# As you can see, there are 100 senators, and they voted on 15 bills (we subtract 3 because the first 3 columns aren't bills).
	#print(votes.shape)

	# We have more "Yes" votes than "No" votes overall
	#print(pd.value_counts(votes.iloc[:,3:].values.ravel()))
	
	# Create a kmeans model on our data, using 2 clusters.  random_state helps ensure that the algorithm returns the same results each time.
	kmeans_model = KMeans(n_clusters=2, random_state=1).fit(votes.iloc[:, 3:]) # test with different clusters

	# These are our fitted labels for clusters -- the first cluster has label 0, and the second has label 1.
	labels = kmeans_model.labels_

	# The clustering looks pretty good!
	# It's separated everyone into parties just based on voting history
	#print(pd.crosstab(labels, votes["party"]))

	# Let's call these types of voters "oddballs" (why not?)
	# There aren't any republican oddballs
	democratic_oddballs = votes[(labels == 1) & (votes["party"] == "D")]

	# It looks like Reid has abstained a lot, which changed his cluster.
	# Manchin seems like a genuine oddball voter.
	#print(democratic_oddballs["name"])

	pca_2 = PCA(2)

	# Turn the vote data into two columns with PCA
	plot_columns = pca_2.fit_transform(votes.iloc[:,3:18])

	# Plot senators based on the two dimensions, and shade by cluster label
	# You can see the plot by clicking "plots" to the bottom right
	fig = plt.figure()
	fig.suptitle('Congress Cluster', fontsize=20)
	plt.scatter(x=plot_columns[:,0], y=plot_columns[:,1], c=labels)

	plt.show()

except:
	e = sys.exc_info()
	print(e)
	sys.exit(1)