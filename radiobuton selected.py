from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj=Service("C:/Users/DELL/PycharmProjects/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_input_radio")
driver.maximize_window()

time.sleep(3)

# ✅ Switch to iframe where radio buttons exist
driver.switch_to.frame("iframeResult")

# Now find the Male radio button
male_radio = driver.find_element(By.XPATH, "//input[@type='radio' and @value='male']")

# Check if it is selected
if male_radio.is_selected():
    print("Male radio button is already selected.")
else:
    print("Male radio button is not selected. Selecting it now.")
    male_radio.click()

# Wait to observe
time.sleep(3)

# Close browser
driver.quit()
