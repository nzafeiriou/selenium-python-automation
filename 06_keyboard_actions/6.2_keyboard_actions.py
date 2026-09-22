from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/key_presses")
item = driver.find_element(By.ID,'target')
item.send_keys("Hello World")

item.send_keys(Keys.CONTROL, "a")

item.send_keys("QA")
