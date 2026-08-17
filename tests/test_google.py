from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, config


def test_google_title(browser):
    browser.get(config.URL_GOOGLE)

    time.sleep(2)

    assert "Google" in browser.title, f"Ожидалось 'Google', а получили '{browser.title}'"

    search_box = browser.find_element(By.NAME, "q")

    browser.execute_script("arguments[0].scrollIntoView(true);", search_box)
    time.sleep(0.5)

    search_box.clear()
    search_box.send_keys("Selenium Python")
    search_box.send_keys(Keys.RETURN)

    time.sleep(3)

    assert "Selenium" in browser.title, f"Ожидалось 'Selenium' в заголовке, а получили '{browser.title}'"
