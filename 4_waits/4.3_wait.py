from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/dynamic_controls")
button = driver.find_element(By.XPATH,'//*[@id="checkbox-example"]/button')
button.click()
wait = WebDriverWait(driver, 10)
add = wait.until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="checkbox-example"]/button'))
)
add.click()
