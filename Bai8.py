from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:/webdriver/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

url = "https://the-internet.herokuapp.com/"
driver.get(url)

a = driver.find_element_by_link_text("Form Authentication").click()
inputusername = driver.find_element_by_name("username").send_keys("tomsmith")
inputpassword = driver.find_element_by_name("password").send_keys("SuperSecretPassword!")
btnlogin = driver.find_element_by_xpath('//*[@id="login"]/button').click()
get_title = driver.title
print(get_title)

time.sleep(5)

driver.close()

