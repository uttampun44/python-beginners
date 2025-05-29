from selenium import webdriver as webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys as keys
import time

# chromedriver.exe should be in the same directory as this script
service = ChromeService(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# driver.get("https://www.google.com")
driver.get("https://www.google.com")

# Wait for the page to load
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")

# send keys to the input element
input_element.send_keys("Uttam Pun Frontend Developer" + keys.ENTER)

input("Press Enter to close the browser...")
driver.quit()