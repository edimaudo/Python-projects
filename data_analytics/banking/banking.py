import pandas as pd
import numpy as np
from sklearn import preprocessing
#import matplotlib.pyplot as plt 
#plt.rc("font", size=14)
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
#import seaborn as sns
#sns.set(style="white")
#sns.set(style="whitegrid", color_codes=True)

#load data
data = pd.read_csv('banking.csv', header=0)
data = data.dropna()
print(data.shape)
print(list(data.columns))

#check for missing variables
data.isnull().sum()

#data preprocessing
#create dummy variables
data2 = pd.get_dummies(data, columns =['job', 'marital', 'default', 'housing', 'loan', 'poutcome'])

#drop unknown variables
data2.drop(data2.columns[[12, 16, 18, 21, 24]], axis=1, inplace=True)
data2.columns

#split data into train and test
X = data2.iloc[:,1:]
y = data2.iloc[:,0]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

#logistic regression model
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train, y_train)

#create confusion matrix
y_pred = classifier.predict(X_test)
from sklearn.metrics import confusion_matrix
confusion_matrix = confusion_matrix(y_test, y_pred)
print(confusion_matrix)

#get accuracy
print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(classifier.score(X_test, y_test)))