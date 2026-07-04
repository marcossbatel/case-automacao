from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    URL_FRAGMENT = "/inventory.html"
    PRODUCT_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def is_open(self):
        self.wait_url_contains(self.URL_FRAGMENT)

    def product_titles(self):
        return [item.text for item in self.find_all(self.PRODUCT_NAMES)]

    def add_product_to_cart(self, name):
        locator = (By.XPATH, f"//div[contains(@class,'inventory_item_name') and normalize-space(text())='{name}']/ancestor::div[contains(@class,'inventory_item')]//button")
        self.click(locator)

    def remove_product_from_cart(self, name):
        locator = (By.XPATH, f"//div[contains(@class,'inventory_item_name') and normalize-space(text())='{name}']/ancestor::div[contains(@class,'inventory_item')]//button[contains(text(), 'Remove')]")
        self.click(locator)

    def open_cart(self):
        self.click(self.CART_LINK)

    def open_product(self, name):
        locator = (By.XPATH, f"//div[contains(@class,'inventory_item_name') and normalize-space(text())='{name}']")
        self.click(locator)

    def cart_quantity(self):
        badge = self.driver.find_elements(*self.CART_BADGE)
        return int(badge[0].text) if badge else 0
