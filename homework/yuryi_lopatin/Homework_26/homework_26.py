from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from time import sleep


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(6)  # Не явное ожидание. Используется редко, может вызывать конфликт с явными ожид.
    chrome_driver.maximize_window()
    yield chrome_driver
    sleep(3)


def test_shop_with_action_chains(driver):
    wait = WebDriverWait(driver, 10)
    driver.get('http://testshop.qa-practice.com/')
    product_link = driver.find_element(By.CSS_SELECTOR, 'a[href="/shop/customizable-desk-9"]')  # ссылка на товар
    # Открываем ссылку в новой вкладке через Ctrl+Click (это то же, что зажать Ctrl и кликнуть)
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL)  # Зажимаем Ctrl
    actions.click(product_link)  # Кликаем по ссылке
    actions.key_up(Keys.CONTROL)  # Отпускаем Ctrl
    actions.perform()  # Выполняем все действия
    print(driver.window_handles)
    tabs = driver.window_handles
    driver.switch_to.window(tabs[-1])  # Переключаемся на новую вкладку (последняя в списке)
    #sleep(3)
    click_button = driver.find_element(By.ID, 'add_to_cart')  # указываем что ищем
    click_button.click()
    continue_button = driver.find_element(By.CLASS_NAME, 'btn-secondary')  # указываем что ищем
    continue_button.click()
    wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'btn-secondary')))  # ✅ ждем пока попап исчезнет
    driver.close()
    driver.switch_to.window(tabs[0])
    driver.find_element(By.CSS_SELECTOR, 'a[href="/shop/cart"]').click()
    product_in_cart = driver.find_element(By.CSS_SELECTOR, 'a[href="/shop/customizable-desk-9#attr=1,3"]').text
    assert 'Customizable Desk' in product_in_cart, f"Ожидали 'Customizable Desk', но получили '{product_in_cart}'"
    print("✅ Тест пройден! Товар успешно добавлен в корзину!")


def test_in_shop2(driver):
    wait = WebDriverWait(driver, 10)
    driver.get('http://testshop.qa-practice.com/')
    print("1. Ищем товар...")
    photo = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/shop/customizable-desk-9"]')))
    print("2. Наводим курсор на товар...")
    actions = ActionChains(driver)
    actions.move_to_element(photo).perform()
    #sleep(3)
    print("3. Ищем иконку корзины...")
    basket = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'o_wsale_product_btn')))
    print("4. Делаем простой клик...", basket)
    basket.click()
    print("✓ Клик выполнен")
    popup = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.modal.show')))
    print("✓ Попап с конфигуратором появился")
    modal_body = popup.find_element(By.CLASS_NAME, 'modal-body')
    modal_text = modal_body.text.lower()
    print(f"Текст в модале:\n{modal_text}")  # Получаем весь текст из модального окна
    # Проверяем наличие ключевых слов товара
    assert "customizable" in modal_text and "desk" in modal_text, "Товар 'Customizable Desk' не найден в попапе!"
    assert "legs" in modal_text, "Секция LEGS не найдена в попапе конфигуратора"  # Проверяем, что товар совпадает
    print("✅ Тест пройден! Товар 'Customizable Desk' найден в попапе конфигуратора")
