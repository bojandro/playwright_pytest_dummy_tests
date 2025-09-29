from __future__ import annotations

import logging
from typing import Optional

from playwright.sync_api import Page, expect

from data.user import User
from pages.base_page import BasePage


logger = logging.getLogger(__name__)


class LoginPage(BasePage):
    def __init__(self, page: Page):
        self.PAGE_URL = self.BASE_URL
        super().__init__(page)
        self.navigate()

        self.login_field = self.page.locator('input[data-test="username"]')
        self.password_field = self.page.locator('input[data-test="password"]')
        self.submit_button = self.page.locator('input[type="submit"]')

    def login(self, user: User, expect_success=True) -> Optional[ProductListPage]:
        """
        Goes to ProductListPage
        """
        self.login_field.fill(user.username)
        self.password_field.fill(user.password)
        self.submit_button.click()

        if expect_success:
            from pages.product_list_page import ProductListPage
            return ProductListPage(self.page)
        else:
            return None

    def check_login_unsuccessful(self):
        error_message = 'Epic sadface: Username and password do not match any user in this service'
        expect(self.page.locator('[data-test="error"]')).to_have_text(error_message)
