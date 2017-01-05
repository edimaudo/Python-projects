from selenium import webdriver

path_to_chromedriver = '/Users/Edima/Desktop/chromedriver' #change as needed

driver = webdriver.Chrome(path_to_chromedriver)
driver.get("http://www.youtube.com/results?search_query=" + "guitar+lessons")

results = driver.find_elements_by_xpath('//div[@class="yt-lockup-content"]')

print(len(results))

for result in results:
    video = result.find_element_by_xpath('.//h3/a')
    title = video.get_attribute('title')
    url = video.get_attribute('href')
    print("{} ({})".format(title, url))
driver.quit()