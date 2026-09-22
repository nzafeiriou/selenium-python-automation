from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service =Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/dynamic_controls")
button = driver.find_element(By.XPATH,'//*[@id="checkbox-example"]/button')
button.click()
wait = WebDriverWait(driver, 10)
remove = wait.until(
EC.invisibility_of_element_located((By.ID,"checkbox"))
)
