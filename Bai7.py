from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:/webdriver/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

url = "http://practice.automationtesting.in/"
driver.get(url)

element = driver.find_element_by_id("menu-item-50").click()

email = driver.find_element_by_id("reg_email").send_keys("Email Address")
password = driver.find_element_by_id("reg_password").send_keys("password")
button = driver.find_element_by_name("register").click()


time.sleep(5)

driver.close()

