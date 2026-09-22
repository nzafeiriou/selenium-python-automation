from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/login")
username = driver.find_element(By.ID,"username")
username.send_keys("wrongUser")
username.clear()
username.send_keys("tomSmith")
user = username.get_attribute("value")
print(user)