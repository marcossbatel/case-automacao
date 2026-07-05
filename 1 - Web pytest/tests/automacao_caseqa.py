import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-features=PasswordLeakDetection,PasswordManagerOnboarding")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-password-manager-reauthentication")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_login_opens_inventory_page(driver):
    login_page = LoginPage(driver).abrir()
    login_page.login()

    inventory_page = InventoryPage(driver)
    assert inventory_page.is_open()


def test_add_item_to_cart_and_open_cart(driver):
    LoginPage(driver).abrir().login()
    inventory_page = InventoryPage(driver)
    inventory_page.adicionar_backpack_ao_carrinho()
    assert inventory_page.cart_badge_count() == "1"

    inventory_page.open_cart()
    cart_page = CartPage(driver)
    assert cart_page.is_open()
    assert cart_page.has_item()


def test_remover_item_do_carrinho(driver):
    LoginPage(driver).abrir().login()
    InventoryPage(driver).adicionar_backpack_ao_carrinho()
    InventoryPage(driver).open_cart()

    cart_page = CartPage(driver)
    cart_page.remove_item()
    assert cart_page.is_open()


def test_finish_checkout(driver):
    LoginPage(driver).abrir().login()
    InventoryPage(driver).adicionar_backpack_ao_carrinho().open_cart()

    cart_page = CartPage(driver)
    cart_page.checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_customer_info()
    checkout_page.finish_order()

    assert checkout_page.is_complete()
