#Intel ML Week 1
import pandas as pd

step_data = [3620, 7891, 9761, 3907, 4338, 5373]
step_counts = pd.Series(step_data,name='steps') 
print(step_counts)

#add date range to series
step_counts.index = pd.date_range('20150329',periods=6)
print(step_counts)

#just like a dict
print(step_counts['2015-04-01'])

#or using index position
print(step_counts[3])

#select all of a particular month
print(step_counts['2015-04'])

#print datatype
print(step_counts.dtype)

#convert datatypes
step_counts = step_counts.astype(np.float)
print(step_counts)

#fill invalid data
step_counts[1:3] = np.NaN

#replace with zeros
step_counts = step_counts.fillna(0.)

#combining data
# Cycling distance
cycling_data = [10.7, 0, None, 2.4, 15.3, 10.9, 0, None]
# Create a tuple of data
joined_data = list(zip(step_data,cycling_data))
# The dataframe
activity_df = pd.DataFrame(joined_data) 
print(activity_df)

#add columns and datarange
# Add column names to dataframe
activity_df = pd.DataFrame(joined_data, index=pd.date_range('20150329',periods=6), 
columns=['Walking','Cycling'])
print(activity_df)

#select row by value
print(activity_df.loc['2015-04-01'])

# Select row of data by integer position same as above
print(activity_df.iloc[-3])

# Name of column
print(activity_df['Walking'])
print(activity_df.Walking) #same as above
print(activity_df.iloc[:,0]) #select first column


#reading data
# The location of the data file
filepath = '~/Iris_Data.csv' # Import the data
data = pd.read_csv(filepath)
# Print a few rows
print(data.iloc[:5])

#assign new data
# Create a new column that is a product # of both measurements 
data['sepal_area'] = data.sepal_length*data.sepal_width
# Print a few rows and columns
print(data.iloc[:5, -3:])

#function to replace iris key word
data['abbrev'] = (data.species .apply(lambda x:x.replace('Iris-','')))

#combining two dataframes
small_data = pd.concat([data.iloc[:2],data.iloc[-2:]]) print(small_data.iloc[:,-3:])

#aggregating data
group_sizes = (data
              .groupby('species’)
              .size())
print(group_sizes)

#mean
print(data.mean())

#basic stats
print(data.petal_length.std(), data.petal_length.var(), data.petal_length.sem())

#basic statistical summary
print(data.describe())

#basic data sampling
# Sample 5 rows without replacement
sample = (data
          .sample(n=5,
                  replace=False,
                  random_state=42))
print(sample.iloc[:,-3:])

#visualizations
import matplotlib.pyplot as plt
plt.plot(data.sepal_length,data.sepal_width,ls ='', marker='o')

#scatterplot
plt.plot(data.sepal_length,data.sepal_width,ls ='', marker='o’,label='sepal')
plt.plot(data.petal_length,data.petal_width,ls ='', marker='o’,label='petal')

#histogram
plt.hist(data.sepal_length, bins=25)

#statistical plots using seaborn
import seaborn as sns
sns.jointplot(x='sepal_length’,
              y='sepal_width’,
              data=data, size=4)
              
#pairplot
sns.pairplot(data, hue='species', size=3)


