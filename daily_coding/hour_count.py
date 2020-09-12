

#Calculate the unique invoice number based on time difference in seconds between records.
#If a record/row has greater than 20sec difference between the current row(indexed) 
#and the previous row then number(unique number) needs to be assigned if not then assign unique number for the current row only
#The rows should be partitioned by Ipkey, date, hour, minute in order to get the correct order of the records(sequential order)
#load data


import pandas as pd
import numpy as np

df = pd.read_csv('FinalData.csv')
df.sort_values(by=['IpAddress','date_time'], inplace=False) #sort df

df_temp = df.head(5)
print(df_temp.iloc[1]['date_time'])

data_info = []

value = 0
for i, row in df_temp.iterrows():
	if i == 0:
		value = value + 1
		data_info.append([row['IpAddress'],row['date_time'],row['data'],value])
	else:
		t1 = pd.to_datetime(df_temp.iloc[i-1]['date_time'])
		t2 = pd.to_datetime(df_temp.iloc[i]['date_time'])
		if pd.Timedelta(t2 - t1).seconds >= 20:
			value = value + 1
			data_info.append([row['IpAddress'],row['date_time'],row['data'],value])

df_final = pd.DataFrame(data_info)
df_final.columns = ['IpAddress','date_time','data','value']
