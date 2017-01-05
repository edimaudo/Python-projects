"""
scrape all email adresses of the website below (and place them in column 1), t
he name of the company (in column 2), the phone numbers 
if any (in column 3) and the name of the contact person if any (in column 4):
"""
from selenium import webdriver
import sys

path_to_chromedriver = '/Users/Edima/Desktop/contest/chromedriver'
driver = webdriver.Chrome(path_to_chromedriver)
BASE_URL = "https://www.wbg-schweiz.ch/information/wohnbaugenossenschaften_schweiz/mitglieder/genossenschaften"
driver.get(BASE_URL)
try:
	house = driver.find_element_by_class_name("accordion")
	house_data = house.find_elements_by_tag_name("h3")
	house_info = [house_name.text for house_name in house_data]

	path = "/Users/edima/Desktop/"
	# open a csv file with append, so old data will not be erased
		writer = csv.writer(csv_file)
		for house in house_info:
			writer.writerow(house)	
	driver.quit()
except:
	e = sys.exc_info()
	print(e)
	driver.quit()
	sys.exit(1)