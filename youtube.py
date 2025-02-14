import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# specify the path to the chromedriver
service_object = Service(r"C:\Users\HP\Desktop\C_Drive\chrome webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)

# navigate to the YouTube website
driver.get("https://www.youtube.com/")

# find the search bar element
search_bar = driver.find_element(By.XPATH,'//input[@id="search"]')

# type in the search query
search_bar.send_keys("simroon tera naam song")

# hit the Enter key
search_bar.send_keys(Keys.RETURN)

# wait for the search results to load

# add the appropriate wait time based on your internet speed
time.sleep(5)

#driver.find_element(By.XPATH,'//*[@id="video-title"]').click()
driver.find_element(By.id,'//*[@id="video-title"]').click()

# Wait for the video to load
# Replace the 10 second wait with a wait for the desired element to appear
time.sleep(5)

# Find the play button element and click on it
driver.find_element(By.XPATH,'//*[@id="movie_player"]/div[1]/video')

time.sleep(20)

driver.close()
