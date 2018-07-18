import pandas as pd
import warnings
warnings.filterwarnings('ignore')
df = pd.read_excel("Online_Retail.xlsx")
df.head()
df1 = df

#data exploration

df1.Country.nunique()
df1.Country.unique()

#country count
customer_country=df1[['Country','CustomerID']].drop_duplicates()
customer_country.groupby(['Country'])['CustomerID'].aggregate('count').reset_index().sort_values('CustomerID', ascending=False)

#check for missing data
df1.isnull().sum(axis=0)

#keep non missing data
df1 = df1[pd.notnull(df1['CustomerID'])]

#check qty
df1.Quantity.min()

#remove negative qty
df1 = df1[(df1['Quantity']>0)]
df1.shape
df1.info()

#add column for total price
df1['TotalPrice'] = df1['Quantity'] * df1['UnitPrice']

#get first and last date
df1['InvoiceDate'].min()
df1['InvoiceDate'].max()

import datetime as dt
NOW = dt.datetime(2011,12,10)
df1['InvoiceDate'] = pd.to_datetime(df1['InvoiceDate'])

#rfm segmentation
rfmTable = df1.groupby('CustomerID').agg({'InvoiceDate': lambda x: (NOW - x.max()).days,
                                        'InvoiceNo': lambda x: len(x),  
                                        'TotalPrice': lambda x: x.sum()})

rfmTable['InvoiceDate'] = rfmTable['InvoiceDate'].astype(int)
rfmTable.rename(columns={'InvoiceDate': 'recency', 
                         'InvoiceNo': 'frequency', 
                         'TotalPrice': 'monetary_value'}, inplace=True)
rfmTable.head()

#quantiles
quantiles = rfmTable.quantile(q=[0.25,0.5,0.75])
quantiles = quantiles.to_dict()

#rfm table
segmented_rfm = rfmTable


def RScore(x,p,d):
    if x <= d[p][0.25]:
        return 1
    elif x <= d[p][0.50]:
        return 2
    elif x <= d[p][0.75]: 
        return 3
    else:
        return 4
    
def FMScore(x,p,d):
    if x <= d[p][0.25]:
        return 4
    elif x <= d[p][0.50]:
        return 3
    elif x <= d[p][0.75]: 
        return 2
    else:
        return 1

#create segmented table
segmented_rfm['r_quartile'] = segmented_rfm['recency'].apply(RScore, args=('recency',quantiles,))
segmented_rfm['f_quartile'] = segmented_rfm['frequency'].apply(FMScore, args=('frequency',quantiles,))
segmented_rfm['m_quartile'] = segmented_rfm['monetary_value'].apply(FMScore, args=('monetary_value',quantiles,))
segmented_rfm.head()


#combine rfm
segmented_rfm['RFMScore'] = segmented_rfm.r_quartile.map(str) 
                            + segmented_rfm.f_quartile.map(str) 
                            + segmented_rfm.m_quartile.map(str)
segmented_rfm.head()