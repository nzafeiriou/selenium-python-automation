from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/windows")
link = driver.find_element(By.XPATH,'//*[@id="content"]/div/a')
link.click()
driver.window_handles
driver.switch_to.window(driver.window_handles[1])
print(driver.title)
