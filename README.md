# 🧪 UI Automation Tests

Проект автоматизации тестирования веб-интерфейса с использованием **Selenium WebDriver** и паттерна **Page Object Model (POM)**.

---

## 📁 Структура проекта
| Путь | Описание |
|------|----------|
| `pages/base_page.py` | Базовый класс для всех страниц |
| `pages/login_page.py` | Класс страницы логина (Saucedemo) |
| `tests/test_google.py` | Тесты для Google |
| `tests/test_saucedemo.py` | Тесты для Saucedemo |
| `conftest.py` | Фикстуры pytest (browser, driver) |
| `pytest.ini` | Настройки pytest |
| `README.md` | Документация проекта |

---

## 🚀 Быстрый старт

### 1. Установка зависимостей

```bash
pip install selenium pytest
2. Запуск тестов
bash
# Запуск всех тестов
pytest tests/

# Только тесты Saucedemo
pytest tests/test_saucedemo.py

# Только тесты Google
pytest tests/test_google.py

# С детализацией
pytest -v tests/

# Запуск конкретного теста
pytest tests/test_saucedemo.py::TestSaucedemoLogin::test_valid_login
📄 Описание файлов
pages/base_page.py
Базовый класс, содержащий общие методы для работы с веб-элементами.

Метод	Параметры	Описание
find_element	locator, timeout=10	Поиск элемента с ожиданием появления в DOM
click	locator, timeout=10	Клик по элементу (ждёт кликабельности)
enter_text	locator, text, timeout=10	Очистка поля и ввод текста
get_text	locator, timeout=10	Получение текстового содержимого элемента
is_element_visible	locator, timeout=10	Проверка видимости элемента (возвращает bool)
Особенности:

Все методы используют WebDriverWait с таймаутом 10 секунд по умолчанию

В конструкторе инициализируется self.wait для переиспользования

pages/login_page.py
Страница логина Saucedemo. Наследуется от BasePage.

Локаторы
Атрибут	Значение	Описание
USERNAME_INPUT	(By.ID, "user-name")	Поле ввода логина
PASSWORD_INPUT	(By.ID, "password")	Поле ввода пароля
LOGIN_BUTTON	(By.ID, "login-button")	Кнопка "Login"
ERROR_MESSAGE	(By.CSS_SELECTOR, "[data-test='error']")	Блок сообщения об ошибке
PRODUCTS_HEADER	(By.CLASS_NAME, "app_logo")	Логотип приложения
PRODUCTS_TITLE	(By.CLASS_NAME, "title")	Заголовок "Products"
Методы
Метод	Возвращает	Описание
open()	self	Открывает страницу логина
enter_username(username)	self	Вводит имя пользователя
enter_password(password)	self	Вводит пароль
click_login_button()	self	Нажимает кнопку входа
login(username, password)	self	Полная авторизация (все шаги)
get_error_message()	str	Возвращает текст ошибки
is_login_successful()	bool	Проверяет успешность входа
get_products_title()	str	Возвращает заголовок "Products"
Пример использования
python
login_page = LoginPage(browser)

# Пошаговый вход
login_page.open()
login_page.enter_username("standard_user")
login_page.enter_password("secret_sauce")
login_page.click_login_button()

# Цепочка вызовов (fluent interface)
login_page.open().login("standard_user", "secret_sauce")

# Проверки
assert login_page.is_login_successful()
title = login_page.get_products_title()
tests/test_saucedemo.py
Тесты авторизации на Saucedemo.

Тест	Данные	Ожидаемый результат
test_valid_login	standard_user / secret_sauce	Успешный вход, заголовок "Products"
test_invalid_login	wrong_user / wrong_password	Ошибка: "Username and password do not match"
test_empty_login	Ничего не вводить	Ошибка: "Username is required"
test_locked_user	locked_out_user / secret_sauce	Ошибка: "Sorry, this user has been locked out"
Структура: Все тесты объединены в класс TestSaucedemoLogin, каждый тест использует фикстуру browser из conftest.py.

tests/test_google.py
Простой тест поиска в Google (без использования POM).

Что делает:

Открывает google.com

Проверяет заголовок страницы

Вводит запрос "Selenium Python"

Проверяет, что слово "Selenium" появилось в заголовке

🛠 Используемые технологии
Технология	Назначение
Python	Язык программирования
Selenium WebDriver	Управление браузером
pytest	Фреймворк для запуска тестов
Page Object Model	Паттерн организации кода (упрощает поддержку)
WebDriverWait	Явные ожидания для стабильности тестов
📌 Рекомендации по разработке
Новые страницы — всегда наследуй от BasePage

Локаторы — храни как атрибуты класса (константы)

Методы — возвращай self для цепочечных вызовов

Ожидания — используй WebDriverWait, избегай time.sleep()

Названия — давай осмысленные имена методам и переменным

🐛 Возможные проблемы и решения
Проблема	Решение
ModuleNotFoundError: No module named 'pages'	Запускай тесты из корня проекта: pytest tests/
Драйвер браузера не найден	Установи WebDriver Manager: pip install webdriver-manager
Тесты падают из-за ожиданий	Увеличь таймаут в BasePage.__init__ или передавай timeout в методы
Элемент не найден	Проверь локатор, используй By.ID, By.CSS_SELECTOR и т.д.
Если хочешь дополнить проект:

Fork репозитория

Создай новую ветку (git checkout -b feature/your-feature)

Внеси изменения

Сделай Pull Request

Правила:

Все новые страницы — от BasePage

Локаторы — только внутри класса страницы

Используй явные ожидания

Пиши понятные названия тестов