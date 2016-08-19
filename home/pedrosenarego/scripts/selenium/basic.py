import os
from selenium import webdriver

driver= webdriver.Chrome()
driver.get("http://www.google.com")
print driver.page_source.encode('utf-8')
driver.get("http://stackoverflow.com/q/3369073/395287")
driver.save_screenshot("/home/pedro/Dropbox/pastaPessoal/3Dprinter/inmoov/scripts/selenium/teste.png") 

driver.quit()
display.stop()

