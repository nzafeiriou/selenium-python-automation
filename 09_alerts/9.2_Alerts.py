from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
button2 = driver.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[2]/button')
button2.click()
alert = driver.switch_to.alert
print(alert.text)
alert.dismiss()