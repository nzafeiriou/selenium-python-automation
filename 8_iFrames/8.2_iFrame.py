from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/iframe")
frame = driver.find_element(By.ID,"mce_0_ifr")
driver.switch_to.frame(frame)
editor = driver.find_element(By.ID,"tinymce")
print(editor.text)
driver.switch_to.default_content()
header = driver.find_element(By.TAG_NAME,"h3")
print(header.text)
