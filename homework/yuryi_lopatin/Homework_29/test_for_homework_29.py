from playwright.sync_api import Page, expect, BrowserContext, Dialog


"""alert accept"""
def test_alert_accept(page: Page):
    def cancel_alert(alert: Dialog):
        print(alert.message)
        print(alert.type)
        alert.accept()

    page.on("dialog", cancel_alert)
    page.goto('https://www.qa-practice.com/elements/alert/confirm#')
    alert = page.get_by_role('link', name='Click')
    alert.click()


"""Работа с tab(ами)"""
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
    print(f"Первая вкладка: кнопка активна")
    new_page.close()  # Закрываем новую вкладку


def test_color_change_full(page: Page):
    print("\n" + "=" * 70)
    page.goto('https://demoqa.com/dynamic-properties')  # Открываем страницу
    print("Страница загружена")
    color_change_btn = page.locator('#colorChange')  # Находим кнопку
    initial_color = color_change_btn.evaluate('el => getComputedStyle(el).color')  # Проверяем начальный цвет
    print(f"Начальный цвет: {initial_color}")
    print("Ждём изменения цвета (5 сек)...")
    page.wait_for_timeout(5500)   # Ждём изменения цвета (происходит через 5 секунд). Ждём чуть больше 5 секунд
    new_color = color_change_btn.evaluate('el => getComputedStyle(el).color')  # Проверяем что цвет изменился
    print(f"Новый цвет: {new_color}")
    assert initial_color != new_color, \
        f"Цвет не изменился! Был и остался: {initial_color}"
    print("Цвет изменился!")
    print("=" * 70 + "\n")
