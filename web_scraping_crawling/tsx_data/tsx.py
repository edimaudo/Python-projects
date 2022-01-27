import requests
import sys
from datetime import date
import datetime
import time
import pandas as pd
from bs4 import BeautifulSoup

URL = 'https://eoddata.com/stocklist/TSX/'
LETTERS = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
tsx_stock_data = []
tsx_all_data = []
print("Starting stock list gathering.....")
for letter in LETTERS:
	try:
		tempURL = URL + letter + ".htm"
		page = requests.get(tempURL)
		soup = BeautifulSoup(page.content, "html.parser")
		results = soup.find(id="ctl00_cph1_divSymbols")
		stock_elements = results.find_all("tr") #, class_="ro")
		for stock_element in stock_elements:
			individual_tsx_stock_data = stock_element.find_all("td")
			tsx_stock_data.append(individual_tsx_stock_data)
		df = pd.DataFrame(tsx_stock_data)
		df.to_csv('stock_data.csv', index=False, header=False)
	except:
		e = sys.exc_info()
		print(e)
		sys.exit(1)
print('Done!')
	



