

#Calculate the unique invoice number based on time difference in seconds between records.
#If a record/row has greater than 20sec difference between the current row(indexed) 
#and the previous row then number(unique number) needs to be assigned if not then assign unique number for the current row only
#The rows should be partitioned by Ipkey, date, hour, minute in order to get the correct order of the records(sequential order)
#load data


import pandas as pd
import numpy as np

df = pd.read_csv('hrdata.csv')

order_information = []

index = 0
for i, row in df.iterrows():
	if i == 0:
		#do something
	else:
		
