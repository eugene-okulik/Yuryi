import pytest
from page.desk1_page import Desk1Page
from page.desk1_page import (FILTER_NEWEST, FILTER_NAME_AZ, FILTER_PRICE_LOW, FILTER_PRICE_HIGH)
from page.locators.desk_locators import DeskLocators as loc
from playwright.sync_api import Page

# Параметры для фильтров — вместо 4 отдельных тестов
FILTER_PARAMS = [
    (loc.ARRIVALS, FILTER_NEWEST, "Newest Arrivals"),
    (loc.NAMEAZ, FILTER_NAME_AZ, "Name (A-Z)"),
    (loc.LOWTOHIGHT, FILTER_PRICE_LOW, "Price - Low to High"),
    (loc.HIGHTTOLOW, FILTER_PRICE_HIGH, "Price - High to Low"),
]


def test_count_all_product_in_page(page: Page):  # Тест подсчет количества торов на стр
    shop_click = Desk1Page(page)
    shop_click.open()
    shop_click.count_all_product_in_page()


def test_checkbox_steel(page: Page):  # Тест перехода на другую стр с установкой чекбокса на steel - NO WORK!
    shop_click = Desk1Page(page)
    shop_click.open()
    shop_click.checkbox_steel()


def test_filter_products_chainge_page(page: Page):  # Тест перехода на страницу по клику на Products
    shop_click = Desk1Page(page)
    shop_click.open()
    shop_click.filter_products_chainge_page()


@pytest.mark.parametrize("filter_text, expected_url, filter_name", FILTER_PARAMS)
def test_apply_filter(page: Page, filter_text: str, expected_url: str, filter_name: str):  # сортировки 4 теста в одном
    f"""Тест перехода по фильтру {filter_name}"""
    desk = Desk1Page(page)
    desk.open()
    desk.apply_filter(filter_text, expected_url)


def test_click_shopping_cart_on_product_car(page: Page):  # тест функции кнопки shopping cart на карточке товара
    # Цепочка: найти элемент → кликнуть
    shop_click = Desk1Page(page)
    shop_click.open()
    shop_click.click_shopping_cart_on_product_car()


def test_last_product(page: Page):  # тест поиск элементов внутри других элементов
    shop_click = Desk1Page(page)
    shop_click.open()
    shop_click.nested_locators()
