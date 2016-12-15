import pandas as pd
import numpy as np
import csv

path = "/Users/edima/desktop/"

df = pd.read_csv(path + 'data.csv')

city_info = df['city_id'].value_counts().index.tolist()
city_count = df['city_id'].value_counts().tolist()

header = ["city_id",'count']
city = zip(city_info,city_count)

with open(path + 'yourfile.csv', 'wb') as f:
    w = csv.writer(f)
    w.writerow(header)
    for data in city:
        w.writerow(data)


