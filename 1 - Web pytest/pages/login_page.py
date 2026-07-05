from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def open(self):
        super().open("https://www.saucedemo.com/")
        return self

    def login(self, username="standard_user", password="secret_sauce"):
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        return self
