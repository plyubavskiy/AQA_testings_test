import pytest
from pages.login_page import LoginPage


class TestSaucedemoLogin:

    def test_valid_login(self, browser):
        login_page = LoginPage(browser)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        assert login_page.is_login_successful(), "Логин не удался: логотип не появился"

        title = login_page.get_products_title()
        assert "Products" in title, f"Ожидался заголовок 'Products', а получили '{title}'"

    def test_invalid_login(self, browser):
        login_page = LoginPage(browser)
        login_page.open()
        login_page.login("wrong_user", "wrong_password")

        error_text = login_page.get_error_message()
        expected_error = "Username and password do not match"

        assert expected_error in error_text, \
            f"Ожидалась ошибка '{expected_error}', а получили '{error_text}'"

    def test_empty_login(self, browser):
        login_page = LoginPage(browser)
        login_page.open()
        login_page.click_login_button()

        error_text = login_page.get_error_message()
        expected_error = "Username is required"

        assert expected_error in error_text, \
            f"Ожидалась ошибка '{expected_error}', а получили '{error_text}'"

    def test_locked_user(self, browser):
        login_page = LoginPage(browser)
        login_page.open()
        login_page.login("locked_out_user", "secret_sauce")

        error_text = login_page.get_error_message()
        expected_error = "Sorry, this user has been locked out"

        assert expected_error in error_text, \
            f"Ожидалась ошибка '{expected_error}', а получили '{error_text}'"
