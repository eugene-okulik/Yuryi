from page.base_page import BasePage
from playwright.sync_api import expect
from page.locators.design_locators import DesignLocators as loc


class DesignPage(BasePage):
    page_url = '/shop/furn-9999-office-design-software-7?category=9'

    def add_to_cart(self, plus_clicks: int = 0, minus_clicks: int = 0, expected_qty: str = '1'):
        """Универсальный метод добавления в корзину"""
        # Кликаем + нужное количество раз
        for _ in range(plus_clicks):
            self.page.locator(loc.PLUS).click()

        # Кликаем - нужное количество раз
        for _ in range(minus_clicks):
            self.page.locator(loc.MINUS).click()

        # Добавляем в корзину
        self.page.locator(loc.ADD).click()

        # Проверяем количество
        expect(self.page.locator(loc.QUANTITY).first).to_have_text(expected_qty)
        print(f"✅ В корзине товаров: {expected_qty}")
