import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix

#Reading Data
path = 'https://archive.ics.uci.edu/ml/machine-learning-databases/tae/tae.data'
data = pd.read_csv(path)
data.columns = ['Native Speaker', 'Course Instructor', 'Course', 'Semester', 'Class Size', 'Class Attribute']

#Creating Training and Test sets
train = data.sample(frac = 0.8, random_state = 102)
test = data.drop(train.index)

#Running Random forest Algorithm
rf = RandomForestClassifier(n_estimators = 1000, n_jobs = -1)
rf.fit(train.ix[:,0:5], train.ix[:,5])
pred = rf.predict(test.ix[:,0:5])
print(pred)
#Checking the Result
print(confusion_matrix(pred, test.ix[:,5]))