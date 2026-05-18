from time import sleep

from playwright.sync_api import expect
from page.locators.desk_locators import DeskLocators as loc
from page.base_page import BasePage


# Константы URL-путей
DESKS_1 = "/shop/category/desks-1"
SHOP = "/shop"
FILTER_STEEL = "/shop/category/desks-1?category=1&search=&order=&attrib=1-1"
FILTER_NEWEST = "/shop?order=create_date+desc&category=1"
FILTER_NAME_AZ = "/shop?order=name+asc&category=1"
FILTER_PRICE_LOW = "/shop?order=list_price+asc&category=1"
FILTER_PRICE_HIGH = "/shop?order=list_price+desc&category=1"
FIRST_PRODUCT = "/shop/customizable-desk-9?category=1#attr=1,3"
LAST_PRODUCT = "/shop/furn-7888-desk-stand-with-screen-21?category=1"


class Desk1Page(BasePage):
    page_url = DESKS_1

    def apply_filter(self, filter_text: str, expected_url: str):
        """Универсальный метод применения фильтра сортировки"""
        self.page.get_by_role(loc.ROLEBTN, name=loc.FEATURED).click()
        self.page.wait_for_timeout(500)
        self.page.get_by_text(filter_text).first.click()
        self.page.wait_for_timeout(2000)
        name_filter_after = self.page.locator(loc.FILTERTEXT).last.inner_text()
        print(f"Название выбранного фильтра: {name_filter_after}")
        expect(self.page).to_have_url(f"{self.base_url}{expected_url}")
        print(f"✅ УСПЕХ, фильтр {name_filter_after} применён\n")

    def count_all_product_in_page(self):
        products = self.page.locator(loc.CART)
        print("=" * 70 + "\n")
        print(f"Всего товаров: {products.count()}")

    def checkbox_steel(self):
        # Цепочка 1: кликнуть на чекбокс
        self.page.locator(loc.CHECKBOXSTEEL).first.click()

        # Проверяем видимость - ЦЕПОЧКА ПРОВЕРОК
        expect(self.page.locator(loc.CHECKBOXSTEEL).first).to_be_visible()
        expect(self.page.locator(loc.CHECKBOXSTEEL).first).not_to_be_empty()
        print("   → Проверки пройдены")
        sleep(3)

        # 5. Проверяем что открылась страница товара Customizable Desk
        # expect(self.page).to_have_url(f"{self.base_url}{FILTER_STEEL}")
        # print(" Кликнули на чекбокс steel - открыли страницу товара Customizable Desk")
        print("=" * 70 + "\n")

    def filter_products_chainge_page(self):
        button = self.page.locator(loc.CARTBTN)
        button.first.click()
        # Проверяем что открылась страница товара
        expect(self.page).to_have_url(f"{self.base_url}{SHOP}")
        print("По клику на products выполнен переход на стр")

    def click_shopping_cart_on_product_car(self):
        # Цепочка: найти элемент → кликнуть
        self.page.locator(loc.CART).first.click()

    def nested_locators(self):
        # Найти блок товаров → внутри найти первый товар → внутри найти кнопку
        shop_section = self.page.locator(loc.PODUCTSGRID)
        last_product = shop_section.locator(loc.CART).last
        buy_button = last_product.locator(loc.BTNPRIMARY)
        buy_button.click()
