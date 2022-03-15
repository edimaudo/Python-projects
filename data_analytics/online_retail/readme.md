## Objective
The goal of this analysis is to determine quantitatively which customers are the best ones by examining how recently a customer has purchased (recency), how often they purchase (frequency), and how much the customer spends (monetary). R_F_M analysis is based on the marketing axiom that "80% of your business comes from 20% of your customers." 

## Data
The The analysis will use the [Online retail dataset](http://archive.ics.uci.edu/ml/datasets/Online+Retail).  This is a dataset which consist of items description, invoice numbers, transactions, quantity etc.

## Overview
The need of customer segmentation:
The differences in customers' behaviour, demographics, geographies, etc. help in classifying them in groups. Learning about different groups in the customer can help with following:

Target Marketing
Client understanding
Optimal product placement
Searching for new customers
Revenue growth

Recency-Frequency-Monetary (RFM) model to determine customer value:
The RFM model is quite useful model in retail customer segmentation where only the data of customer transaction is available. RFM stands for the three dimensions:

Recency – How recently did the customer purchase?
Frequency – How often do they purchase?
Monetary Value – How much do they spend?
A combination of these three attributes can be defined to assign a quantitative value to customers. e.g. A customer who recently bought high value products and transacts regularly is a high value customer.

## Approach
- Data Cleaning: Quantity was updated since there were some negative quantity values
- RFM Analysis: Each customer was ranked based on the RFM algorithm.  That is it used three categories, how recent was their last purchase, how often do they transact with us, and how much have the spent on our products. By ranking each of these categories we can group customers into 10 different segements that we can target with a different marketing and sales strategy.  The business questions such as who is most loyal, best customers are answered in the jupyter notebook.
