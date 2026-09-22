from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://demo.automationtesting.in/Register.html")
female = driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[5]/div/label[2]')
if female.is_selected():
    print("Before: True")
else:
    print("Before: False")
female.click()
if female.is_selected():
    print("After: True")