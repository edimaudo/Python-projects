import os
import sys
import time
from selenium import webdriver
import pandas as pd
import numpy as np
from selenium.webdriver.support.ui import Select

"""
Goes to this URL: https://data.usac.org/publicreports/FRN/Status/FundYear
Selects a State perform for 10 states
Select All Data Points
Clicks "Build Data File" to download an .XLS file
csv files should be combined

"""
US_STATES = ["AK","AL"]
path_to_chromedriver = '/Users/Edima/Desktop/chromedriver' #change as needed
driver = webdriver.Chrome(path_to_chromedriver)
BASE_URL = "https://data.usac.org/publicreports/FRN/Status/FundYear"
driver.get(BASE_URL)
time.sleep(1)
try:
	for state in US_STATES:
		mySelect = Select(driver.find_element_by_id("SelectedStateId"))
		mySelect.select_by_visible_text(state)
		driver.find_element_by_name("hasDataPoint").click()
		driver.find_element_by_name("CreateReport").click()
		time.sleep(2)

	fileinfo = os.listdir("/Users/Edima/Downloads")
	filenames = [value for value in fileinfo if value[-3:] == "csv"]
	results = []
	for filename in filenames:
	    results.append(pd.read_csv("/Users/Edima/Downloads/" + filename))

	combined = pd.concat(results, ignore_index=True)
	combined.to_excel('result.xlsx', index=False)
	driver.quit()
except:
	e = sys.exc_info()
	print(e)
	driver.quit()
	sys.exit(1)

