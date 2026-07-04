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
    elements = driver.find_elements(By.CSS_SELECTOR, '.inventory_item_name')
    print('count names', len(elements))
    for e in elements[:5]:
        print('tag', e.tag_name, 'text', repr(e.text))
        print('outerHTML', e.get_attribute('outerHTML'))
    for name in ['Sauce Labs Backpack', 'Sauce Labs Fleece Jacket']:
        xp = f"//*[@class='inventory_item_name' and normalize-space(text())='{name}']"
        els = driver.find_elements(By.XPATH, xp)
        print('xpath count', xp, len(els))
        if els:
            print('outer', els[0].get_attribute('outerHTML'))
finally:
    driver.quit()
