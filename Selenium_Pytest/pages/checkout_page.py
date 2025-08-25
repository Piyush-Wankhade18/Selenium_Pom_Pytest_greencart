from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class CheckoutPage:
    country_dropdown = (By.CSS_SELECTOR, "select[style]")
    terms_checkbox = (By.CSS_SELECTOR, "input[type='checkbox']")
    proceed_button = (By.XPATH, "//div[@style]/button")

    def __init__(self, driver):
        self.driver = driver

    def select_country(self, country_name):
        dropdown = Select(self.driver.find_element(*self.country_dropdown))
        dropdown.select_by_visible_text(country_name)

    def agree_terms_and_submit(self):
        self.driver.find_element(*self.terms_checkbox).click()
        self.driver.find_element(*self.proceed_button).click()
