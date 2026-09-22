from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

service = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver =webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/dropdown")
item = driver.find_element(By.ID,"dropdown")
dropdown = Select(item)
dropdown.select_by_value("1")
time.sleep(2)

