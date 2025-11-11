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
    chrome_driver.maximize_window()
    yield chrome_driver
    sleep(10)


"Осуществляем проверку введенного текста assert(ом)"
def test_input_text(driver):
    input_data = 'text'
    driver.get('https://www.qa-practice.com/elements/input/simple')  # заходим на стр
    text_string = driver.find_element(By.ID, 'id_text_string')  # указываем что ищем
    text_string.send_keys(input_data)
    text_string.send_keys(Keys.ENTER)
    result_text = driver.find_element(By.ID, 'result-text')
    assert result_text.text == input_data


"""Заполняем форму регистрации"""
def test_inter_in_form(driver):
    input_name = 'Yuri'
    input_last_name = 'Lo'
    user_email = 'uryi.84@mail.ru'
    user_number = '8122128506'
    birth_date = '07 Feb 2000'
    input_subject = 'Hindi'
    input_state = 'NCR'
    input_city = 'Delhi'
    current_address = 'Thailand, Surathani, Ko Samui, Maenam, Soi 5, 22/24'

    wait = WebDriverWait(driver, 10)
    driver.get('https://demoqa.com/automation-practice-form')  # заходим на стр

    text_string = driver.find_element(By.ID, 'firstName')  # указываем что ищем
    text_string.send_keys(input_name)

    text_string = driver.find_element(By.ID, 'lastName')  # указываем что ищем
    text_string.send_keys(input_last_name)

    text_string = driver.find_element(By.ID, 'userEmail')  # указываем что ищем
    text_string.send_keys(user_email)

    gender_label = driver.find_element(By.CSS_SELECTOR, 'label[for="gender-radio-1"]')
    gender_label.click()
    print("✅ Выбрали пол: Male")

    hobbies_label = driver.find_element(By.CSS_SELECTOR, 'label[for="hobbies-checkbox-3"]')
    hobbies_label.click()
    print("✅ Выбрали хобби: Music")

    text_string = driver.find_element(By.ID, 'userNumber')  # указываем что ищем
    text_string.send_keys(user_number)

    text_string = driver.find_element(By.ID, 'dateOfBirthInput')  # указываем что ищем
    text_string.send_keys(birth_date)

    text_string = driver.find_element(By.ID, 'currentAddress')  # указываем что ищем
    text_string.send_keys(current_address)

    state_input = driver.find_element(By.ID, 'subjectsInput')  # указываем что ищем
    state_input.send_keys(input_subject)
    state_input.send_keys(Keys.ENTER)
    print("✅ Выбрали subjects: Hindi")

    state_input = driver.find_element(By.ID, 'react-select-3-input')  # указываем что ищем
    state_input.send_keys(input_state)
    state_input.send_keys(Keys.ENTER)
    print("✅ Выбрали штат: NCR")

    state_input = driver.find_element(By.ID, 'react-select-4-input')  # указываем что ищем
    state_input.send_keys(input_city)
    state_input.send_keys(Keys.ENTER)
    print("✅ Выбрали город: Delhi")

    submit_button = driver.find_element(By.ID, 'submit')  # Отправляем форму
    driver.execute_script("arguments[0].click();", submit_button)

    wait = WebDriverWait(driver, 10)  # Читаем результаты
    modal = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'modal-content')))
    rows = modal.find_elements(By.CSS_SELECTOR, '.table tr')
    print("\nРЕЗУЛЬТАТЫ:")
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, 'td')
        if len(cells) == 2:
            print(f"{cells[0].text:20} | {cells[1].text}")


def test_select_language(driver):
    """Выбор языка и проверка результата"""
    wait = WebDriverWait(driver, 10)
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    select = Select(driver.find_element(By.ID, 'id_choose_language'))  # Выбираем Python
    select.select_by_visible_text('Python')
    driver.find_element(By.ID, 'submit-id-submit').click()  # Отправляем
    result = wait.until(EC.visibility_of_element_located((By.ID, 'result-text')))  # Проверяем
    assert result.text == 'Python'
    print("✅ Тест пройден!")


def test_hello_world(driver):
    """Минимальная версия теста"""
    wait = WebDriverWait(driver, 15)
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    driver.find_element(By.CSS_SELECTOR, '#start button').click()  # Клик
    print("✅ Кликнули Start")
    result = wait.until(EC.visibility_of_element_located((By.ID, 'finish'))) # Ждём результат
    assert result.text.strip() == 'Hello World!'  # Проверка
    print(f"✅ Тест пройден! Текст: {result.text}")
