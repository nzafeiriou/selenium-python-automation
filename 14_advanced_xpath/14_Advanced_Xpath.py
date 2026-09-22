from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/login")
button = driver.find_element(By.XPATH, '//button[.//i[contains(text(),"Login")]]')
button.click()
print(driver.current_url)