from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
button = driver.find_element(By.ID,"start")
button.click()
wait = WebDriverWait(driver, 10)
helloWord = wait.until(
  EC.visibility_of_element_located((By.ID,"finish"))
)
