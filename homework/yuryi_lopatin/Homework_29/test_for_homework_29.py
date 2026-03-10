from playwright.sync_api import Page, expect, BrowserContext, Dialog
import re


def test_alert_accept(page: Page):
    def cancel_alert(alert: Dialog):
        print(alert.message)
        print(alert.type)
        alert.accept()

    page.on("dialog", cancel_alert)
    page.goto('https://www.qa-practice.com/elements/alert/confirm#')
    alert = page.get_by_role('link', name='Click')
    alert.click()


def test_tabs(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    link = page.locator('#new-page-button')
    with context.expect_page() as new_page_event:
        link.click()
    new_page = new_page_event.value
    result = new_page.locator('#result-text')
    expect(result).to_have_text('I am a new page in a new tab')
    print(f"Текс на новой вкладка: {result.inner_text()}")
    expect(link).to_be_enabled()
    print("Первая вкладка: кнопка активна")
    new_page.close()


"""Ждём изменения класса кнопки"""
def test_color_change_wait_class(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    color_btn = page.locator('#colorChange')

    initial_class = color_btn.get_attribute('class')
    print(f"Начальные классы: {initial_class}")  # Проверяем начальные классы

    expect(color_btn).to_have_class(re.compile('text-danger'), timeout=10000)  # Ждём появления класса 'text-danger'

    new_class = color_btn.get_attribute('class')
    print(f"Новые классы: {new_class}")  # Проверяем что класс действительно изменился

    assert 'text-danger' in new_class
    print("Класс изменился!")
