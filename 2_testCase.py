import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.dealsdray.com/")
driver.maximize_window()

driver.implicitly_wait(10)

driver.find_element(By.NAME, "username").send_keys("prexo.mis@dealsdray.com")
driver.find_element(By.NAME, "password").send_keys("prexo.mis@dealsdray.com")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

driver.find_element(By.XPATH, "//button[@class='MuiButtonBase-root has-submenu compactNavItem css-46up3a']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='Orders']").click()
driver.find_element(By.XPATH, "//button[normalize-space()='Add Bulk Orders']").click()
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/input[1]").send_keys("C:\\Users\\Suraj\\Downloads\\demo-data.xlsx")
driver.find_element(By.XPATH,"//button[normalize-space()='Import']").click()
driver.find_element(By.XPATH,"//button[normalize-space()='Validate Data']").click()

time.sleep(5)
driver.switch_to.alert.accept()

driver.find_element(By.XPATH,"//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium css-adjfm3']").click()
driver.save_screenshot("C:\Screenshot\demoexcel.png")

driver.close()