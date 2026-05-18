from page.locators.common_locators import CommonLocators


class DesignLocators(CommonLocators):

    ADD = '#add_to_cart'  # Локатор для поиска кнопки add to cart
    QUANTITY = '.my_cart_quantity'  # Локатор для проверки значения кол-во товаров в корзине
    PLUS = '.fa-plus'  # Локатор для поиска кнопки +
    MINUS = '.fa-minus'  # Локатор для поиска кнопки -
