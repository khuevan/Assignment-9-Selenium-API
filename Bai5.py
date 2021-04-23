from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chrome_driver_path = "C:/webdriver/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

url = "http://practice.automationtesting.in/"
driver.get(url)

driver.set_window_size(500,500)

print(driver.current_url)

time.sleep(5)

driver.close()

