
import urllib2
import pandas as pd
import csv  
from datetime import datetime 
from bs4 import BeautifulSoup
from urllib2 import urlopen


quote_page = 'http://www.bloomberg.com/quote/SPX:IND'
page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser') 
name_box = soup.find('h1', attrs={'class': 'name'})
name = name_box.text.strip() # strip() is used to remove starting and trailing  

price_box = soup.find('div', attrs={'class':'price'})  
price = price_box.text  
print (name + " " + price)
with open('index.csv', 'a') as csv_file:  
    writer = csv.writer(csv_file)
    writer.writerow([name, price, datetime.now()])