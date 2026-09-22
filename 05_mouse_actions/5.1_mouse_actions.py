from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

service = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/hovers")
image1 = driver.find_element(By.XPATH,'//*[@id="content"]/div/div[1]/img')
actions = ActionChains(driver)
actions.move_to_element(image1).perform()
caption = driver.find_element(By.XPATH,'//*[@id="content"]/div/div[1]/div/h5')
print(caption.is_displayed())
