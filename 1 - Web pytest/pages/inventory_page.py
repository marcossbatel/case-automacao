from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")
    BACKPACK_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def valida_home(self):
        return self.is_visible(self.INVENTORY_LIST)

    def adicionar_backpack_ao_carrinho(self):
        self.click(self.BACKPACK_ADD_BUTTON)
        return self

    def contador_badge_carrinho(self):
        return self.localizar(self.CART_BADGE).text

    def open_cart(self):
        self.click(self.CART_LINK)
        return self
