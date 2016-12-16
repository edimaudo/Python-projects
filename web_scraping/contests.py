
from selenium import webdriver
import time
import sys


path_to_chromedriver = '/Users/Edima/Desktop/contest/chromedriver' #change as needed
my_data =  ["Edima", "Udo", "Edima Udo",
'edimaudo@outlook.com',"12 Southgate Avenue","Toronto","M3N 1P2", "Ontario", "5555555555"]
driver = webdriver.Chrome(path_to_chromedriver)

#collateral beauty contest 1
BASE_URL = "https://concours.quebecor.com/collateral-beauty-contest/index.php"
driver.get(BASE_URL)
try:
	email_address = driver.find_element_by_name("f_11015")
	first_name = driver.find_element_by_name("f_11016")
	last_name = driver.find_element_by_name("f_11017")
	address = driver.find_element_by_name("f_11173")
	city = driver.find_element_by_name("f_11174")
	province = driver.find_element_by_name("f_11175")
	postal_code = driver.find_element_by_name("f_11018")
	phone_number = driver.find_element_by_name("f_11019")

	#write to screen
	email_address.send_keys(my_data[3])
	first_name.send_keys(my_data[0])
	last_name.send_keys(my_data[1])
	address.send_keys(my_data[4])
	city.send_keys(my_data[5])
	province.send_keys(my_data[-2])
	postal_code.send_keys(my_data[-3])
	phone_number.send_keys(my_data[-1])

	driver.find_element_by_name("f_11020").click()# gender
	driver.find_element_by_xpath("//select[@name='f_11021']/option[text()='1989']").click()#f_11021 # year
	driver.find_element_by_name("politique_confidentialite").click() # check box
	driver.find_element_by_name("submit").click()# submit
	time.sleep(10)

except:
	e = sys.exc_info()
	print(e)
	sys.exit(1)

#aria-expanded='false'

#collateral beauty contest 2
BASE_URL = "http://www.tribute.ca/contests/collateral-beauty-smart-phone-contest-c3814/?referrer=TRIBUTE"
driver.get(BASE_URL)
try:
	first_name = driver.find_element_by_name("ctl00$phMain$ucContest$txtFirstName")
	last_name = driver.find_element_by_name("ctl00$phMain$ucContest$txtLastName")
	street_address = driver.find_element_by_name("ctl00$phMain$ucContest$txtAddress")
	city = driver.find_element_by_name("ctl00$phMain$ucContest$txtCity")
	postal_code = driver.find_element_by_name("ctl00$phMain$ucContest$txtPostalCode")
	email_address = driver.find_element_by_name("ctl00$phMain$ucContest$email")
	phone_number = driver.find_element_by_name("ctl00$phMain$ucContest$txtPhone")
	skill_test = driver.find_element_by_name("ctl00$phMain$ucContest$txtSkillTest")
	
	# write to screen
	skill_test.send_keys("love, time and death")
	first_name.send_keys(my_data[0])
	last_name.send_keys(my_data[1])
	street_address.send_keys(my_data[4])
	city.send_keys(my_data[5])
	postal_code.send_keys(my_data[-3])
	email_address.send_keys(my_data[3])
	phone_number.send_keys(my_data[-1])
	
	driver.find_element_by_xpath("//select[@name='ctl00$phMain$ucContest$ddlProvince']/option[text()='Ontario']").click()#mySelect = Select(driver.find_element_by_id("ddlProvince"))#mySelect.select_by_value("ON") #driver.find_element_by_xpath("//select[@id='ddlProvince']/option[@value='Ontario']").click()
	driver.find_element_by_id("rbMale").click() #driver.find_element_by_xpath("//select[@id='rbMale']").click()
	driver.find_element_by_xpath("//select[@name='ctl00$phMain$ucContest$ddlAge']/option[text()='25 - 34']").click() #driver.find_element_by_xpath("//select[@id='ddlAge']/option[@value='25-34']").click()
	driver.find_element_by_xpath("//select[@name='ctl00$phMain$ucContest$ddlAdSource']/option[text()='Other']").click()#driver.find_element_by_xpath("//select[@id='ddlAdSource']/option[@value='Other']").click()
	#driver.find_element_by_name("ctl00$phMain$ucContest$cbContestRules").click() #driver.find_element_by_xpath('//select[@id="cbContestRules"]').click()
	driver.find_element_by_name("ctl00$phMain$ucContest$btnSubmit").click()
	
except:
	e = sys.exc_info()
	print(e)
	#driver.quit()
	sys.exit(1)

BASE_URL = "http://www.tribute.ca/contests/movies-for-a-year-c3796/?referrer=TRIBUTE"
driver.get(BASE_URL)
try:
	first_name = driver.find_element_by_name("ctl00$phMain$ucContest$txtFirstName")
	last_name = driver.find_element_by_name("ctl00$phMain$ucContest$txtLastName")
	street_address = driver.find_element_by_name("ctl00$phMain$ucContest$txtAddress")
	city = driver.find_element_by_name("ctl00$phMain$ucContest$txtCity")
	postal_code = driver.find_element_by_name("ctl00$phMain$ucContest$txtPostalCode")
	email_address = driver.find_element_by_name("ctl00$phMain$ucContest$email")
	phone_number = driver.find_element_by_name("ctl00$phMain$ucContest$txtPhone")
	skill_test = driver.find_element_by_name("ctl00$phMain$ucContest$txtSkillTest")
	
	# write to screen
	skill_test.send_keys("30")
	first_name.send_keys(my_data[0])
	last_name.send_keys(my_data[1])
	street_address.send_keys(my_data[4])
	city.send_keys(my_data[5])
	postal_code.send_keys(my_data[-3])
	email_address.send_keys(my_data[3])
	phone_number.send_keys(my_data[-1])
	
	driver.find_element_by_xpath("//select[@name='ctl00$phMain$ucContest$ddlProvince']/option[text()='Ontario']").click()
	driver.find_element_by_id("rbMale").click() 
	driver.find_element_by_xpath("//select[@name='ctl00$phMain$ucContest$ddlAge']/option[text()='25 - 34']").click() 
	driver.find_element_by_xpath("//select[@name='ctl00$phMain$ucContest$ddlAdSource']/option[text()='Other']").click()
	driver.find_element_by_name("ctl00$phMain$ucContest$btnSubmit").click()
	timer.sleep(8)
except:
	e = sys.exc_info()
	print(e)
	sys.exit(1)

BASE_URL = "http://www.tribute.ca/contests/tiff-2016-gift-bag-contest-c3780/?referrer=TRIBUTE"
driver.get(BASE_URL)
try:
	first_name = driver.find_element_by_name("ctl00$phMain$ucContest$txtFirstName")
	last_name = driver.find_element_by_name("ctl00$phMain$ucContest$txtLastName")
	street_address = driver.find_element_by_name("ctl00$phMain$ucContest$txtAddress")
	city = driver.find_element_by_name("ctl00$phMain$ucContest$txtCity")
	postal_code = driver.find_element_by_name("ctl00$phMain$ucContest$txtPostalCode")
	email_address = driver.find_element_by_name("ctl00$phMain$ucContest$email")
	phone_number = driver.find_element_by_name("ctl00$phMain$ucContest$txtPhone")
	skill_test = driver.find_element_by_name("ctl00$phMain$ucContest$txtSkillTest")
	
	# write to screen
	skill_test.send_keys("62")
	first_name.send_keys(my_data[0])
	last_name.send_keys(my_data[1])
	street_address.send_keys(my_data[4])
	city.send_keys(my_data[5])
	postal_code.send_keys(my_data[-3])
	email_address.send_keys(my_data[3])
	phone_number.send_keys(my_data[-1])
	
	driver.find_element_by_xpath("//select[@name='ctl00$phMain$ucContest$ddlProvince']/option[text()='Ontario']").click()
	driver.find_element_by_id("rbMale").click() 
	driver.find_element_by_xpath("//select[@name='ctl00$phMain$ucContest$ddlAge']/option[text()='25 - 34']").click() 
	driver.find_element_by_xpath("//select[@name='ctl00$phMain$ucContest$ddlAdSource']/option[text()='Other']").click()
	driver.find_element_by_name("ctl00$phMain$ucContest$btnSubmit").click()
except:
	e = sys.exc_info()
	print(e)
	sys.exit(1)










