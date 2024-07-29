# Данный скрипт проверяет покупку в 1 клик N=1 товарных изделий в корзину через страницу товарной позиции: заходит в каталог,
# заходит в товарную позицию, открывает форму покупки в 1 клик, заполняет данные и создает заявку.
# import time
import random
import pytest
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

catalog = "https://develop.senatnn.ru/catalog/"

# Перенес фикстуру со скоупом на класс с тестами в файл conftest.py, его нужно держать в папке с запускаемыми тестами 
# и не запускать pytest глобально из папки с проектом.

class TestBuyScenarios():
    
    @allure.epic('Smoke-функционал')
    @allure.feature('Сценарии покупки')
    @allure.story('Покупка товара используя форму в 1 клик')
    @pytest.mark.smoke
    def test_guest_buy_in_one_click_form(self, browser):
        with allure.step("Переходим на страницу каталога"):
            browser.get(catalog)
            browser.implicitly_wait(5)

        with allure.step("Ждём Jivosite чтобы убрать из страницы"):
            WebDriverWait(browser, 7).until(EC.presence_of_element_located((By.TAG_NAME, "jdiv")))
            browser.execute_script("document.getElementsByTagName('jdiv')[0].remove()")
            browser.execute_script("document.querySelector('.header-bottom').remove()") # Удаляем Header чтобы не мешал

        with allure.step("Заходим в случайную карточку изделия (захардкожена первая)"): 
            jewelry_cards_links = browser.find_elements(By.CSS_SELECTOR, ".senat-cat-item.NEW .senat-item-image-wrapper")
            jewelry_cards_links[0].click()

        with allure.step("Ищем список с размерами"):
            WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn-link.oneclick"))) 
        if len(browser.find_elements(By.CSS_SELECTOR, ".product-item-detail-info-container-title")) == 1: 
            sizes = browser.find_elements(By.CSS_SELECTOR, ".offer-list-item")
            with allure.step("Размер предусмотрен - выбираем случайный размер"):
                if len(sizes) > 1:
                    sizes[random.randint(0, len(sizes) - 1)].click()
                else:
                    sizes[0].click()
        else:
            with allure.step("Размер не предусмотрен - пропускаем"):
                pass


        # СЦЕНАРИЙ ПОКУПКИ В 1 КЛИК 
        with allure.step("Открываем форму покупки в 1 клик"):
            browser.find_element(By.CSS_SELECTOR, "#oneclick-start").click()
        WebDriverWait(browser, 7).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".fancybox-container")))
        
        # нужно создать массив по классу ".popup-form .lk-form-input"
        with allure.step("Парсим поля формы в массив"):
            input_fields = browser.find_elements(By.CSS_SELECTOR, ".fancybox-container .popup-form .lk-form-input")
        with allure.step("Заполняем поля тестовыми данными"):
            input_fields[0].send_keys("Test Automation")
            input_fields[1].send_keys("77777777777")
            input_fields[2].send_keys("test@test.test")
            input_fields[3].send_keys("Какой-то текст")
        with allure.step("Соглашаемся с пользовательским соглашением"):
            browser.find_element(By.CSS_SELECTOR, ".agreement__checkbox").click()
        with allure.step("Отправляем данные через форму"):
            browser.find_element(By.CSS_SELECTOR, "button.lk-btn").click()
        # time.sleep(5)

