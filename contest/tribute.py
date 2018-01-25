from selenium import webdriver
import sys
from datetime import date
import datetime
import time

count = 0
while(count < 5):
	path_to_chromedriver = '/Users/Edima/Desktop/contest/chromedriver' #change as needed
	my_data =  ["Edima", "Udo", "Edima Udo",
	'edimaudo@outlook.com',"76 Westgate Boulevard","Toronto","M3H 1P2", "Ontario", "6479876976"]

	contests = ["http://www.tribute.ca/contests/war-dogs-blu-ray-contest-c3806/?referrer=TRIBUTE",
	"http://www.tribute.ca/contests/hell-or-high-water-c3821/?referrer=TRIBUTE",
	"http://www.tribute.ca/contests/collateral-beauty-smart-phone-contest-c3814/",
	"http://www.tribute.ca/contests/zen-fone3-contest-c3819/",
	"http://www.tribute.ca/contests/tiff-2016-gift-bag-contest-c3780/?referrer=TRIBUTE",
	"http://www.tribute.ca/contests/movies-for-a-year-c3796/?referrer=TRIBUTE",
	"http://www.tribute.ca/contests/star-wars-the-force-awakens-droid-c3822/?referrer=TRIBUTE",
	"http://www.tribute.ca/contests/suicide-squad-blu-ray-c3823/?referrer=TRIBUTE",
	"http://www.tribute.ca/contests/lego-star-wars-blu-ray-c3826/?referrer=TRIBUTE",
	"http://www.tribute.ca/contests/casio-g-shock-watches-c3836/?referrer=TRIBUTE",
	"http://www.tribute.ca/contests/gourmet-gift-basket-c3837/?referrer=TRIBUTE",
	"http://www.tribute.ca/contests/the-accountant-blu-ray-c3852/?referrer=TRIBUTE"]
	special_answers = ["Miles Teller","Toby and Tanner","love, time and death",
	"Corning Gorilla Glass","62","6","map","Viola Davis","Kyber Saber","Casio","black Malbec","Christian Wolff"]
	driver = webdriver.Chrome(path_to_chromedriver)
	for value in range(len(contests)):
		if special_answers[value] == "Miles Teller" and date.today()>=datetime.date(2016, 12, 5):
			continue
		elif special_answers[value] == "Toby and Tanner" and date.today()>=datetime.date(2016, 12, 12):
			continue
		elif special_answers[value] == "love, time and death" and date.today()>=datetime.date(2017, 1, 9):
			continue
		elif special_answers[value] == "Corning Gorilla Glass" and date.today()>=datetime.date(2017, 1, 16):
			continue
		elif special_answers[value] == "62" and date.today()>=datetime.date(2017, 1, 20):
			continue
		elif special_answers[value] == "6" and date.today()>=datetime.date(2017, 1, 27):
			continue
		elif special_answers[value] == "map" and date.today()>=datetime.date(2017, 1, 13):
			continue
		elif special_answers[value] == "Viola Davis" and date.today()>=datetime.date(2017, 1, 9):
			continue
		elif special_answers[value] == "Kyber Saber" and date.today()>=datetime.date(2016, 12, 16):
			continue
		elif special_answers[value] == "Casio" and date.today()>=datetime.date(2017, 2, 8):
			continue		
		elif special_answers[value] == "black Malbec" and date.today()>=datetime.date(2017, 1, 16):
			continue
		elif special_answers[value] == "Christian Wolff" and date.today()>=datetime.date(2017, 1, 23):
			continue
		else:
			BASE_URL = contests[value]
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

				skill_test.send_keys(special_answers[value])
				time.sleep(1)
				first_name.send_keys(my_data[0])
				time.sleep(1)
				last_name.send_keys(my_data[1])
				time.sleep(1)
				street_address.send_keys(my_data[4])
				time.sleep(1)
				city.send_keys(my_data[5])
				time.sleep(1)
				postal_code.send_keys(my_data[-3])
				time.sleep(1)
				email_address.send_keys(my_data[3])
				time.sleep(1)
				phone_number.send_keys(my_data[-1])
				time.sleep(1)
				driver.find_element_by_xpath("//select[@name='ctl00$phMain$ucContest$ddlProvince']/option[text()='Ontario']").click()
				time.sleep(1)
				driver.find_element_by_id("rbMale").click() 
				time.sleep(1)
				driver.find_element_by_xpath("//select[@name='ctl00$phMain$ucContest$ddlAge']/option[text()='25 - 34']").click() 
				time.sleep(1)
				driver.find_element_by_xpath("//select[@name='ctl00$phMain$ucContest$ddlAdSource']/option[text()='Other']").click()
				time.sleep(1)
				driver.find_element_by_name("ctl00$phMain$ucContest$btnSubmit").click()
				time.sleep(1)
				count+=1
			except:
				e = sys.exc_info()
				print(e)
				driver.quit()
				sys.exit(1)
	driver.quit()
	time.sleep(60)


			