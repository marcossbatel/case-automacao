import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


BASE_URL = "https://www.saucedemo.com"
STANDARD_USER = "standard_user"
SECRET_SAUCE = "secret_sauce"
PRODUCT_BACKPACK = "Sauce Labs Backpack"
PRODUCT_JACKET = "Sauce Labs Fleece Jacket"
PRODUCT_BIKE_LIGHT = "Sauce Labs Bolt Bike Light"
PRODUCT_TSHIRT = "Sauce Labs Bolt T-Shirt"


def login(driver, username=STANDARD_USER, password=SECRET_SAUCE):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)
    return InventoryPage(driver)


def add_products_to_cart(inventory_page, *products):
    for product in products:
        inventory_page.add_product_to_cart(product)


@pytest.mark.parametrize(
    "username,password,error_message",
    [
        ("", SECRET_SAUCE, "Username is required"),
        (STANDARD_USER, "", "Password is required"),
        ("usuario_invalido", SECRET_SAUCE, "Username and password do not match any user in this service"),
        (STANDARD_USER, "senha_invalida", "Username and password do not match any user in this service"),
    ],
)
def test_login_errors(driver, username, password, error_message):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)
    assert error_message in login_page.get_error_message()


def test_login_with_valid_credentials(driver):
    inventory_page = login(driver)
    inventory_page.is_open()
    titles = inventory_page.product_titles()
    assert PRODUCT_BACKPACK in titles
    assert PRODUCT_JACKET in titles


def test_home_shows_products(driver):
    inventory_page = login(driver)
    titles = inventory_page.product_titles()
    assert len(titles) >= 6


def test_add_single_product_to_cart(driver):
    inventory_page = login(driver)
    inventory_page.add_product_to_cart(PRODUCT_BACKPACK)
    inventory_page.open_cart()
    cart_page = CartPage(driver)
    cart_page.is_open()
    assert PRODUCT_BACKPACK in cart_page.product_titles()


def test_add_multiple_products_to_cart(driver):
    inventory_page = login(driver)
    add_products_to_cart(inventory_page, PRODUCT_BACKPACK, PRODUCT_JACKET)
    inventory_page.open_cart()
    cart_page = CartPage(driver)
    cart_page.is_open()
    titles = cart_page.product_titles()
    assert PRODUCT_BACKPACK in titles
    assert PRODUCT_JACKET in titles


def test_remove_product_from_cart_from_home(driver):
    inventory_page = login(driver)
    inventory_page.add_product_to_cart(PRODUCT_BACKPACK)
    inventory_page.remove_product_from_cart(PRODUCT_BACKPACK)
    inventory_page.open_cart()
    cart_page = CartPage(driver)
    cart_page.is_open()
    assert PRODUCT_BACKPACK not in cart_page.product_titles()


def test_remove_product_from_cart_from_cart(driver):
    inventory_page = login(driver)
    inventory_page.add_product_to_cart(PRODUCT_BACKPACK)
    inventory_page.open_cart()
    cart_page = CartPage(driver)
    cart_page.is_open()
    cart_page.remove_item(PRODUCT_BACKPACK)
    assert PRODUCT_BACKPACK not in cart_page.product_titles()


def test_product_detail_navigation(driver):
    inventory_page = login(driver)
    inventory_page.open_product(PRODUCT_BACKPACK)
    product_page = ProductPage(driver)
    assert product_page.title() == PRODUCT_BACKPACK


def test_add_product_from_detail_page(driver):
    inventory_page = login(driver)
    inventory_page.open_product(PRODUCT_BACKPACK)
    product_page = ProductPage(driver)
    product_page.add_to_cart()
    product_page.open_cart()
    cart_page = CartPage(driver)
    assert PRODUCT_BACKPACK in cart_page.product_titles()


def test_remove_product_from_detail_page(driver):
    inventory_page = login(driver)
    inventory_page.open_product(PRODUCT_BACKPACK)
    product_page = ProductPage(driver)
    product_page.add_to_cart()
    product_page.remove_from_cart()
    product_page.open_cart()
    cart_page = CartPage(driver)
    assert PRODUCT_BACKPACK not in cart_page.product_titles()


def test_checkout_cancel_keeps_item_in_cart(driver):
    inventory_page = login(driver)
    inventory_page.add_product_to_cart(PRODUCT_BACKPACK)
    inventory_page.open_cart()
    cart_page = CartPage(driver)
    cart_page.checkout()
    checkout_page = CheckoutPage(driver)
    checkout_page.continue_checkout("João", "Silva", "12345")
    checkout_page.cancel_checkout()
    inventory_page.is_open()
    inventory_page.open_cart()
    cart_page = CartPage(driver)
    assert PRODUCT_BACKPACK in cart_page.product_titles()


def test_finish_checkout_single_product(driver):
    inventory_page = login(driver)
    inventory_page.add_product_to_cart(PRODUCT_BACKPACK)
    inventory_page.open_cart()
    cart_page = CartPage(driver)
    cart_page.checkout()
    checkout_page = CheckoutPage(driver)
    checkout_page.continue_checkout("João", "Silva", "12345")
    checkout_page.finish_checkout()
    assert "Thank you for your order!" in checkout_page.completion_text()


def test_finish_checkout_multiple_products(driver):
    inventory_page = login(driver)
    add_products_to_cart(inventory_page, PRODUCT_BACKPACK, PRODUCT_BIKE_LIGHT, PRODUCT_TSHIRT)
    inventory_page.open_cart()
    cart_page = CartPage(driver)
    cart_page.checkout()
    checkout_page = CheckoutPage(driver)
    checkout_page.continue_checkout("João", "Silva", "12345")
    checkout_page.finish_checkout()
    assert "Thank you for your order!" in checkout_page.completion_text()
