from __future__ import annotations

import logging

from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from pages.product_list_page import Product


logger = logging.getLogger(__name__)


class ShoppingCartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.shopping_cart_list = self.page.locator('.cart_list')

    def check_number_of_products_in_cart(self, expected: int):
        expect(self.shopping_cart_list).to_have_count(expected)

    def check_product_is_in_cart(self, product: Product):
        for el in self.shopping_cart_list.all():
            actual_product_title = el.locator('.inventory_item_name').text_content()
            actual_product_description = el.locator('.inventory_item_desc').text_content()
            actual_product_price = el.locator('.inventory_item_price').text_content()

            if all([
                actual_product_title == product.title,
                actual_product_description == product.description,
                actual_product_price == product.price
            ]):
                return True
        else:
            raise AssertionError(f"Couldn't find product {product} in the shopping cart")
