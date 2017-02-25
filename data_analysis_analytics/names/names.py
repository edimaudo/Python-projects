import numpy as np
import matplotlib.pyplot as pp
import pandas as pd
import seaborn
import zipfile


##zipfile.ZipFile('names.zip').extractall('.')

names2015 = pd.read_csv('yob2015.txt', names = ['Name', 'Sex', 'Babies'])

#print(names2015.head())

all_years = []

for year in range(1880, 2015+1):
    all_years.append(pd.read_csv('yob{}.txt'.format(year),
                                 names = ['Name', 'Sex', 'Babies']))
    all_years[-1]['Year'] = year

group_name = all_names.groupby(['Sex', 'Year'])

#create pivot table
pd.pivot_table(all_names, 'Babies', 'Name', 'Year')

pd.pivot_table(all_names, 'Babies', ['Name', 'Sex'], 'Year')

#visualize data
all_names_index = all_names.set_index(['Sex','Name','Year']).sort_index()

def name_plot(sex, name):
    data = all_names_index.loc[sex, name]

    pp.plot(data.index, data.values)