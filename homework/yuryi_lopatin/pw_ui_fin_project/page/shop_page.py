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
        #1. Находим контейнер товаров
        products_container = self.page.locator(loc.PODUCTSGRID)

        # 2. Внутри находим первый товар
        first_product = products_container.locator(loc.CART).first

        # 3. Наводим на товар
        first_product.hover()
        self.page.wait_for_timeout(500)

        # 4. Внутри товара ищем название
        product_name = first_product.locator(loc.PODUCTNAME)
        name_text = product_name.inner_text()
        print(f"Товар: {name_text}")

        # 5. Кликаем на товар
        product_name.click()
        # 6. Проверяем что открылась страница товара
        expect(self.page).to_have_url(f"{self.base_url}/shop/customizable-desk-9#attr=1,3")
        print("✅ Цепочка действий выполнена!")
        print(f"✅ Открыли страницу товара {name_text}")
        print("=" * 70 + "\n")


    """Полный тест продукта с hover и цепочками"""
    def switch_last_product(self):
        # 1. Получаем все товары
        products = self.page.locator(loc.CART)
        total = products.count()
        print(f"📦 Найдено товаров: {total}")

        # 2. Работаем с последним товаром - ЦЕПОЧКА ДЕЙСТВИЙ
        last_product = products.last

        # Прокручиваем до товара
        last_product.scroll_into_view_if_needed()
        print("   → Прокрутили к товару")

        # Наводим курсор
        last_product.hover()
        print("   → Навели курсор")
        self.page.wait_for_timeout(500)

        # Получаем название - ЦЕПОЧКА ЛОКАТОРОВ
        product_name_element = last_product.locator(loc.PODUCTNAME)
        product_name = product_name_element.inner_text()
        print(f"   → Название: {product_name}")

        # Проверяем видимость - ЦЕПОЧКА ПРОВЕРОК
        expect(product_name_element).to_be_visible()
        expect(product_name_element).not_to_be_empty()
        print("   → Проверки пройдены")

        # 3. Кликаем на товар
        product_name_element.click()

        # 4. Проверяем что открылась страница товара
        expect(self.page).to_have_url(
            f"{self.base_url}/shop/e-com09-large-desk-13")
        print("✅ Цепочка действий выполнена!")
        print(f"✅ Открыли страницу товара {product_name}")
        print("=" * 70 + "\n")


    def last_product(self):
        # Найти блок товаров → внутри найти первый товар → внутри найти кнопку
        shop_section = self.page.locator(loc.PODUCTSGRID)
        last_product = shop_section.locator(loc.CART).last
        buy_button = last_product.locator(loc.BTNPRIMARY)
        buy_button.click()


    def visible_shopping_cart_in_product_cart(self):
        # Наводим на последний товар
        last_product = self.page.locator(loc.CART).last
        last_product.hover()

        # Проверяем что-то появилось или изменилось, например, теперь видна кнопка quick_view_button
        quick_view_button = last_product.locator(loc.SHOPPINGCART)
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
