from selenium import webdriver
import sys
import csv

path_to_chromedriver = '/Users/Edima/Desktop/contest/chromedriver'
driver = webdriver.Chrome(path_to_chromedriver)

path = "/Users/edima/Desktop/"
BASE_URL = "http://www2.sas.com/proceedings/sugi30/toc.html"
driver.get(BASE_URL)
try:
	#body = driver.find_element_by_tag_name("body")
	data = driver.find_elements_by_tag_name("p")
	temp_output = []
	for item in data:
		temp_output.append(item.text)

	output = temp_output[9:]

	driver.quit()
except:
	e = sys.exc_info()
	print(e)
	driver.quit()
	sys.exit(1)