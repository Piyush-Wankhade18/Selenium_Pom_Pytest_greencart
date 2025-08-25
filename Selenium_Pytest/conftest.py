import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="class")
def setup(request):
    service_object = Service(r"C:\Users\HP\Desktop\C_Drive\chrome webdriver\chromedriver.exe")
    driver = webdriver.Chrome(service=service_object)
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.quit()
