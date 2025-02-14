# Selenium wait
#
# Implicit wait-- It is a global wait --It comes from webdriver -- and it is applicable on web page
# explicit wait --conditional wait -- we have to import it -- it is applicable on a particular locator

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ye jo ham kar rahe hai we are doing it in version 3 to do it in version 4 we need a service object
service_object = Service(r"C:\Users\HP\Desktop\C_Drive\chrome webdriver\chromedriver.exe")
# set chrome driver .exe path
# driver = webdriver.Chrome(r"C:\Users\HP\Desktop\C_Drive\chrome webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)
driver.implicitly_wait(7)
# url
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(3)
result_products=driver.find_elements (By.XPATH,"//div[@class='products']/div")
count = len(result_products)
print(count)
assert count > 0
# selenium chaining
for results in result_products:
    results.find_element(By.XPATH,"div/button").click()
    time.sleep(1)
driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.CSS_SELECTOR,"div[class='action-block'] button").click()
time.sleep(2)
# sum validation
total=driver.find_elements(By.XPATH,"//tr/td[5]/p")

sum = 0
for price in total:
    sum = sum+int(price.text)
print(sum)
total_amount=driver.find_element(By.CSS_SELECTOR,"span[class='totAmt']")
print(int(total_amount.text))
assert sum == int(total_amount.text)
driver.find_element(By.CSS_SELECTOR,"input[class='promoCode']").send_keys("rahulshettyacademy")
driver.implicitly_wait(7)
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
time.sleep(7)
link=driver.find_element(By.XPATH,"//div[@style]/button")
link.click()
time.sleep(7)
driver.find_element(By.CSS_SELECTOR,"select[style]").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"select[style]").send_keys("india")
select_dropdown=Select(driver.find_element(By.CSS_SELECTOR,"select[style]"))
select_dropdown.select_by_visible_text('India')

driver.find_element(By.CSS_SELECTOR,"input[type='checkbox']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[@style]/button").click()
time.sleep(7)
driver.close()

# https://rahulshettyacademy.com/seleniumPractise/#/country
