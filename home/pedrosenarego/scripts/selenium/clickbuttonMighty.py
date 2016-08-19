import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()
browser.get('https://mightytext.net/web8/?exp=1')
time.sleep(3)


username = browser.find_element_by_css_selector('#Email')
browser.implicitly_wait(3)
username.send_keys('pedrogilsenarego@gmail.com')
login = browser.find_element_by_css_selector('#next')
login.click()

time.sleep(2)
password = browser.find_element_by_css_selector('#Passwd')
browser.implicitly_wait(3)
password.send_keys('****pass*****')
login = browser.find_element_by_css_selector('#signIn')
login.click()
time.sleep(5)

elm = browser.find_element_by_css_selector('#custom-alert-and-confirm-modal-cancel-button')
browser.implicitly_wait(5)
elm.click()

time.sleep(5)


elm = browser.find_element_by_css_selector('#newSms > span')
browser.implicitly_wait(5)
elm.click()

time.sleep(3)
NUMBER = sys.argv[1]
TEXT = sys.argv[2]

destinatary = browser.find_element_by_css_selector('#selectContactForSingleCompose')
browser.implicitly_wait(5)
destinatary.send_keys(str(NUMBER))
time.sleep(3)

elm = browser.find_element_by_css_selector('#send-one-text')
browser.implicitly_wait(5)
elm.click()


text = browser.find_element_by_css_selector('#send-one-text')
browser.implicitly_wait(3)
text.send_keys(str(TEXT))
time.sleep(3)

send = browser.find_element_by_css_selector('#send-button-single-text > div')
send.click()
time.sleep(3)



