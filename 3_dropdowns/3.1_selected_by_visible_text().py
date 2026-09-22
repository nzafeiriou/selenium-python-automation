from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

service = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/dropdown")
option = driver.find_element(By.ID,"dropdown")
dropdown = Select(option)
dropdown.select_by_visible_text("Option 2")
print(dropdown.first_selected_option.text)