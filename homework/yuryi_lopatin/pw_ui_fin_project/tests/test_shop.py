from page.shop_page import ShopPage
from playwright.sync_api import Page


"""Тест перехода на страницу заказа первого продукта"""
def test_switch_first_product(page: Page):
    shop_click = ShopPage(page)
    shop_click.open()
    shop_click.switch_first_product()


"""Тест перехода на страницу заказа последнего продукта"""
def test_switch_last_product(page: Page):
    shop_click = ShopPage(page)
    shop_click.open()
    shop_click.switch_last_product()


"""тест поиск элементов внутри других элементов"""
def test_last_product(page: Page):
    shop_click = ShopPage(page)
    shop_click.open()
    shop_click.last_product()


"""тест видимости и функциональности кнопки shopping cart на карточке товара"""
def test_visible_shopping_cart_in_product_cart(page: Page):
    shop_click = ShopPage(page)
    shop_click.open()
    shop_click.visible_shopping_cart_in_product_cart()


"""тест перехода на 2 страницу"""
def test_switch_paje_2(page: Page):
    shop_click = ShopPage(page)
    shop_click.open()
    shop_click.action_chain_qa()
