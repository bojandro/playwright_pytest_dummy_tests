from __future__ import annotations

from typing import Optional

from playwright.sync_api import Page

from data.product import Product
from pages.base_page import BasePage


class CheckoutPageTwo(BasePage):
    def __init__(self, page: Page):
        self.PAGE_URL = r'https://www.saucedemo.com/v1/checkout-step-two.html'
        super().__init__(page)
        self.checkout_product_list = self.page.locator('.cart_item')

    def check_product_is_in_checkout(self, product: Product):
        for el in self.checkout_product_list.all():
            actual_product_title = el.locator('.inventory_item_name').text_content()
            actual_product_description = el.locator('.inventory_item_desc').text_content()
            actual_product_price = el.locator('.inventory_item_price').text_content()

            if all([
                actual_product_title == product.title,
                actual_product_description == product.description,
                actual_product_price == '$' + product.price
            ]):
                return True
        else:
            raise AssertionError(f"Couldn't find product {product} on the checkout page")

    def click_finish_button(self, expect_success=True) -> Optional[CheckoutCompletePage]:
        finish_button = self.page.get_by_text('FINISH')
        finish_button.click()
        if expect_success:
            from pages.checkout_complete_page import CheckoutCompletePage
            return CheckoutCompletePage(self.page)
        else:
            return None
