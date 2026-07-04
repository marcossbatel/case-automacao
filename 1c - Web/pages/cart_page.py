from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    TITLE = (By.CSS_SELECTOR, "span.title")
    CART_ITEMS = (By.CSS_SELECTOR, ".cart_item .inventory_item_name")
    REMOVE_BUTTON = (By.XPATH, "//button[contains(text(), 'Remove')]")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def is_open(self):
        self.find(self.TITLE)

    def product_titles(self):
        return [item.text for item in self.find_all(self.CART_ITEMS)]

    def remove_item(self, name):
        locator = (By.XPATH, f"//div[@class='inventory_item_name' and normalize-space(text())='{name}']/ancestor::div[contains(@class,'cart_item')]//button[contains(text(), 'Remove')]")
        self.click(locator)

    def checkout(self):
        self.click(self.CHECKOUT_BUTTON)
