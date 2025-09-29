from __future__ import annotations

from playwright.sync_api import Page

from data.user import User
from pages.base_page import BasePage


class CheckoutPageOne(BasePage):
    def __init__(self, page: Page):
        self.PAGE_URL = r'https://www.saucedemo.com/v1/checkout-step-one.html'
        super().__init__(page)

    def enter_order_information(self, user: User):
        first_name_input = self.page.locator('[placeholder="First Name"]')
        last_name_input = self.page.locator('[placeholder="Last Name"]')
        zip_code_input = self.page.locator('[placeholder="Zip/Postal Code"]')

        first_name_input.fill(user.first_name)
        last_name_input.fill(user.last_name)
        zip_code_input.fill(user.zip_code)

    def click_continue_button(self) -> CheckoutPageTwo:
        continue_button = self.page.locator('[type="submit"]')
        continue_button.click()
        from pages.checkout_page_two import CheckoutPageTwo
        return CheckoutPageTwo(self.page)
