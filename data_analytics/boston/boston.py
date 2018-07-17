import numpy as np
import pandas as pd
from numpy.linalg import inv
from sklearn.datasets import load_boston
from statsmodels.regression.linear_model import OLS


# load the boston data set
boston = load_boston()

# obtain the feature matrix as a numpy array
X = boston.data

# obtain the target variable as a numpy array
y = boston.target

#check features
feature_names = boston.feature_names
print(feature_names)