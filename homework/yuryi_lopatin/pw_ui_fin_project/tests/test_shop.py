from page.shop_page import ShopPage
from playwright.sync_api import Page


def test_switch_first_product(page: Page):  # Тест перехода на страницу заказа первого продукта
    shop_click = ShopPage(page)
    shop_click.open()
    shop_click.switch_first_product()


def test_switch_last_product(page: Page):  # Тест перехода на страницу заказа последнего продукта
    shop_click = ShopPage(page)
    shop_click.open()
    shop_click.switch_last_product()


def test_last_product(page: Page):  # тест поиск элементов внутри других элементов
    shop_click = ShopPage(page)
    shop_click.open()
    shop_click.last_product()


def test_visible_shopping_cart_in_product_cart(page: Page):  # тест функции кнопки shopping cart на карточке товара
    shop_click = ShopPage(page)
    shop_click.open()
    shop_click.visible_shopping_cart_in_product_cart()


def test_switch_paje_2(page: Page):  # тест перехода на 2 страницу
    shop_click = ShopPage(page)
    shop_click.open()
    shop_click.action_chain_qa()
