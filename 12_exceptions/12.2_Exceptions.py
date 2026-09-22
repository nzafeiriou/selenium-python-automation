from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException

service = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/login")
try:
    username = driver.find_element(By.ID,"username")
    print("Username found")
except NoSuchElementException:
    print("The username was not found.")

try:
    wrongID = driver.find_element(By.ID,"wrongID")
    print("Element found")
except NoSuchElementException:
    print("Element not found")
