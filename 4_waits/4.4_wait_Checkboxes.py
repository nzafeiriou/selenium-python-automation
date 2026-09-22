from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/")
driver.find_element(By.LINK_TEXT,"Checkboxes").click()
wait = WebDriverWait(driver, 10)
checkbox =wait.until(
    EC.element_to_be_clickable((By.XPATH,"//input[@type='checkbox']"))
)
checkbox.click()
time.sleep(4)
#checkboxes = driver.find_elements(By.XPATH,'//input[@type="checkbox"]')
#if not checkboxes[0].is_selected():
    #checkboxes[0].click()


