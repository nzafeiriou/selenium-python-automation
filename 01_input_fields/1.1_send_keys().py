from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/login")

username = driver.find_element(By.ID,"username")
username.send_keys("tomsmith")
pwd = driver.find_element(By.ID,"password")
pwd.send_keys("SuperSecretPassword!")
time.sleep(5)