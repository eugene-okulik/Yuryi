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

'''webdriver может делать следующие действия с найденным еллементом
1) element.get_attribute('value-значение') - получает значение атрибута (в примере проверяем что написано в плейсхолдер)
2) element.value_of_css_property(font-size) - получает значение его css настроек (цвет, цвет бэкграунд и др.)
3) element.tag_name - получает название его тега (пригодится если не работает result_text.text, c get.attribute найдет)
4) element.clear() - очищает поле ввода (работает не всегда, там где не работает, нужно ввести 20 бэкспэйсов
Далее рассмотрим в коде:'''

'''1) element.get_attribute('value') - получаем значение атрибута (в этом тесте проверим что написано в плейсхолдер)
иногда, если сделать print(result_text.text - значение не отдает, а если использовать:
print(result_text.get_attribute(innerText) - значение отдает, нужно помнить и знать оба способа, рассмотрим второй'''
# был просто с result_text.text, но он не всегда срабатывает см. начало файла search_in_qu_practice.py
def test_id_name(driver):
    input_data = 'text'
    driver.get('https://www.qa-practice.com/elements/input/simple')  # заходим на стр
    text_string = driver.find_element(By.ID, 'id_text_string')  # указываем что ищем
    text_string.send_keys(input_data)
    text_string.send_keys(Keys.ENTER)
    result_text = driver.find_element(By.ID, 'result-text')
    assert result_text.text == input_data  # тут используем result_text.text, а не get_attribute, но работает не всегда

# далее примеры с get_attribute
def test_css_selector_with_get_attribute(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.CSS_SELECTOR, '[placeholder = "Submit me"]')  # указываем что ищем
    #text_string = driver.find_element(By.CSS_SELECTOR, '.textinput')  # указываем класснейм и ставим . перед ним
    #text_string = driver.find_element(By.CSS_SELECTOR, '#id_text_string')  # указываем id и ставим # перед ним
    assert text_string.get_attribute('placeholder') == 'Submit me'

def test_xpath_with_get_attribute(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.XPATH,'//*[@placeholder = "Submit me"]')
    #text_string = driver.find_element(By.CSS_SELECTOR, '.textinput')  # указываем класснейм и ставим . перед ним
    #text_string = driver.find_element(By.CSS_SELECTOR, '#id_text_string')  # указываем id и ставим # перед ним
    assert text_string.get_attribute('placeholder') == 'Submit me'

'''1.1) element.get.attribute('innerText') = element.text - проверим текст у элемента Text string после ввода
В 'innerText' мы получим атрибут, которого визуально на странице нет, но введенный текст из него получить можно'''
def test_id_name_with_get_attribute(driver):
    input_data = 'text'
    driver.get('https://www.qa-practice.com/elements/input/simple')  # заходим на стр
    text_string = driver.find_element(By.ID, 'id_text_string')  # указываем что ищем
    text_string.send_keys(input_data)
    assert text_string.get_attribute('value') == input_data

'''1.1) element.get.attribute('innerText') = element.text - проверим текст у элемента Text string после ввода и ентер'''
def test_click_enter_in_id_name_with_get_attribute(driver):
    input_data = 'text'
    driver.get('https://www.qa-practice.com/elements/input/simple')  # заходим на стр
    text_string = driver.find_element(By.ID, 'id_text_string')  # указываем что ищем
    text_string.send_keys(input_data)
    text_string.send_keys(Keys.ENTER)
    result_text = driver.find_element(By.ID, 'result-text')
    assert result_text.get_attribute('innerText') == input_data

'''1.2 подсчитаем символы'''
def test_id_name_with_get_attribute2(driver):
    input_data = 'text'
    driver.get('https://www.qa-practice.com/elements/input/simple')  # заходим на стр
    text_string = driver.find_element(By.ID, 'id_text_string')  # указываем что ищем
    text_string.send_keys(input_data)
    text_string.send_keys(Keys.ENTER)
    sleep(2)
    result_text= driver.find_element(By.ID, 'result-text')
    print(result_text.text)  # 1 способ - result_text.text
    print(result_text.get_attribute('innerText'))  # 2 способ - result_text.text
    print(f"Количество символов: {len(result_text.text)}")  # ← 1 способ - result_text.text - Количество символов: 4
    print(f"Количество символов: {len(result_text.get_attribute('innerText'))}")  # ← 2 способ - Количество символов: 4
    print(f"Ожидаемое количество: {len(input_data)}")
    #assert result_text.text == input_data  # ← 1 способ - result_text.text
    assert result_text.get_attribute('innerText') == input_data  # ← 2 способ - нужно добавить sleep(2) после Keys.ENTER
    #assert result_text.text.strip() == input_data  # ← 1 способ - result_text.text
    assert result_text.get_attribute('innerText').strip() == input_data  # ← 2 способ - нужно добавить sleep(2)

def test_classname_with_get_attribute(driver):
    input_data = 'text'
    driver.get('https://www.qa-practice.com/elements/input/simple')  # заходим на стр
    text_string = driver.find_element(By.ID, 'id_text_string')  # указываем что ищем
    text_string.send_keys(input_data)
    text_string.send_keys(Keys.ENTER)
    result_text= driver.find_element(By.CLASS_NAME, 'result-text')
    print(result_text.text)  # 1 способ - result_text.text
    print(result_text.get_attribute('innerText'))  # 2 способ - result_text.text
    print(f"Количество символов: {len(result_text.text)}")  # ← 1 способ - result_text.text - Количество символов: 4
    print(f"Количество символов: {len(result_text.get_attribute('innerText'))}")  # ← 2 способ - Количество символов: 4
    print(f"Ожидаемое количество: {len(input_data)}")
    # assert result_text.text == input_data  # ← 1 способ - result_text.text
    assert result_text.get_attribute('innerText') == input_data  # ← 2 способ - нужно добавить sleep(2) после Keys.ENTER
    # assert result_text.text.strip() == input_data  # ← 1 способ - result_text.text
    assert result_text.get_attribute('innerText').strip() == input_data  # ← 2 способ - нужно добавить sleep(2)

def test_classname2(driver):
    input_data = 'text'
    driver.get('https://www.qa-practice.com/elements/input/simple')  # заходим на стр
    text_string = driver.find_element(By.CLASS_NAME, 'textinput')  # указываем что ищем
    text_string.send_keys(input_data)
    text_string.send_keys(Keys.ENTER)
    result_text = driver.find_element(By.CLASS_NAME, 'result-text')
    print(result_text.text)  # 1 способ - result_text.text
    print(result_text.get_attribute('innerText'))  # 2 способ - result_text.text
    print(f"Количество символов: {len(result_text.text)}")  # ← 1 способ - result_text.text - Количество символов: 4
    print(f"Количество символов: {len(result_text.get_attribute('innerText'))}")  # ← 2 способ - Количество символов: 4
    print(f"Ожидаемое количество: {len(input_data)}")
    # assert result_text.text == input_data  # ← 1 способ - result_text.text
    assert result_text.get_attribute('innerText') == input_data  # ← 2 способ - нужно добавить sleep(2) после Keys.ENTER
    # assert result_text.text.strip() == input_data  # ← 1 способ - result_text.text
    assert result_text.get_attribute('innerText').strip() == input_data  # ← 2 способ - нужно добавить sleep(2)

'''2) element.element.value_of_css_property('font_size') - получает значение css настроек (цвет, цвет бэкграунд и др)'''
def test_css_selector_value_of_css_property(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.CSS_SELECTOR, '[placeholder = "Submit me"]')  # указываем что ищем
    #text_string = driver.find_element(By.CSS_SELECTOR, '.textinput')  # указываем класснейм и ставим . перед ним
    #text_string = driver.find_element(By.CSS_SELECTOR, '#id_text_string')  # указываем id и ставим # перед ним
    print(text_string.value_of_css_property('border-color')) #test_css_selector_value_of_css_property rgb(206, 212, 218)

def test_xpath_value_of_css_property(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.XPATH,'//*[@placeholder = "Submit me"]')
    #text_string = driver.find_element(By.CSS_SELECTOR, '.textinput')  # указываем класснейм и ставим . перед ним
    #text_string = driver.find_element(By.CSS_SELECTOR, '#id_text_string')  # указываем id и ставим # перед ним
    print(text_string.value_of_css_property('border-color')) #test_xpath_value_of_css_property PASSED rgb(206, 212, 218)

'''3) element clear - удалит ранее введенный в поле текст, если не работает нужно 20 раз ввести бэкспэйс'''
# Простой вариант теста без доп проверок
def test_clear_by_id(driver):
    input_data = 'text'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.ID, 'id_text_string')
    text_string.send_keys(input_data)
    # Посмотрим на ввод
    sleep(3)
    # Очищаем поле
    text_string.clear()

def test_clear_by_name(driver):
    input_data = 'text'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.NAME, 'text_string')
    text_string.send_keys(input_data)
    # Посмотрим на ввод
    sleep(3)
    # Очищаем поле
    text_string.clear()

# Красивый вариант теста с проверками
def test_clear_with_id(driver):
    input_data = 'text'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.ID, 'id_text_string')
    text_string.send_keys(input_data)
    # Проверяем значение в поле ввода
    assert text_string.get_attribute('value') == input_data
    sleep(3)
    print(f"✅ Значение в поле: '{text_string.get_attribute('value')}'")
    # Очищаем поле
    text_string.clear()
    # Проверяем, что поле пустое
    assert text_string.get_attribute('value') == ''
    print("✅ Поле очищено!")

def test_clear_with_name(driver):
    input_data = 'text'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.NAME, 'text_string')
    text_string.send_keys(input_data)
    # Проверяем значение в поле ввода
    assert text_string.get_attribute('value') == input_data
    sleep(3)
    print(f"✅ Значение в поле: '{text_string.get_attribute('value')}'")
    # Очищаем поле
    text_string.clear()
    # Проверяем, что поле пустое
    assert text_string.get_attribute('value') == ''
    print("✅ Поле очищено!")

'''3.1) element clear -работает не всегда, если не работает нужно 20 раз ввести бэкспэйс'''
# Простой вариант теста без доп проверок
def test_clear_by_id_with_backspace(driver):
    input_data = 'text'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.ID, 'id_text_string')
    text_string.send_keys(input_data)
    # Посмотрим на ввод
    sleep(3)
    # Очищаем поле
    #text_string.clear()
    for _ in range(20):
        text_string.send_keys(Keys.BACKSPACE)

def test_clear_by_name_with_backspace(driver):
    input_data = 'text'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.NAME, 'text_string')
    text_string.send_keys(input_data)
    # Посмотрим на ввод
    sleep(3)
    # Очищаем поле
    #text_string.clear()
    for _ in range(20):
        text_string.send_keys(Keys.BACKSPACE)

# Красивый вариант теста с проверками
def test_clear_to_id_with_backspace(driver):
    input_data = 'text'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.ID, 'id_text_string')
    text_string.send_keys(input_data)
    # Проверяем значение в поле ввода
    assert text_string.get_attribute('value') == input_data
    sleep(3)
    print(f"✅ Значение в поле: '{text_string.get_attribute('value')}'")
    # Очищаем поле
    #text_string.clear()
    for _ in range(20):
        text_string.send_keys(Keys.BACKSPACE)
    # Проверяем, что поле пустое
    assert text_string.get_attribute('value') == ''
    print("✅ Поле очищено!")

def test_clear_to_name_with_backspace(driver):
    input_data = 'text'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.NAME, 'text_string')
    text_string.send_keys(input_data)
    # Проверяем значение в поле ввода
    assert text_string.get_attribute('value') == input_data
    sleep(3)
    print(f"✅ Значение в поле: '{text_string.get_attribute('value')}'")
    # Очищаем поле
    #text_string.clear()
    for _ in range(20):
        text_string.send_keys(Keys.BACKSPACE)
    # Проверяем, что поле пустое
    assert text_string.get_attribute('value') == ''
    print("✅ Поле очищено!")

'''3.2) Ранее вводили на абум 20 бэкспейсов, а что если текст короче, или длиннее, как подсчитать кол-во символов.
как и с элементом element.get.attribute('innerText') мы можем получить атрибут, которого визуально на странице нет, 
но введенный текст из него получить можно'''

# Простой вариант теста без доп проверок
def test_clear_by_id_with_backspace2(driver):
    input_data = 'text'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.ID, 'id_text_string')
    text_string.send_keys(input_data)
    # Посмотрим на ввод
    sleep(2)
    len_simbol = len(text_string .get_attribute('value'))  # ← 2 способ - Количество символов
    # Посмотрим на ввод
    print(f'кол-во символов {len_simbol}')
    # Очищаем поле
    #text_string.clear()
    for _ in range(len_simbol):
        text_string.send_keys(Keys.BACKSPACE)
    # Проверяем, что поле пустое
    assert text_string.get_attribute('value') == ''
    print("✅ Поле очищено!")

def test_clear_by_name_with_backspace2(driver):
    input_data = 'text'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.NAME, 'text_string')
    text_string.send_keys(input_data)
    len_simbol = len(text_string.get_attribute('value'))  # ← 2 способ - Количество символов
    # Посмотрим на ввод
    print(f'кол-во символов {len_simbol}')
    sleep(3)
    # Очищаем поле
    # text_string.clear()
    for _ in range(len_simbol):
        text_string.send_keys(Keys.BACKSPACE)
    # Проверяем, что поле пустое
    assert text_string.get_attribute('value') == ''
    print("✅ Поле очищено!")

# Красивый вариант теста с проверками
def test_clear_to_id_with_backspace3(driver):
    input_data = 'text'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.ID, 'id_text_string')
    text_string.send_keys(input_data)
    # Проверяем значение в поле ввода
    assert text_string.get_attribute('value') == input_data
    sleep(3)
    len_simbol = len(text_string.get_attribute('value'))  # ← 2 способ - Количество символов
    # Посмотрим на ввод
    print(f'кол-во символов {len_simbol}')
    # Очищаем поле
    #text_string.clear()
    for _ in range(len_simbol):
        text_string.send_keys(Keys.BACKSPACE)
    # Проверяем, что поле пустое
    assert text_string.get_attribute('value') == ''
    print("✅ Поле очищено!")

def test_clear_to_name_with_backspace3(driver):
    input_data = 'text'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.NAME, 'text_string')
    text_string.send_keys(input_data)
    # Проверяем значение в поле ввода
    assert text_string.get_attribute('value') == input_data
    sleep(3)
    len_simbol = len(text_string.get_attribute('value'))  # ← 2 способ - Количество символов
    # Посмотрим на ввод
    print(f'кол-во символов {len_simbol}')
    # Очищаем поле
    #text_string.clear()
    for _ in range(len_simbol):
        text_string.send_keys(Keys.BACKSPACE)
    # Проверяем, что поле пустое
    assert text_string.get_attribute('value') == ''
    print("✅ Поле очищено!")

'''Альтернативный вариант (более простой) - Используем длину исходных данных:'''
def test_clear_by_id_with_backspace4(driver):
    input_data = 'text'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.ID, 'id_text_string')
    text_string.send_keys(input_data)
    sleep(1)
    # Очищаем через length напрямую
    #text_string.clear()
    for _ in range(len(input_data)):  # Используем длину исходных данных
        text_string.send_keys(Keys.BACKSPACE)
    assert text_string.get_attribute('value') == ''
    print("✅ Поле очищено!")

'''Альтернативный вариант (более простой) - Используем длину исходных данных:'''
def test_clear_by_name_with_backspace4(driver):
    input_data = 'text'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.NAME, 'text_string')
    text_string.send_keys(input_data)
    sleep(1)
    # Очищаем через length напрямую
    #text_string.clear()
    for _ in range(len(input_data)):  # Используем длину исходных данных
        text_string.send_keys(Keys.BACKSPACE)
    assert text_string.get_attribute('value') == ''
    print("✅ Поле очищено!")

#Способ очистки как в уроке!!!
def test_clear_to_id_with_backspace5(driver):
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

def test_clear_to_name_with_backspace5(driver):
    input_data = 'text'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.NAME, 'text_string')
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

#Тот же способ, но с дополнительной проверкой
def test_clear_to_id_with_backspace6(driver):
    input_data = 'text'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.ID, 'id_text_string')
    text_string.send_keys(input_data)
    sleep(3)
    entered_value = text_string.get_attribute('value')
    # Проверяем, что значение введено правильно
    assert entered_value == input_data
    print(f"✅ Значение в поле: '{entered_value}'")
    # Очищаем поле
    #text_string.clear()
    for _ in range(len(entered_value)):
        text_string.send_keys(Keys.BACKSPACE)
    # Проверяем, что поле пустое
    assert text_string.get_attribute('value') == ''
    print("✅ Поле очищено!")

def test_clear_to_name_with_backspace6(driver):
    input_data = 'text'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.NAME, 'text_string')
    text_string.send_keys(input_data)
    sleep(3)
    entered_value = text_string.get_attribute('value')
    # Проверяем, что значение введено правильно
    assert entered_value == input_data
    print(f"✅ Значение в поле: '{entered_value}'")
    # Очищаем поле
    #text_string.clear()
    for _ in range(len(entered_value)):
        text_string.send_keys(Keys.BACKSPACE)
    # Проверяем, что поле пустое
    assert text_string.get_attribute('value') == ''
    print("✅ Поле очищено!")

'''webdriver может делать следующие встроенные проверки
1) element.is_displayed - отображается или нет элемент. Пример проверки assert text_string.is_displayed()
2) element.is_enabled - активен или нет элемент (например радио кнопка). Пример проверки assert text_string.is_enabled()
3) element.is_selected - выбран или нет элемент (например чек бокс). Пример проверки assert text_string.is_selected()'''

"""1) element_is_displayed - отображается или нет элемент"""
def test_clear_to_id_with_backspace5(driver):
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
    assert text_string.is_displayed()  # 1) element.is_displayed - отображается или нет элемент.
    #assert text_string.is_enabled()  # 2) element.is_enabled - активен или нет элемент (например радио кнопка).

'''2) element.is_select и is_enabled - Класс обертка для тега <select> с методами для выбора по text, value, № option'''
def test_enabled_and_select2(driver):
    driver.get('https://www.qa-practice.com/elements/button/disabled')  # заходим на стр
    button = driver.find_element(By.NAME, 'submit')  # распечатаем состояние кнопки
    print(button.is_enabled())  # False - т.е. кнопка disabled
    # между принтами найдем веб элемент, сделаем селект веб эл., а после переключения снова распечатаем состояние кнопки
    web_element = driver.find_element(By.ID, 'id_select_state')  # тут находим веб элемент на странице
    dropdown = Select(web_element)  # создаем переменную в которой запускаем класс Select, инициализируем его с веб эл.
    # dropdown.select_by_value('enabled')  # можно искать по select_by_value - dropdown.select_by_value('enabled')
    dropdown.select_by_visible_text('Enabled') # или искать по visible_text - dropdown.select_by_visible_text('Enabled')
    print(button.is_enabled())  # True - т.е. кнопка enabled

'''webdriver может делать wait - не явного ожидание (implicitly_wait) появления элемента на стр перед проверкой'''
def test_css_selector_with_get_attribute_dynamic_properties(driver):
    driver.get('https://demoqa.com/dynamic-properties')
    button3 = driver.find_element(By.ID, 'visibleAfter')  # тут ищем по id
    button3.click()  # кнопка появится на стр через 5 сек., отработает хорошо т.к. есть chrome_driver.implicitly_wait(5)

# "Обращаемся к ID и NAME и вызываем submit"
# driver = webdriver.Chrome()
# driver.get('https://www.qa-practice.com/elements/input/simple')  # заходим на стр
# text_string = driver.find_element(By.ID, 'id_text_string')  # указываем что ищем
# text_string.send_keys('text')
# text_string.submit()
# sleep(2)
#
# driver = webdriver.Chrome()
# driver.get('https://www.qa-practice.com/elements/input/simple')  # заходим на стр
# text_string = driver.find_element(By.NAME, 'text_string')  # указываем что ищем
# text_string.send_keys('text')
# text_string.submit()
# sleep(2)
#
# "Обращаемся к ID и NAME и жмем кнопку ENTER"
# driver = webdriver.Chrome()
# driver.get('https://www.qa-practice.com/elements/input/simple')  # заходим на стр
# text_string = driver.find_element(By.ID, 'id_text_string')  # указываем что ищем
# text_string.send_keys('text')
# text_string.send_keys(Keys.ENTER)
# sleep(2)
#
# driver = webdriver.Chrome()
# driver.get('https://www.qa-practice.com/elements/input/simple')  # заходим на стр
# text_string = driver.find_element(By.NAME, 'text_string')  # указываем что ищем
# text_string.send_keys('text')
# text_string.send_keys(Keys.ENTER)
# sleep(2)

# def test_teg(driver):
#     driver.get('https://www.qa-practice.com/elements/input/simple')  # заходим на стр
#     assert driver.find_element(By.TAG_NAME, 'h1').text == 'Input field'
#
# def test_link(driver):
#     driver.get('https://www.qa-practice.com/elements/input/simple')
#     contact_link = driver.find_element(By.LINK_TEXT, 'Contact')  # ищет по полному совпадению
#     #contact_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'act')
#     # Клик через JavaScript (обходит перекрытия)
#     driver.execute_script("arguments[0].click();", contact_link)
#     contact_link.click()
#     assert driver.find_element(By.TAG_NAME, 'h1').text == 'Contact us'
#
# def test_link2(driver):
#     driver.get('https://www.qa-practice.com/elements/input/simple')
#     #contact_link = driver.find_element(By.LINK_TEXT, 'Contact')
#     contact_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'act')  # ищет по частичному совпадению
#     # Клик через JavaScript (обходит перекрытия)
#     driver.execute_script("arguments[0].click();", contact_link)
#     contact_link.click()
#     assert driver.find_element(By.TAG_NAME, 'h1').text == 'Contact us'