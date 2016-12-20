# simple classification using scikit decision tree
import sys
from sklearn import tree

#original 
"""
first feature input is size in grams
0 --> apple
1 --> orange

features = [[140,"smooth"],[130,"smooth"],[150,"bumpy"],[170,"bumpy"]]
labels = [apple, apple, orange, orange]
"""
features = [[140,1],[130,1],[150,0],[170,0]] #training data
labels = [0,0,1,1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)
try:
	print (clf.predict([[160,0]]))
except:
	e = sys.exc_info()
	print(e)
	sys.exit(1)

