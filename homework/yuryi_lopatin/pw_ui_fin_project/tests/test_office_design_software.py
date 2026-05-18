import pytest
from page.design_page import DesignPage
from playwright.sync_api import Page


# plus_clicks, minus_clicks, expected_qty, описание
CART_PARAMS = [
    (0, 0, '1', 'просто добавить в корзину'),
    (1, 0, '2', 'нажать + и добавить'),
    (1, 1, '1', 'нажать + и - и добавить'),
]


@pytest.mark.parametrize("plus_clicks, minus_clicks, expected_qty, description", CART_PARAMS)
def test_add_to_cart(page: Page, plus_clicks: int, minus_clicks: int,
                     expected_qty: str, description: str):
    f"""Тест добавления в корзину: {description}"""
    design = DesignPage(page)
    design.open()
    design.add_to_cart(plus_clicks, minus_clicks, expected_qty)