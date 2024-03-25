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

# URL of the website to scrape
url = "https://google.com"

# Open the website in the browser
driver.get(url)

# Find the search input element by its class name
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")

# Clear any existing text in the search input field
input_element.clear()

# Enter the search query "dune 2" into the search input field and press Enter
input_element.send_keys("dune 2" + Keys.ENTER)

# Wait for the search results to load (you can adjust the sleep time as needed)
time.sleep(10)

# Close the browser when done
driver.quit()
