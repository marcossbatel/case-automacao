from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    ZIP_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_MESSAGE = (By.CLASS_NAME, "complete-header")

    def fill_customer_info(self, first_name="Joao", last_name="Silva", zip_code="12345"):
        self.type_text(self.FIRST_NAME_INPUT, first_name)
        self.type_text(self.LAST_NAME_INPUT, last_name)
        self.type_text(self.ZIP_CODE_INPUT, zip_code)
        self.click(self.CONTINUE_BUTTON)
        return self

    def finish_order(self):
        self.click(self.FINISH_BUTTON)
        return self

    def is_complete(self):
        return self.is_visible(self.COMPLETE_MESSAGE)
