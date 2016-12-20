# visualizing classification usiing iris data set and scikit learn

import sys
import numpy as np
from sklearn import tree
from sklearn.datasets import load_iris
import os
from IPython.display import Image
import pydot
from sklearn.externals.six import StringIO
iris = load_iris()

#features
#print(iris.feature_names)
#print(iris.target_names)
#print(iris.data[0])

#split data -- training and test data

# training data
test_idx = [0,50,100]
# remove test data
train_target = np.delete(iris.target, test_idx) 
train_data = np.delete(iris.data,test_idx,axis=0)

#test data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

# perform training 
clf = tree.DecisionTreeClassifier()
clf.fit(train_data,train_target)

try:
	print(test_target) #shows all three flower types
	print(clf.predict(test_data)) # predict flower
	dot_data = StringIO()
	# make sure graphiz and pydot or pydotplus is installed
	tree.export_graphviz(clf, out_file=dot_data, 
                         feature_names=iris.feature_names,  
                         class_names=iris.target_names,  
                         filled=True, rounded=True,  
                         impurity=False)
	graph = pydot.graph_from_dot_data(dot_data.getvalue())
	#graph.write_pdf("iris.pdf") 

	#classify based on output
	print(test_data[1],test_target[1])
	print(iris.feature_names,iris.target_names)
	print(test_data[0],test_target[0])
	print(iris.feature_names,iris.target_names)
except:
	e = sys.exc_info()
	print(e)
	sys.exit(1)