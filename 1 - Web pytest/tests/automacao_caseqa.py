import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--window-size\=1920,1080")
    # options.add_argument("--disable-features\=PasswordLeakDetection,PasswordManagerOnboarding")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-password-manager-reauthentication")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_login_abre_home(driver):
    login_page = LoginPage(driver).abrir()
    login_page.login()

    inventory_page = InventoryPage(driver)
    assert inventory_page.valida_home()


def test_adicionar_item_ao_carrinho_e_abrir_carrinho(driver):
    LoginPage(driver).abrir().login()
    inventory_page = InventoryPage(driver)
    inventory_page.adicionar_backpack_ao_carrinho()
    assert inventory_page.contador_badge_carrinho() == "1"

    inventory_page.open_cart()
    cart_page = CartPage(driver)
    assert cart_page.valida_carrinho()
    assert cart_page.contem_item()


def test_remover_item_do_carrinho(driver):
    LoginPage(driver).abrir().login()
    InventoryPage(driver).adicionar_backpack_ao_carrinho()
    InventoryPage(driver).open_cart()

    cart_page = CartPage(driver)
    cart_page.remove_item()
    assert cart_page.valida_carrinho()


def test_finaliza_checkout(driver):
    LoginPage(driver).abrir().login()
    InventoryPage(driver).adicionar_backpack_ao_carrinho().open_cart()

    cart_page = CartPage(driver)
    cart_page.checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.preencher_informacoes_cliente()
    checkout_page.finalizar_pedido()

    assert checkout_page.pagina_sucesso()
