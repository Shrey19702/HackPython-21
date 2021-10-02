# An automation script to help browse anything on google.
# Provide your search query in the send_keys() method

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver')

driver.get("https://google.com")

search = driver.find_element_by_xpath("//input[@name='q']")
search.send_keys("Hello world")
search.submit()