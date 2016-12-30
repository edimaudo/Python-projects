import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from sklearn.tree import DecisionTreeRegressor

bikes = pd.read_csv("data.csv")
#print(bikes.head())

plt.figure(figsize=(8,6))
plt.plot(bikes['gender'],bikes['bikeid'],'o')
plt.xlabel('gender')
plt.ylabel('bike id')
plt.show()
