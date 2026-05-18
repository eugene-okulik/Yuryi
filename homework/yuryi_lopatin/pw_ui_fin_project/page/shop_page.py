from page.locators.shop_locators import ShopLocators as loc
from page.base_page import BasePage
from playwright.sync_api import expect


# Константы URL-путей
SHOP = "/shop"
FIRST_PRODUCT = "/shop/customizable-desk-9#attr=1,3"
LAST_PRODUCT = "/shop/e-com09-large-desk-13"
SHOP_PAGE_2 = "/shop/page/2"


class ShopPage(BasePage):
    page_url = '/shop'

    """Тест перехода на страницу заказа первого продукта"""
    def switch_first_product(self):
        products_container = self.page.locator(loc.PODUCTSGRID)  # 1. Находим контейнер товаров
        first_product = products_container.locator(loc.CART).first  # 2. Внутри находим первый товар
        first_product.hover()  # 3. Наводим на товар
        self.page.wait_for_timeout(500)
        product_name = first_product.locator(loc.PODUCTNAME)  # 4. Внутри товара ищем название
        name_text = product_name.inner_text()
        print(f"Товар: {name_text}")
        product_name.click()  # 5. Кликаем на товар
        expect(self.page).to_have_url(f"{self.base_url}/shop/customizable-desk-9#attr=1,3")  # 6. видим открыл стр товар
        print("✅ Цепочка действий выполнена!")
        print(f"✅ Открыли страницу товара {name_text}")
        print("=" * 70 + "\n")


    """Полный тест продукта с hover и цепочками"""
    def switch_last_product(self):
        products = self.page.locator(loc.CART)  # 1. Получаем все товары
        total = products.count()
        print(f"📦 Найдено товаров: {total}")
        last_product = products.last  # 2. Работаем с последним товаром - ЦЕПОЧКА ДЕЙСТВИЙ
        last_product.scroll_into_view_if_needed()  # Прокручиваем до товара
        print("   → Прокрутили к товару")
        last_product.hover()  # Наводим курсор
        print("   → Навели курсор")
        self.page.wait_for_timeout(500)
        product_name_element = last_product.locator(loc.PODUCTNAME)  # Получаем название - ЦЕПОЧКА ЛОКАТОРОВ
        product_name = product_name_element.inner_text()
        print(f"   → Название: {product_name}")
        expect(product_name_element).to_be_visible()  # Проверяем видимость - ЦЕПОЧКА ПРОВЕРОК
        expect(product_name_element).not_to_be_empty()
        print("   → Проверки пройдены")
        product_name_element.click()  # 3. Кликаем на товар
        expect(self.page).to_have_url(f"{self.base_url}/shop/e-com09-large-desk-13")  # 4. видим что открылась стр товар
        print("✅ Цепочка действий выполнена!")
        print(f"✅ Открыли страницу товара {product_name}")
        print("=" * 70 + "\n")


    def last_product(self):
        shop_section = self.page.locator(loc.PODUCTSGRID)  # ищем блок товаров → ищем первый товар → внутри найти кнопку
        last_product = shop_section.locator(loc.CART).last
        buy_button = last_product.locator(loc.BTNPRIMARY)
        buy_button.click()


    def visible_shopping_cart_in_product_cart(self):
        last_product = self.page.locator(loc.CART).last  # Наводим на последний товар
        last_product.hover()
        quick_view_button = last_product.locator(loc.SHOPPINGCART)  # Проверяем что-то появилось или изменилось
        assert quick_view_button.is_visible()
        self.page.wait_for_timeout(500)  # Даём время на анимацию
        print("✅ Навели на товар - теперь видна кнопка quick_view_button")


    def action_chain_qa(self):
        button = self.page.locator(loc.PAGE).first
        # Цепочка действий:
        button.scroll_into_view_if_needed()  # Прокрутить до элемента
        button.hover()  # Навести курсор
        button.wait_for(state='visible')  # Убедиться что видим
        # 6. Кликаем
        button.click()
        # 7. Проверяем что открылась страница 2
        expect(self.page).to_have_url(f"{self.base_url}/shop/page/2")
        print("✅ Выполнен переход на shop/page/2")
