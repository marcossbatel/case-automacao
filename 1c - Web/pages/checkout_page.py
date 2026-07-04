from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.ID, "cancel")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_MESSAGE = (By.CLASS_NAME, "complete-header")

    def continue_checkout(self, first_name, last_name, postal_code):
        self.type_text(self.FIRST_NAME, first_name)
        self.type_text(self.LAST_NAME, last_name)
        self.type_text(self.POSTAL_CODE, postal_code)
        self.click(self.CONTINUE_BUTTON)

    def cancel_checkout(self):
        self.click(self.CANCEL_BUTTON)

    def finish_checkout(self):
        self.click(self.FINISH_BUTTON)

    def completion_text(self):
        return self.get_text(self.COMPLETE_MESSAGE)
