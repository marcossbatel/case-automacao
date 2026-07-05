from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def abrir(self):
        super().abrir_url("https://www.saucedemo.com/")
        return self

    def login(self, username="standard_user", password="secret_sauce"):
        self.inserir_texto(self.USERNAME_INPUT, username)
        self.inserir_texto(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        return self
