import numpy as np
import pandas as pd
import glob
#import matplotlib.pyplot as plt


#path ='/Users/edima/Desktop/citibike/data/' # use your path
#allFiles = glob.glob(path + "/*.csv")
#frame = pd.DataFrame()

df = pd.read_csv('data.csv')
df.head()

#group data

#gender grouping
total = df.gender.count()
groupedGender.size() / total * 100

groupedStart = df.groupby('start station name')
groupedStart['start station name'].count().sort_values(ascending=False)[:5]

groupedEnd = df.groupby('end station name')
groupedEnd['end station name'].count().sort_values(ascending=False)[:5]