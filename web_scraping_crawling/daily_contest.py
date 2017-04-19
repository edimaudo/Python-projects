from selenium import webdriver
from selenium.webdriver.support.ui import Select
import datetime
from datetime import date
import time
import sys

path = os.path.dirname(os.path.abspath(__file__))
path_to_chromedriver = path + "/" + 'chromedriver'	
my_data =  ["Edima", "Udo", "Edima Udo",
'edimaudo@outlook.com',"12 Southgate Avenue","Toronto","M3N 1P2", "Ontario", "6479876976"]
driver = webdriver.Chrome(path_to_chromedriver)

def main():
	#do something
	BASE_URL = "http://steamykitchen.com/43873-apple-ipad-mini-giveaway-4.html"
	try:
		if datetime.date.today() < datetime.date(2017,07,10):
			driver.get(BASE_URL)
			driver.find_element_by_id("skg_first_name").send_keys(my_data[0])
			timer.sleep(1)
			driver.find_element_by_id("skg_last_name").send_keys(my_data[1])
			timer.sleep(1)
			driver.find_element_by_id("skg_email").send_keys(my_data[3])
			timer.sleep(1)
			driver.find_element_by_name("submit_giveaway_entry").click()
			time.sleep(2)
	except:
		e = sys.exc_info()
		print(e)

	BASE_URL = "http://steamykitchen.com/43871-hp-14-inch-notebook-windows-10-amd-e2-7110-quad-core.html"
	try:
		if datetime.date.today() < datetime.date(2017,07,10):
			driver.get(BASE_URL)
			driver.find_element_by_id("skg_first_name").send_keys(my_data[0])
			time.sleep(1)
			driver.find_element_by_id("skg_last_name").send_keys(my_data[1])
			time.sleep(1)
			driver.find_element_by_id("skg_email").send_keys(my_data[3])
			time.sleep(1)
			driver.find_element_by_name("submit_giveaway_entry").click()
	except:
		e = sys.exc_info()
		print(e)

	BASE_URL = "https://fairmont.promo.eprize.com/canada150/"
	try:
		if datetime.date.today() < datetime.date(2017,05,31):
			driver.get(BASE_URL)
			driver.find_element_by_name("first_name").send_keys(my_data[0])
			time.sleep(1)
			driver.find_element_by_name("last_name").send_keys(my_data[1])
			time.sleep(1)
			driver.find_element_by_name("email").send_keys(my_data[3])
			time.sleep(1)
			driver.find_element_by_name("age").click()
			time.sleep(1)
			driver.find_element_by_class_name("submit").click()
	except:
		e = sys.exc_info()
		print(e)


if __name__ == "__main__":
	main()