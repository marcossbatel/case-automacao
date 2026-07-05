from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    ZIP_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_MESSAGE = (By.CLASS_NAME, "complete-header")

    def preencher_informacoes_cliente(self, primeiro_nome="Joao", ultimo_nome="Silva", zip_code="12345"):
        self.inserir_texto(self.FIRST_NAME_INPUT, primeiro_nome)
        self.inserir_texto(self.LAST_NAME_INPUT, ultimo_nome)
        self.inserir_texto(self.ZIP_CODE_INPUT, zip_code)
        self.click(self.CONTINUE_BUTTON)
        return self

    def finalizar_pedido(self):
        self.click(self.FINISH_BUTTON)
        return self

    def pagina_sucesso(self):
        return self.is_visible(self.COMPLETE_MESSAGE)
