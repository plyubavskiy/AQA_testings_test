from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from typing import Union, Tuple


class BasePage:
    """Базовый класс для всех Page Object классов"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # таймаут 10 секунд

    def find_element(self, locator: Tuple[By, str], timeout: int = 10) -> WebElement:
        """Найти элемент с ожиданием его появления"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator: Tuple[By, str], timeout: int = 10) -> None:
        """Кликнуть по элементу с ожиданием его кликабельности"""
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def enter_text(self, locator: Tuple[By, str], text: str, timeout: int = 10) -> None:
        """Ввести текст в поле с предварительной очисткой"""
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: Tuple[By, str], timeout: int = 10) -> str:
        """Получить текст элемента"""
        return self.find_element(locator, timeout).text

    def is_element_visible(self, locator: Tuple[By, str], timeout: int = 10) -> bool:
        """Проверить, виден ли элемент"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except:
            return False