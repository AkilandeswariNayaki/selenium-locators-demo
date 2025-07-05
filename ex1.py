from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj=Service("C:/Users/DELL/PycharmProjects/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://practicetestautomation.com/practice-test-login/")
#driver.get("https://demoqa.com/")
driver.maximize_window()
#Absolute path ex
# driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[1]/div[1]/input").send_keys("Javascript")
# driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[1]/div[1]/div/svg").click()
#driver.find_element(By.XPATH,"//input[@id='tnb-google-search-input']")
# driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[1]/div[1]/input").send_keys("html")
# driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[1]/div[1]/div/svg").click()
#Realtive XPATH EX
# driver.find_element(By.XPATH,"//input[@id='tnb-google-search-input']").send_keys("python")
# driver.find_element(By.XPATH,"//div[@id='tnb-google-search-submit-btn']//*[name()='
driver.find_element(By.XPATH,"/html/body/div/div/header/div[3]/div[1]/div/div[2]/div/nav/ul/li[2]/a").click()
driver.find_element(By.XPATH,"/html/body/div/div/section/div/div/article/div[2]/div[1]/div[1]/p/a").click()
driver.find_element(By.XPATH,"/html/body/div/div/section/section/div[1]/div[1]/input").send_keys("student")
driver.find_element(By.XPATH,"/html/body/div/div/section/section/div[1]/div[2]/input").send_keys("Password123")
driver.find_element(By.XPATH,"/html/body/div/div/section/section/div[1]/button").click()


#CONTAINS AND STARTS WITH EXAMPLE & text

#driver.find_element(By.XPATH,"//*[contains(@class,'banner-')]").click()
#driver.find_element(By.XPATH,"//*[starts-with(@class,'btn btn-primary')]").click()

#driver.find_element(By.XPATH,"//a[@class='btn btn-primary-shadow btn-block']").click()
#driver.find_element(By.CLASS_NAME,"btn btn-primary-shadow btn-block").click() #using class selector

#driver.find_element(By.XPATH,"//a[normalize-space()='Test Exceptions']").click()
time.sleep(20)
