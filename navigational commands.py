from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj=Service("C:/Users/DELL/PycharmProjects/chromedriver-win64/chromedriver.exe")
d=webdriver.Chrome(service=serv_obj)
d.get("https://demo.nopcommerce.com/")
d.get("https://www.amazon.in/")

d.maximize_window()
d.back() 
d.forward()
d.refresh()

time.sleep(5)
d.quit()