from selenium import webdriver
import sys
import csv

path_to_chromedriver = '/Users/Edima/Desktop/contest/chromedriver' #change as needed
driver = webdriver.Chrome(path_to_chromedriver)

path = "/Users/Edima/Desktop/"
BASE_URL = "http://statbel.fgov.be/en/statistics/figures/economy/indicators/prix_prod_con/"
driver.get(BASE_URL)
try:
	data = driver.find_element_by_class_name("statisticTable")
	items = data.find_elements_by_tag_name("tr")
	
	data_info = []
	for item in items:
		data_info.append(item.text)
	
	main_data = data_info[1:]
	main_data_temp = [data.split(" ") for data in main_data]
	print(main_data_temp)
	header = ['Gross indices (2010=100)','I',"II","III","IV","Year"]
	with open(path + 'index.csv', 'a') as csv_file:
		w = csv.writer(csv_file)
		w.writerow(header)
		for data in main_data_temp:
			w.writerow(data)
	driver.quit()
except:
	e = sys.exc_info()
	print(e)
	driver.quit()
	sys.exit(1)