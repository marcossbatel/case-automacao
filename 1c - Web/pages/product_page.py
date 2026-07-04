from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):
    TITLE = (By.CLASS_NAME, "inventory_details_name")
    ADD_BUTTON = (By.XPATH, "//button[contains(text(), 'Add to cart')]")
    REMOVE_BUTTON = (By.XPATH, "//button[contains(text(), 'Remove')]")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def title(self):
        return self.get_text(self.TITLE)

    def add_to_cart(self):
        self.click(self.ADD_BUTTON)

    def remove_from_cart(self):
        self.click(self.REMOVE_BUTTON)

    def open_cart(self):
        self.click(self.CART_LINK)
