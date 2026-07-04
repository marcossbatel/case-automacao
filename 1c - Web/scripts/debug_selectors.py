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
    names = [e.text for e in driver.find_elements(By.CSS_SELECTOR, '.inventory_item_name')]
    print('names', names[:5])
    xp = "//div[@class='inventory_item_name' and normalize-space(text())='Sauce Labs Backpack']/ancestor::div[contains(@class,'inventory_item')]//button"
    els = driver.find_elements(By.XPATH, xp)
    print('count xp', len(els))
    for e in els:
        print('button text', e.text, e.get_attribute('outerHTML'))
    xp2 = "//div[@class='inventory_item_name' and normalize-space(text())='Sauce Labs Backpack']"
    print('count xp2', len(driver.find_elements(By.XPATH, xp2)))
    xp3 = "//div[contains(@class,'inventory_item')]//div[@class='inventory_item_name']"
    print('count xp3', len(driver.find_elements(By.XPATH, xp3)))
finally:
    driver.quit()
