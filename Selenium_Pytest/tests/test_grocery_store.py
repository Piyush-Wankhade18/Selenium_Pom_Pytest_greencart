import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.mark.usefixtures("setup")
class TestGroceryStore:

    def test_purchase_flow(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

        # Home Page
        home = HomePage(driver)
        home.search_product("ber")

        wait.until(EC.presence_of_all_elements_located(home.product_list))
        assert len(home.get_products()) > 0

        home.add_products_to_cart()
        home.go_to_cart()

        # Cart Page
        cart = CartPage(driver)
        cart_sum = cart.calculate_sum()
        total_amount = cart.get_total_amount()
        assert cart_sum == total_amount

        cart.apply_promo_code("rahulshettyacademy")
        promo_message = wait.until(EC.presence_of_element_located(cart.promo_info)).text
        assert "applied" in promo_message.lower()

        cart.place_order()

        # Checkout Page
        checkout = CheckoutPage(driver)
        checkout.select_country("India")
        checkout.agree_terms_and_submit()
