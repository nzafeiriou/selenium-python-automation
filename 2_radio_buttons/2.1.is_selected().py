from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://demo.automationtesting.in/Register.html")
male = driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[5]/div/label[1]/input')
if male.is_selected():
    print("Male selected")
else:
    print("Male not selected")

