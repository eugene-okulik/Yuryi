from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
from time import sleep


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

"Осуществляем проверку введенного текста assert(ом)"
@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    sleep(1)

def test_id_name(driver):
    input_data = 'text'
    driver.get('https://www.qa-practice.com/elements/input/simple')  # заходим на стр
    text_string = driver.find_element(By.ID, 'id_text_string')  # указываем что ищем
    text_string.send_keys(input_data)
    text_string.send_keys(Keys.ENTER)
    result_text = driver.find_element(By.ID, 'result-text')
    assert result_text.text == input_data

def test_classname_with_id(driver):
    input_data = 'text'
    driver.get('https://www.qa-practice.com/elements/input/simple')  # заходим на стр
    text_string = driver.find_element(By.ID, 'id_text_string')  # указываем что ищем
    text_string.send_keys(input_data)
    text_string.send_keys(Keys.ENTER)
    result_text= driver.find_element(By.CLASS_NAME, 'result-text')
    assert result_text.text == input_data

def test_classname_with_classname(driver):
    input_data = 'text'
    driver.get('https://www.qa-practice.com/elements/input/simple')  # заходим на стр
    text_string = driver.find_element(By.CLASS_NAME, 'textinput')  # указываем что ищем
    text_string.send_keys(input_data)
    text_string.send_keys(Keys.ENTER)
    result_text= driver.find_element(By.CLASS_NAME, 'result-text')
    assert result_text.text == input_data

def test_id_with_classname(driver):
    input_data = 'text'
    driver.get('https://www.qa-practice.com/elements/input/simple')  # заходим на стр
    text_string = driver.find_element(By.CLASS_NAME, 'textinput')  # указываем что ищем
    text_string.send_keys(input_data)
    text_string.send_keys(Keys.ENTER)
    result_text= driver.find_element(By.ID, 'result-text')
    assert result_text.text == input_data

#Все 4 варианта в одном тесте - можно раскомментить закомментированные строки в любом порядке
def test_classname_univers(driver):
    input_data = 'text'
    driver.get('https://www.qa-practice.com/elements/input/simple')  # заходим на стр
    text_string = driver.find_element(By.ID, 'id_text_string')  # указываем что ищем
    #text_string = driver.find_element(By.CLASS_NAME, 'textinput')  # указываем что ищем
    text_string.send_keys(input_data)
    text_string.send_keys(Keys.ENTER)
    #result_text= driver.find_element(By.ID, 'result-text')
    result_text = driver.find_element(By.CLASS_NAME, 'result-text')
    assert result_text.text == input_data

def test_teg(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')  # заходим на стр
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Input field'

def test_link(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    contact_link = driver.find_element(By.LINK_TEXT, 'Contact')  # ищет по полному совпадению
    #contact_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'act')
    # Клик через JavaScript (обходит перекрытия)
    driver.execute_script("arguments[0].click();", contact_link)
    contact_link.click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Contact us'

def test_link2(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    #contact_link = driver.find_element(By.LINK_TEXT, 'Contact')
    contact_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'act')  # ищет по частичному совпадению
    # Клик через JavaScript (обходит перекрытия)
    driver.execute_script("arguments[0].click();", contact_link)
    contact_link.click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Contact us'

def test_css_selector(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.CSS_SELECTOR, '[placeholder = "Submit me"]')  # указываем что ищем
    #text_string = driver.find_element(By.CSS_SELECTOR, '.textinput')  # указываем класснейм и ставим . перед ним
    #text_string = driver.find_element(By.CSS_SELECTOR, '#id_text_string')  # указываем id и ставим # перед ним
    text_string.send_keys('input_data')
    text_string.send_keys(Keys.ENTER)

def test_xpath(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.XPATH,'//*[@placeholder = "Submit me"]')
    #text_string = driver.find_element(By.CSS_SELECTOR, '.textinput')  # указываем класснейм и ставим . перед ним
    #text_string = driver.find_element(By.CSS_SELECTOR, '#id_text_string')  # указываем id и ставим # перед ним
    text_string.send_keys('input_data')
    text_string.send_keys(Keys.ENTER)
