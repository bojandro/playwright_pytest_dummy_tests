import pytest

from data.user import User
from pages.login_page import LoginPage


@pytest.mark.shopping_cart
class TestShoppingCart:
    def test_add_to_shopping_cart(
        self,
        login_page: LoginPage,
        main_user: User
    ):
        product_list_page = login_page.login(main_user)

        product_data = product_list_page.add_to_cart_by_index(2)
        product_list_page.check_number_of_items_in_cart(1)
        shopping_cart_page = product_list_page.click_on_shopping_cart_icon()

        shopping_cart_page.check_number_of_products_in_cart(1)
        shopping_cart_page.check_product_is_in_cart(product_data)
