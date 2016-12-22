from selenium import webdriver
import sys
import csv
import time

path_to_chromedriver = '/Users/Edima/Desktop/contest/chromedriver' #change as needed
driver = webdriver.Chrome(path_to_chromedriver)

path = "/Users/edima/Desktop/"
BASE_URL = "http://www.dictionary.com/"
driver.get(BASE_URL)
try:
	word_search = ['handy']
	
	search_bar = driver.find_element_by_id("q")
	search_bar.send_keys(word_search[0])

	driver.find_element_by_id("search-submit").click()
	
	driver.current_url
	source = driver.find_element_by_id("source-luna")
	word_info = source.find_element_by_class_name("def-pbk")
	word_data = word_info.find_elements_by_class_name("def-set")
	temp_output = [data.find_element_by_class_name("def-content").text for data in word_data]

	print(temp_output)
	
	temp_output2 = [value[:value.find(":")] for value in temp_output]
	print(temp_output2)
	temp_output3 = [value.split(";") for value in temp_output2]
	print(temp_output3)

	output = [for info in temp_output3 for data in info]


	driver.quit()
except:
	e = sys.exc_info()
	print(e)
	driver.quit()
	sys.exit(1)