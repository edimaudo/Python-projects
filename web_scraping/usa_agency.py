"""
 scrape all the information 
(Website,Main Address,E-mail,Phone Number,Government branch)
from the website https://www.usa.gov/federal-agencies/a 
"""

from selenium import webdriver
import sys
import csv

path_to_chromedriver = '/Users/Edima/Desktop/contest/chromedriver'
driver = webdriver.Chrome(path_to_chromedriver)
BASE_URL = "https://www.usa.gov/federal-agencies/a"
driver.get(BASE_URL)
try:
	agency_data = []
	a_agency = driver.find_element_by_class_name("one_column_bullet")
	items = a_agency.find_elements_by_tag_name("li")
	agency_urls = [item.find_element_by_css_selector('a').get_attribute('href') for item in items]
	
	for agency_url in agency_urls:
		BASE_URL = agency_url
		driver.get(BASE_URL)
		agency_PlaceHolder = ["","","","",""]
		headers, ptags =driver.find_elements_by_tag_name("header"), driver.find_elements_by_tag_name("p")
		agency_PlaceHolder[0] = BASE_URL
		for header,ptag in zip(headers,ptags):
			if header.text == "Main Address:":
				agency_PlaceHolder[1] = ptag.text
			if header.text == "E-mail:":
				agency_PlaceHolder[2] = ptag.text
			if header.text == "Phone Number:":
				agency_PlaceHolder[3] = ptag.text
			if header.text == "Government branch:":
				agency_PlaceHolder[4] = ptag.text		
		agency_data.append(agency_PlaceHolder)
	
	#print(agency_data)	
	
	path = "/Users/edima/Documents/Coding/python_projects/web_scraping/web_scraping/"
	# open a csv file with append, so old data will not be erased
	with open(path + 'index.csv', 'a') as csv_file:  
		writer = csv.writer(csv_file)
		for agency in agency_data:
			writer.writerow(agency)	

	driver.quit()
except:
	e = sys.exc_info()
	print(e)
	driver.quit()
	sys.exit(1)


