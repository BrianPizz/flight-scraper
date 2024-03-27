from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import os
import random

# Define a list of user-agent strings to mimic different web browsers
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
]

# Initialize Chrome WebDriver with options
chrome_driver_path = "/Users/pizz/Desktop/chromedriver"
options = Options()
options.add_argument("--headless")  # Run browser in headless mode
options.add_argument(f"user-agent={random.choice(user_agents)}")  # Set a random user-agent
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# URL of the website to scrape
url = "https://www.expedia.com/Flights-Search?flight-type=on&mode=search&trip=roundtrip&leg1=from:Los%20Angeles,%20CA,%20United%20States%20of%20America%20(LAX-Los%20Angeles%20Intl.),to:Columbus,%20OH,%20United%20States%20of%20America%20(CMH-John%20Glenn%20Columbus%20Intl.),departure:4/9/2024TANYT&leg2=from:Columbus,%20OH,%20United%20States%20of%20America%20(CMH-John%20Glenn%20Columbus%20Intl.),to:Los%20Angeles,%20CA,%20United%20States%20of%20America%20(LAX-Los%20Angeles%20Intl.),departure:4/16/2024TANYT&options=cabinclass:economy&fromDate=4/9/2024&toDate=4/16/2024&d1=2024-4-9&d2=2024-4-16&passengers=adults:1,infantinlap:N"

# Open the website in the browser
driver.get(url)

# Wait for the search results to load (you can adjust the sleep time as needed)
time.sleep(10)

# Close the browser when done
driver.quit()
