import csv
import pandas as pd
import numpy as np
import sys

"""
The number of women currently serving in the U.S. Congress, according to Sunlight Foundation data 
"""

data = pd.read_csv("legislators.csv")
columns = data.columns.tolist()
#print(columns)
columns = ['in_office', 'gender']
try:
	#data = data.dropna()
	df = pd.DataFrame(data)
	df1 = df[columns]
	
	df2 = df1[(df1['in_office'] == 1) & (df1['gender'] == 'F')]
	print(len(df2))

except:
	e = sys.exc_info()
	print(e)
	sys.exit(1)