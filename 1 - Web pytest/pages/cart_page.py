from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    TITLE = (By.CSS_SELECTOR, ".title")
    ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    REMOVE_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def is_open(self):
        return self.find(self.TITLE).text == "Your Cart"

    def has_item(self):
        return self.is_visible(self.ITEM_NAME)

    def remove_item(self):
        self.click(self.REMOVE_BUTTON)
        return self

    def checkout(self):
        self.click(self.CHECKOUT_BUTTON)
        return self
