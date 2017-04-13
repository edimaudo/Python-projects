"""
Go to https://www.ordnancesurvey.co.uk/business-and-government/partners/finder/
extract companyname, url, contact, email, phone number
"""

import os
import sys
import time
import csv
from selenium import webdriver
from selenium.webdriver.support.ui import Select

def main():

	path = os.path.dirname(os.path.abspath(__file__))
	path_to_chromedriver = path + "/" + 'chromedriver'	
	
	try:
		company_url = []
		data_info = []
		driver = webdriver.Chrome(path_to_chromedriver)
		BASE_URL = "https://www.ordnancesurvey.co.uk/business-and-government/partners/finder/"
		#driver.get(BASE_URL)

		#data = driver.find_element_by_id("mainListings")
		#column = data.find_elements_by_class_name("grid-cols-4")
		
		# for col in column:
		# 	column_comp = col.find_elements_by_class_name("pner")
		# 	url_data = [url.find_element_by_css_selector('a').get_attribute('href') for url in column_comp]
		# 	company_url = url_data

		# print(len(company_url))
		# count = 0
		# company_url_count = len(company_url)

		# while(count < company_url_count):
		# 	url = company_url[count]
		# 	driver.get(url)
		# 	company_data = ["","","","","",""]
		# 	company_name = driver.find_element_by_tag_name("h1")
		# 	company_data[0] = company_name.text

		# 	company_url = driver.find_element_by_class_name("asset-links")
		# 	company_url_ul = company_url.find_element_by_tag_name("ul")
		# 	company_url_li = company_url_ul.find_element_by_tag_name("li")
		# 	company_data[1] = company_url_li.find_element_by_css_selector('a').get_attribute('href')
			
		# 	other_info = driver.find_element_by_class_name("grid-cols-4")
		# 	table = other_info.find_element_by_tag_name("table")
		# 	table_body = table.find_element_by_tag_name("tbody")
		# 	table_data = table_body.find_elements_by_tag_name("tr")	

		# 	all_table_data = [data.text for data in table_data]	
		# 	name_table_data = [item.split() for item in all_table_data]

		# 	for info in name_table_data:
		# 		if info[0]=="Email":
		# 			company_data = info[1]
		# 		elif info[0]=="Contact":
		# 			company_data = info[1]
		# 		elif info[0] == "Phone":
		# 			company_data = info[1]
			
		# 	data_info.append(company_data)
		# 	count+=1

		# print(company_data)
		#driver.quit()

		headers = ["company name", "url", "contact", "email", "phone number"]
		
		#output
		# with open(path + 'index.csv', 'a') as csv_file:
		# 	w = csv.writer(csv_file)
		# 	w.writerow(header)
		# 	for data in data_info:
		# 		w.writerow(data)
	except:
		e = sys.exc_info()
		print(e)
		#driver.quit()
		sys.exit(1)



if __name__ == "__main__":
	main()