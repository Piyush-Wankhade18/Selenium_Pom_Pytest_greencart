from selenium.webdriver.common.by import By

class HomePage:
    search_box = (By.CSS_SELECTOR, ".search-keyword")
    product_list = (By.XPATH, "//div[@class='products']/div")
    add_to_cart_btn = (By.XPATH, "div/button")
    cart_icon = (By.CSS_SELECTOR, "img[alt='Cart']")
    proceed_to_checkout = (By.CSS_SELECTOR, "div[class='action-block'] button")

    def __init__(self, driver):
        self.driver = driver

    def search_product(self, product_name):
        self.driver.find_element(*self.search_box).send_keys(product_name)

    def get_products(self):
        return self.driver.find_elements(*self.product_list)

    def add_products_to_cart(self):
        for product in self.get_products():
            product.find_element(*self.add_to_cart_btn).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()
        self.driver.find_element(*self.proceed_to_checkout).click()
