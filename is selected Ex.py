from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj=Service("C:/Users/DELL/PycharmProjects/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

# Open the website
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
m_radb=driver.find_element(By.XPATH,'//*[@id="gender-male"]')
f_radb=driver.find_element(By.XPATH,"//label[@for='gender-radio-2']")
o_radb=driver.find_element(By.XPATH,"//label[@for='gender-radio-3']")
print(m_radb.is_selected())
print(f_radb.is_selected())
print(o_radb.is_selected())
# m_radb=driver.find_element(By.XPATH,"//label[@for='gender-radio-1']")
# m_radb.click()
# print(m_radb.is_selected())
# print("After Female option clicked:",f_radb.is_selected())
# print(o_radb.is_selected())



# Wait for a while to see the result
time.sleep(3)

# Close the browser
driver.quit()
