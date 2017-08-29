import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('http://inmoov.fr')

elm = browser.find_element_by_link_text('Blog')
browser.implicitly_wait(5)
elm.click()

#browser = webdriver.Chrome()
#browser.get('https://mightytext.net/web8/?exp=1')

#elm = browser.find_element_by_link_text('Scheduler')
#browser.implicitly_wait(5)
#elm.click()



