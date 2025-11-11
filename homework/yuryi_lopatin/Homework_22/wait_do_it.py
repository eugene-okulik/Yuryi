from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from time import sleep


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    # chrome_driver.implicitly_wait(5)  # не явное ожидание 5 секунд, вместо sleep
    chrome_driver.maximize_window()
    yield chrome_driver  # лучше использовать yield
    chrome_driver.quit()  # закрываем браузер после теста


"Работает с не явным ожиданием не работает из-за ошибки ElementClickInterceptedException - рекламный баннер (iframe)"
def test_5_sec(driver):
    driver.get('https://demoqa.com/dynamic-properties')
    button3 = driver.find_element(By.ID, 'visibleAfter')
    button3.click()

"Работает с явным ожиданием не работает из-за ошибки ElementClickInterceptedException - рекламный баннер (iframe)"
def test_5_sec2(driver):
    driver.get('https://demoqa.com/dynamic-properties')
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'visibleAfter')))
    button3 = driver.find_element(By.ID, 'visibleAfter')
    button3.click()

'''тест явного ожидания (wait).
Для добавления вещи в корзину нужно сперва кликнуть на сайз. потом на цветом, потом подождать когда добавится'''
def test_test_cart(driver):
    driver.get('http://testshop.qa-practice.com/shop/warranty-33')
    wait = WebDriverWait(driver, 10)
    button_add_one = driver.find_element(By.CSS_SELECTOR, '.fa-plus')  # добавляем один элемент
    button_add_one.click()
    button_add_to_cart = driver.find_element(By.ID, 'add_to_cart')  # указали кнопку добавить в корзину
    button_add_to_cart.click()
    # Ждем обновления корзины
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.my_cart_quantity'), '2'))
    cart_quantity = driver.find_element(By.CSS_SELECTOR, '.my_cart_quantity')
    print(f"✅ Товары добавлены! Количество: {cart_quantity.text}")

    assert cart_quantity.text == '2'
    print(driver.get_cookies())
