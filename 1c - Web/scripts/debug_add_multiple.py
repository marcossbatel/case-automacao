from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless=new')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920,1080')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
try:
    driver.get('https://www.saucedemo.com')
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()
    time.sleep(2)
    for name in ['Sauce Labs Backpack', 'Sauce Labs Fleece Jacket']:
        xp = f"//div[contains(@class,'inventory_item_name') and normalize-space(text())='{name}']/ancestor::div[contains(@class,'inventory_item')]//button"
        print('search', xp)
        els = driver.find_elements(By.XPATH, xp)
        print('found', len(els))
        if els:
            btn = els[0]
            print('button text', btn.text)
            driver.execute_script('arguments[0].scrollIntoView(true);', btn)
            btn.click()
            time.sleep(1)
    print('badge', driver.find_elements(By.CLASS_NAME, 'shopping_cart_badge'))
    badges = driver.find_elements(By.CLASS_NAME, 'shopping_cart_badge')
    print('badge text', badges[0].text if badges else 'none')
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    time.sleep(2)
    items = [e.text for e in driver.find_elements(By.CSS_SELECTOR, '.cart_item .inventory_item_name')]
    print('cart items', items)
finally:
    driver.quit()
