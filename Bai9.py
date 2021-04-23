from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select

chrome_driver_path = "C:/webdriver/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

url = "https://itmscoaching.herokuapp.com/form"
driver.get(url)

inputFirstName = driver.find_element_by_id("first-name").send_keys("Binh")
inputLastName = driver.find_element_by_id("last-name").send_keys("Nguyen")
inputJobTitle = driver.find_element_by_id("job-title").send_keys("Tester")
radioLoe = driver.find_element_by_id("radio-button-3").click()
checkboxSex = driver.find_element_by_id("checkbox-2").click()
selectmenuYears = driver.find_element_by_xpath('//*[@id="select-menu"]/option[4]').click()
date = driver.find_element_by_id("datepicker").send_keys("20/7/2011")
btnSubmit = driver.find_element_by_xpath('/html/body/div/form/div/div[8]/a').click()
time.sleep(5)

# driver.close()

