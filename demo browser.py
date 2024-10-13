import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service

service_obj = Service("C:/Users/ganki/OneDrive/Documents/msedgedriver.exe")
driver = webdriver.Edge(service=service_obj)
driver = webdriver.Edge()

driver.get("https://rahulshettyacademy.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)















time.sleep(2)