import allure

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)     

    def open(self, link):
        with allure.step(f'Открываем страницу"{link}"'):
            self.browser.get(self.url)

    def is_element_present(self, method, selector):
        try:
            self.browser.find_element(method, selector)
        except(NoSuchElementException):
            return False
        return True

    def is_text_in_element_present(self, method, selector, text, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.text_to_be_present_in_element(method, selector, text))
        except TimeoutException:
            return False
        return True
        
    # def move_to_element(self, method, selector):
    #     element = self.browser.find_element(method,selector)
    #     ActionChains(self.browser).click(element).perform()
