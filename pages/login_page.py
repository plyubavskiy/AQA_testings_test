from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page Object для страницы логина Saucedemo"""

    # Локаторы (все элементы страницы)
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    PRODUCTS_HEADER = (By.CLASS_NAME, "app_logo")
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")

    # URL страницы
    URL = "https://www.saucedemo.com/"

    def open(self):
        """Открыть страницу логина"""
        self.driver.get(self.URL)
        return self  # Возвращаем self для цепочки вызовов

    def enter_username(self, username: str):
        """Ввести логин"""
        self.enter_text(self.USERNAME_INPUT, username)
        return self

    def enter_password(self, password: str):
        """Ввести пароль"""
        self.enter_text(self.PASSWORD_INPUT, password)
        return self

    def click_login_button(self):
        """Нажать кнопку Войти"""
        self.click(self.LOGIN_BUTTON)
        return self

    def login(self, username: str, password: str):
        """
        Полный сценарий логина (цепочка методов)
        Пример: LoginPage(driver).login("user", "pass")
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        return self

    def get_error_message(self) -> str:
        """Получить текст сообщения об ошибке"""
        return self.get_text(self.ERROR_MESSAGE)

    def is_login_successful(self) -> bool:
        """
        Проверить, успешно ли выполнен вход.
        Ищем логотип или заголовок "Products"
        """
        return (self.is_element_visible(self.PRODUCTS_HEADER) or
                self.is_element_visible(self.PRODUCTS_TITLE))

    def get_products_title(self) -> str:
        """Получить заголовок страницы товаров (после логина)"""
        return self.get_text(self.PRODUCTS_TITLE)