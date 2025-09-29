import pytest

from data.user import User
from pages.login_page import LoginPage


@pytest.mark.auth
class TestLogin:
    def test_login_correct(
        self,
        login_page: LoginPage,
        main_user: User
    ):
        product_list_page = login_page.login(main_user)
        product_list_page.check_redirected_to()

    def test_login_incorrect(
        self,
        login_page: LoginPage,
        incorrect_user: User
    ):
        login_page.login(incorrect_user)
        login_page.check_login_unsuccessful()
