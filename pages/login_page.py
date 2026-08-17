from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import config


class LoginPage(BasePage):

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    PRODUCTS_HEADER = (By.CLASS_NAME, "app_logo")
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")

    URL = config.URL_SAUCE

    def open(self):
        self.driver.get(self.URL)
        return self

    def enter_username(self, username: str):
        self.enter_text(self.USERNAME_INPUT, username)
        return self

    def enter_password(self, password: str):
        self.enter_text(self.PASSWORD_INPUT, password)
        return self

    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)
        return self

    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        return self

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)

    def is_login_successful(self) -> bool:
        return (self.is_element_visible(self.PRODUCTS_HEADER) or
                self.is_element_visible(self.PRODUCTS_TITLE))

    def get_products_title(self) -> str:
        return self.get_text(self.PRODUCTS_TITLE)