from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os

# Initialize Chrome WebDriver (replace the path with your ChromeDriver path)
chrome_driver_path = "/Users/pizz/Desktop/chromedriver"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

url = "https://google.com"

driver.get(url)

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear()
input_element.send_keys("dune 2" + Keys.ENTER)

time.sleep(10)

driver.quit()