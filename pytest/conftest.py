# Файл конфигурации тестов - используется как внешний модуль, содержащий в себе на выбор 2 драйвера для 
# выполнения тестов: Chrome-webdriver и Firefox-webdriver 
import pytest
import allure

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options



def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                    help="Choose browser: chrome or firefox")

    parser.addoption('--language', action='store', default="ru",
                    help="Choose language: en,ru or another")
    

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        with allure.step("Запускаем Chrome для тестов"):
            options = Options()
            # options.add_argument("--headless")
            options.add_argument("window-size=1920,1080")
            options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
            browser = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == "firefox":
        with allure.step("Запускаем Firefox для тестов"):
            options = webdriver.FirefoxProfile()
            options.set_preference("intl.accept_languages", user_language)
            browser = webdriver.Firefox(options=options, executable_path=GeckoDriverManager().install())
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    with allure.step("Завершаем сессию браузера"):
        browser.quit()