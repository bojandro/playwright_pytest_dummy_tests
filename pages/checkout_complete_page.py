from __future__ import annotations

from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    def __init__(self, page: Page):
        self.PAGE_URL = r'https://www.saucedemo.com/v1/checkout-complete.html'
        super().__init__(page)

    def check_order_successful(self):
        expected_elements = {
            'complete-header': 'THANK YOU FOR YOUR ORDER',
            'complete-text': 'Your order has been dispatched, and will arrive just as fast as the pony can get there'
        }
        for locator, text in expected_elements.items():
            expect(self.page.locator(locator).get_by_text(text))
