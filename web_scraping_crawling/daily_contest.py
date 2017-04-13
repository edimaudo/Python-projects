from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time
import sys

path = os.path.dirname(os.path.abspath(__file__))
path_to_chromedriver = path + "/" + 'chromedriver'	
my_data =  ["Edima", "Udo", "Edima Udo",
'edimaudo@outlook.com',"12 Southgate Avenue","Toronto","M3N 1P2", "Ontario", "6479876976"]
driver = webdriver.Chrome(path_to_chromedriver)

def main():
	#do something


if __name__ == "__main__":
	main()