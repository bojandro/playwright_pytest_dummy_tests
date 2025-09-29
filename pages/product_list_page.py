from __future__ import annotations

import logging

from playwright.sync_api import Page, expect

from data.product import Product
from pages.base_page import BasePage


logger = logging.getLogger(__name__)


class ProductListPage(BasePage):
    def __init__(self, page: Page):
        self.PAGE_URL = r'https://www.saucedemo.com/v1/inventory.html'
        super().__init__(page)

        self.products = self.page.locator('.inventory_item').all()
        self.shopping_cart_icon = self.page.locator('[data-icon="shopping-cart"]')

    def add_to_cart_by_index(self, index: int) -> Product:
        logger.info(f'Adding item with index={index} to the shopping cart')
        product = self.products[index]
        product_title = product.locator('.inventory_item_name').text_content()
        product_description = product.locator('.inventory_item_desc').text_content()
        product_price = product.locator('.inventory_item_price').text_content().replace('$', '')
        product_data = Product(
            product_title,
            product_description,
            product_price
        )
        add_to_cart_button = product.get_by_text('ADD TO CART')
        add_to_cart_button.click()
        logger.info(f'Added {product_data}, index={index} to the shopping cart')
        return product_data

    def check_number_of_items_in_cart(self, expected: int):
        expect(self.page.locator('.shopping_cart_badge')).to_have_text(str(expected))

    def click_on_shopping_cart_icon(self) -> ShoppingCartPage:
        """
        Goes to ShoppingCartPage
        """
        self.shopping_cart_icon.click()
        from pages.shopping_cart_page import ShoppingCartPage
        return ShoppingCartPage(self.page)
