from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config


def test_google_title(browser):
    browser.get(config.URL_GOOGLE)
    wait = WebDriverWait(browser, 10)

    assert "Google" in browser.title, f"Ожидалось 'Google', а получили '{browser.title}'"

    search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
    browser.execute_script("arguments[0].scrollIntoView(true);", search_box)

    search_box.clear()
    search_box.send_keys("Selenium Python")
    search_box.send_keys(Keys.RETURN)

    wait.until(EC.title_contains("Selenium"))

    assert "Selenium" in browser.title, f"Ожидалось 'Selenium' в заголовке, а получили '{browser.title}'"
