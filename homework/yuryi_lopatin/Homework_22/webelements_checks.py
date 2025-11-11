from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import pytest
from time import sleep


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(5)
    chrome_driver.maximize_window()
    yield chrome_driver
    sleep(2)

'''webdriver может делать следующие встроенные проверки
1) element.is_displayed - отображается или нет элемент. Пример проверки assert text_string.is_displayed()
2) element.is_enabled - активен или нет элемент (например радио кнопка). Пример проверки assert text_string.is_enabled()
3) element.is_selected - выбран или нет элемент (например чек бокс). Пример проверки assert text_string.is_selected()'''

"""1) element_is_displayed - отображается или нет элемент"""
def test_displayed(driver):
    input_data = 'text'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.ID, 'id_text_string')
    text_string.send_keys(input_data)
    sleep(3)
    entered_value = text_string.get_attribute('value')
    print(f"✅ Значение в поле: '{text_string.get_attribute('value')}'")
    # Очищаем поле
    #text_string.clear()
    for _ in range(len(entered_value)):
        text_string.send_keys(Keys.BACKSPACE)
    # Проверяем, что поле пустое
    assert text_string.get_attribute('value') == ''
    print("✅ Поле очищено!")
    assert text_string.is_displayed()  # 1) element.is_displayed - проверка покажет, отображается или нет элемент.
    #assert text_string.is_enabled()  # 2) element.is_enabled - активен или нет элемент (например радио кнопка).

'''2) element.is_select и is_enabled - Класс обертка для тега <select> имеет ряд методов для выбора по text, value, № option'''
def test_enabled_and_select2(driver):
    driver.get('https://www.qa-practice.com/elements/button/disabled')  # заходим на стр
    button = driver.find_element(By.NAME, 'submit')  # распечатаем состояние кнопки
    print(button.is_enabled())  # False - т.е. кнопка disabled
    # между принтами найдем веб элемент, сделаем селект веб эл., а после переключения снова распечатаем состояние кнопки
    web_element = driver.find_element(By.ID, 'id_select_state')  # тут находим веб элемент на странице
    dropdown = Select(web_element)  # создаем переменную в которой запускаем класс Select, инициализируем его с веб эл.
    # dropdown.select_by_value('enabled')  # можно искать по visible_text - dropdown.select_by_visible_text('Enabled')
    dropdown.select_by_visible_text('Enabled')  # можно искать по select_by_value - dropdown.select_by_value('enabled')
    print(button.is_enabled())  # True - т.е. кнопка enabled

'''webdriver может делать wait - не явного ожидание (implicitly_wait) появления элемента на стр перед проверкой'''
def test_css_selector_with_get_attribute_dynamic_properties(driver):
    driver.get('https://demoqa.com/dynamic-properties')
    button3 = driver.find_element(By.ID, 'visibleAfter')  # тут ищем по id
    button3.click()  # кнопка появится на стр через 5 сек., отработает хорошо т.к. есть chrome_driver.implicitly_wait(5)

# def test_enabled_and_select(driver):  # моя попытка
#     driver.get('https://www.qa-practice.com/elements/button/disabled')  # заходим на стр
#     button = driver.find_element(By.ID, 'id_select_state')  # указываем что ищем
#     print(button.is_enabled())  # True - т.е. кнопка enabled это странно
#     button.send_keys(Keys.ARROW_DOWN)
#     sleep(2)
#     result_select_element = driver.find_element(By.NAME, 'submit')
#     print(button.is_enabled())  # True - т.е. кнопка enabled
#
# def test_classname_with_get_attribute(driver):
#     input_data = 'text'
#     driver.get('https://www.qa-practice.com/elements/input/simple')  # заходим на стр
#     text_string = driver.find_element(By.ID, 'id_text_string')  # указываем что ищем
#     text_string.send_keys(input_data)
#     text_string.send_keys(Keys.ENTER)
#     result_text= driver.find_element(By.CLASS_NAME, 'result-text')
#     print(result_text.text)  # 1 способ - result_text.text
#     print(result_text.get_attribute('innerText'))  # 2 способ - result_text.text
#     print(f"Количество символов: {len(result_text.text)}")  # ← 1 способ - result_text.text - Количество символов: 4
#     print(f"Количество символов: {len(result_text.get_attribute('innerText'))}")  # ← 2 способ - Количество символов: 4
#     print(f"Ожидаемое количество: {len(input_data)}")
#     # assert result_text.text == input_data  # ← 1 способ - result_text.text
#     assert result_text.get_attribute('innerText') == input_data  # ← 2 способ - нужно добавить sleep(2) после Keys.ENTER
#     # assert result_text.text.strip() == input_data  # ← 1 способ - result_text.text
#     assert result_text.get_attribute('innerText').strip() == input_data  # ← 2 способ - нужно добавить sleep(2)
#
# def test_classname2(driver):
#     input_data = 'text'
#     driver.get('https://www.qa-practice.com/elements/input/simple')  # заходим на стр
#     text_string = driver.find_element(By.CLASS_NAME, 'textinput')  # указываем что ищем
#     text_string.send_keys(input_data)
#     text_string.send_keys(Keys.ENTER)
#     result_text= driver.find_element(By.CLASS_NAME, 'result-text')
#     print(result_text.text)  # 1 способ - result_text.text
#     print(result_text.get_attribute('innerText'))  # 2 способ - result_text.text
#     print(f"Количество символов: {len(result_text.text)}")  # ← 1 способ - result_text.text - Количество символов: 4
#     print(f"Количество символов: {len(result_text.get_attribute('innerText'))}")  # ← 2 способ - Количество символов: 4
#     print(f"Ожидаемое количество: {len(input_data)}")
#     # assert result_text.text == input_data  # ← 1 способ - result_text.text
#     assert result_text.get_attribute('innerText') == input_data  # ← 2 способ - нужно добавить sleep(2) после Keys.ENTER
#     # assert result_text.text.strip() == input_data  # ← 1 способ - result_text.text
#     assert result_text.get_attribute('innerText').strip() == input_data  # ← 2 способ - нужно добавить sleep(2)