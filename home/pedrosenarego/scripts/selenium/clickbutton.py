import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('http://inmoov.fr/')

for i in browser.find_element_by_xpath("//*[@type='Blog']"):
    i.click()
    
time.sleep(6)


