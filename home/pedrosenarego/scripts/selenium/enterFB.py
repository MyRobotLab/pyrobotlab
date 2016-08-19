import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()
browser.get('https://www.facebook.com/')
time.sleep(10)

username = browser.find_element_by_css_selector('#email')
username.send_keys('pedrogilsenarego@hotmail.com')
password = browser.find_element_by_css_selector('#pass')
password.send_keys('***pass***')

login = browser.find_element_by_css_selector('#u_0_p')

login.click()





#elm = browser.find_element_by_link_text('Scheduler')
#browser.implicitly_wait(5)
#elm.click()

#password = browser.find_element_by_id('Password')
#password.send_keys('Pokemon1337')
