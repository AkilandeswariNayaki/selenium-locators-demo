from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj=Service("C:/Users/DELL/PycharmProjects/chromedriver-win64/chromedriver.exe")
d=webdriver.Chrome(service=serv_obj)
d.get("https://www.facebook.com/")
d.maximize_window()
#css selector using1. Tag and Id
#d.find_element(By.CSS_SELECTOR,"input#email").send_keys("hai")
#or
# d.find_element(By.CSS_SELECTOR,"#email").send_keys("hai")
# d.find_element(By.CSS_SELECTOR,"input#pass").send_keys("<PASSWORD>")
# # css selector 2.Tag and Class
#d.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("success")
#or
# d.find_element(By.CSS_SELECTOR,".inputtext").send_keys("success")
# 3. tag name and one attribute
#d.find_element(By.CSS_SELECTOR,"input[data-testid=royal-email]").send_keys("wow")
#d.find_element(By.CSS_SELECTOR,"[data-testid=royal-email]").send_keys("wow")
# 4.tag class and attribute
d.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal-pass]").send_keys("success")
time.sleep(10)
d.quit()