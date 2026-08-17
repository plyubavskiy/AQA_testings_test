import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    """
    Фикстура, которая создает драйвер с настройками для обхода блокировок.
    """
    # Настройки Chrome
    chrome_options = Options()

    # === Базовые настройки для обхода блокировок ===
    # Отключаем уведомления
    chrome_options.add_argument("--disable-notifications")
    # Отключаем автоматизацию (скрываем, что это Selenium)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    # Убираем сообщение "Chrome управляется автоматическим ПО"
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    # === Дополнительные аргументы для стабильности ===
    chrome_options.add_argument("--disable-gpu")  # Отключаем GPU (ускоряет)
    chrome_options.add_argument("--no-sandbox")  # Убираем песочницу (для стабильности)
    chrome_options.add_argument("--disable-dev-shm-usage")  # Для Linux/WSL
    chrome_options.add_argument("--disable-extensions")  # Отключаем расширения
    chrome_options.add_argument("--disable-popup-blocking")  # Отключаем блокировку всплывающих окон
    chrome_options.add_argument("--disable-infobars")  # Убираем инфо-панель

    # === Настройка User-Agent (маскировка под обычного пользователя) ===
    chrome_options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36")

    # === Headless режим (окно браузера НЕ открывается) ===
    # Раскомментируйте строку ниже, если хотите запускать тесты без открытия окна
    chrome_options.add_argument("--headless=new")

    # Создаем сервис (автоматическое скачивание драйвера)
    service = Service(ChromeDriverManager().install())

    # Создаем драйвер с настройками
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Устанавливаем размер окна (для headless режима)
    driver.set_window_size(1920, 1080)

    yield driver

    driver.quit()


@pytest.fixture
def browser_headless(browser):
    """
    Фикстура для headless режима (окно не открывается).
    Можно использовать для CI/CD.
    """
    # Берем существующие настройки и добавляем headless
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    yield driver
    driver.quit()