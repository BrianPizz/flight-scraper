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
url = "https://www.expedia.com/Flights-Search?flight-type=on&mode=search&trip=roundtrip&leg1=from:Los%20Angeles,%20CA,%20United%20States%20of%20America%20(LAX-Los%20Angeles%20Intl.),to:Columbus,%20OH,%20United%20States%20of%20America%20(CMH-John%20Glenn%20Columbus%20Intl.),departure:4/9/2024TANYT&leg2=from:Columbus,%20OH,%20United%20States%20of%20America%20(CMH-John%20Glenn%20Columbus%20Intl.),to:Los%20Angeles,%20CA,%20United%20States%20of%20America%20(LAX-Los%20Angeles%20Intl.),departure:4/16/2024TANYT&options=cabinclass:economy&fromDate=4/9/2024&toDate=4/16/2024&d1=2024-4-9&d2=2024-4-16&passengers=adults:1,infantinlap:N"

# Open the website in the browser
driver.get(url)

# Wait for the search results to load (you can adjust the sleep time as needed)
time.sleep(10)

# Close the browser when done
driver.quit()
