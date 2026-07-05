from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")
    BACKPACK_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def is_open(self):
        return self.is_visible(self.INVENTORY_LIST)

    def add_backpack_to_cart(self):
        self.click(self.BACKPACK_ADD_BUTTON)
        return self

    def cart_badge_count(self):
        return self.find(self.CART_BADGE).text

    def open_cart(self):
        self.click(self.CART_LINK)
        return self
