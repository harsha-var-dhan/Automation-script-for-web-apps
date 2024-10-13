import  time
from selenium import webdriver


from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
name = "harsha"
service_obj = Service("C:/Users/ganki/OneDrive/Documents/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
alert.accept()
















time.sleep(5)