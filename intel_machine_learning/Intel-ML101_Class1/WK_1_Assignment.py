from __future__ import print_function
import os
data_path = "/Users/edima/Documents/Coding/python_projects/intel_machine_learning/Intel-ML101_Class1/data/"
print (data_path)

import numpy as np
import pandas as pd

filepath = os.sep.join(data_path + 'Iris_Data.csv')
print(filepath)
data = pd.read_csv(data_path + 'Iris_Data.csv')
data.head()

# Number of rows
print(data.shape[0])

# Column names
print(data.columns.tolist())

# Data types
print(data.dtypes)

#question 2
# Examine the species names and note that they all begin with 'Iris-'. 
#Remove this portion of the name so the species name is shorter.
data['species'] = data.species.str.replace('Iris-', '')

#question 3
#The number of each species present. (Hint: check out the series .value_counts method.)
#The mean, median, and quantiles and ranges (max-min) for each petal and sepal measurement.


