from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def test_google_title(browser):
    """
    Тест: поиск в Google с обходом блокировок.
    Используем улучшенные настройки драйвера.
    """
    # Открываем Google
    browser.get("https://www.google.com")

    # Ждем загрузки страницы
    time.sleep(2)

    # Проверяем заголовок
    assert "Google" in browser.title, f"Ожидалось 'Google', а получили '{browser.title}'"

    # Ищем поле поиска
    search_box = browser.find_element(By.NAME, "q")

    # Убеждаемся, что поле видимо и активно
    browser.execute_script("arguments[0].scrollIntoView(true);", search_box)
    time.sleep(0.5)

    # Очищаем и вводим текст
    search_box.clear()
    search_box.send_keys("Selenium Python")
    search_box.send_keys(Keys.RETURN)

    # Ждем загрузки результатов
    time.sleep(3)

    # Проверяем, что поиск сработал
    assert "Selenium" in browser.title, f"Ожидалось 'Selenium' в заголовке, а получили '{browser.title}'"

    print("✅ Тест Google пройден!")