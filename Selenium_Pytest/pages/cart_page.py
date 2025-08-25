from selenium.webdriver.common.by import By

class CartPage:
    item_prices = (By.XPATH, "//tr/td[5]/p")
    total_amount = (By.CSS_SELECTOR, "span.totAmt")
    promo_code = (By.CSS_SELECTOR, "input.promoCode")
    promo_button = (By.CSS_SELECTOR, ".promoBtn")
    promo_info = (By.CSS_SELECTOR, "span.promoInfo")
    place_order_button = (By.XPATH, "//div[@style]/button")

    def __init__(self, driver):
        self.driver = driver

    def calculate_sum(self):
        prices = self.driver.find_elements(*self.item_prices)
        return sum(int(price.text) for price in prices)

    def get_total_amount(self):
        return int(self.driver.find_element(*self.total_amount).text)

    def apply_promo_code(self, code):
        self.driver.find_element(*self.promo_code).send_keys(code)
        self.driver.find_element(*self.promo_button).click()

    def place_order(self):
        self.driver.find_element(*self.place_order_button).click()
