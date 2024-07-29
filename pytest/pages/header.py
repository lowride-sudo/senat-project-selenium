import allure

from .base_page import BasePage
from .locators import HeaderLocators
from .personal_data import PersonalData
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


class HeaderContainer(BasePage):

## Данные функции являют собой абстракции для использования их в качестве шагов для исполнения тестов

# Выбор города
    def should_be_city_confirm_popup(self):
        assert self.is_element_present(*HeaderLocators.HEADER_CITY_CONFIRM_POPUP), "City confirm popup is not presented"
    
    def click_button_to_city_change(self): # кликаем на кнопку нет,
        other_city_button = self.browser.find_element(*HeaderLocators.HEADER_CITY_CONFIRM_FALSE_BUTTON)
        with allure.step("Отказываемся от автоматически определенного города"):
            other_city_button.click()

    def click_button_to_city_approve(self): # кликаем на кнопку да,
        other_city_button = self.browser.find_element(*HeaderLocators.HEADER_CITY_CONFIRM_TRUE_BUTTON)
        with allure.step("Соглашаемся с автоматически определенным городом"):
            other_city_button.click()
        
    # Если попапа подтверждения города нет - кликаем на кнопку выбранного города
    def click_geo_link_to_city_change(self): 
        geo_link = self.browser.find_element(*HeaderLocators.HEADER_CITY_SEARCH_POPUP_LINK)
        with allure.step("Открываем попап с выбором города"):
            geo_link.click()

    # Выбор Нижнего Новгорода
    def choose_nn_city_link(self):
        nn_city_link = self.browser.find_element(*HeaderLocators.HEADER_CITY_SEARCH_POPUP_CITY_NN)
        with allure.step("Выбираем Нижний Новгород через попап"):
            nn_city_link.click()

    # Проверяем что город - Нижний Новгород
    def should_be_chosen_city_label_nn(self):
        text = 'Нижний Новгород'
        assert self.browser.is_text_in_element_present(*HeaderLocators.HEADER_ACTUAL_CITY_LABEL) == text
        # chosen_city_text = self.browser.find_element(self.browser.find_element(*HeaderLocators.HEADER_ACTUAL_CITY_LABEL))
        # print(chosen_city_text)
        # assert chosen_city_text == 'Нижний Новгород', "City is not Nizhny Novgorod"
        

    # Выбор Москвы
    def choose_mos_city_link(self):
        mos_city_link = self.browser.find_element(*HeaderLocators.HEADER_CITY_SEARCH_POPUP_CITY_MOS)
        with allure.step("Выбираем Москву через попап"):
            mos_city_link.click()

    # Проверяем что город - Москва
    def should_be_chosen_city_label_moscow(self):
        chosen_city = self.browser.find_element(*HeaderLocators.HEADER_ACTUAL_CITY_LABEL)
        assert chosen_city.text == 'Москва', "City is not Moscow"
        
    # Забить в поиск <Соколов>
    def fill_text_into_input_field(self, text):
        input_field = self.browser.find_element(*HeaderLocators.HEADER_SEARCH_INPUT_FIELD_)
        with allure.step("Заполняем текст в поле поиска"):
            input_field.send_keys(text)
    
    def input_field_search(self):
        search_button = self.browser.find_element(*HeaderLocators.HEADER_SEARCH_INPUT_FIELD_)
        with allure.step("Отправляем запрос"):
            search_button.click()

    # Переход в каталог через меню
    def go_to_catalog_page(self):
        catalog_link = self.browser.find_element(*HeaderLocators.HEADER_CATALOG_LINK)
        with allure.step("Переходим в каталог через меню в хеадере"):
            catalog_link.click()

    # Переход в корзину
    def go_to_cart_page(self):
        cart_page_link = self.browser.find_element(*HeaderLocators.HEADER_CART_ICON)
        with allure.step("Переходим в корзину из хеадера"):
            cart_page_link.click()

    # Переход на главную страницу
    def go_to_main_page(self):
        main_page_link = self.browser.find_element(*HeaderLocators.HEADER_LOGO_LINK)
        with allure.step("Переходим на главную страницу из хеадера"):
            main_page_link.click()

    # Разлогинивание пользователя
    def open_login_menu_and_click_to_logoff_link(self):
        action = ActionChains(self.browser)
        profile_menu_icon = self.browser.find_element(*HeaderLocators.HEADER_LOGIN_ICON)
        with allure.step("Наводим курсор на иконку - открывается меню"):
            action.move_to_element(profile_menu_icon).perform()
        logoff_menu_link = self.browser.find_element(*HeaderLocators.HEADER_LOGIN_POPUP_AUTHORIZED_LOGOUT_LINK)
        with allure.step("Кликаем на <Выйти>"):
            logoff_menu_link.click()

    # Переход в заказы в личном кабинете
    def open_login_menu_and_click_to_my_orders_link(self):
        action = ActionChains(self.browser)
        profile_menu_icon = self.browser.find_element(*HeaderLocators.HEADER_LOGIN_ICON)
        action.move_to_element(profile_menu_icon).perform()
        my_orders_menu_link = self.browser.find_element(*HeaderLocators.HEADER_LOGIN_POPUP_AUTHORIZED_MY_ORDERS_LINK)
        with allure.step("Кликаем на ссылку <Мои заказы>"):
            my_orders_menu_link.click()


## Авторизация пользователя

    # Кликаем на иконку "Войти"
    def click_to_login_icon(self):
        login_icon = self.browser.find_element(*HeaderLocators.HEADER_LOGIN_ICON)
        with allure.step("Кликаем на ссылку <Войти> в хеадере"):
            login_icon.click()

    # Вводим телефон в поле ввода
    def fill_phone_input_field(self):
        # phone_input_field = self.browser.find_element(*HeaderLocators.HEADER_LOGIN_POPUP_PHONE_INPUT_FIELD)
        # phone_input_field.send_keys(f"{PersonalData.login_data[0]}")
        
        # Вводим номер телефона через JS
        with allure.step("Вводим номер телефона"):
            self.browser.execute_script(f"const input = document.querySelector('{HeaderLocators.HEADER_LOGIN_POPUP_PHONE_INPUT_FIELD[1]}'); input.value = '{PersonalData.login_data[0]}';")
        
        phone_input_field = self.browser.find_element(*HeaderLocators.HEADER_LOGIN_POPUP_PHONE_INPUT_FIELD)
        with allure.step("Нажимаем Enter"):
            phone_input_field.send_keys(Keys.RETURN) # нажимаем Ввод чтобы активировать кнопку


    # Кликаем кнопку отправки телефонного номера
    def click_send_phone_button(self):
        send_phone_button = self.browser.find_element(*HeaderLocators.HEADER_LOGIN_POPUP_SEND_PHONE_BUTTON)
        with allure.step("Нажимаем кнопку <Отправить>"):
            send_phone_button.click()

    # Вводим смс-код в поле ввода
    def fill_sms_code_input_field(self):
        sms_code_input_field = self.browser.find_element(*HeaderLocators.HEADER_LOGIN_POPUP_SMS_CODE_INPUT_FIELD)
        with allure.step("Вводим SMS-код"):
            sms_code_input_field.send_keys(f"{PersonalData.login_data[1]}")
        with allure.step("Нажимаем кнопку <Отправить>"):
            sms_code_input_field.send_keys(Keys.RETURN)

    # # Кликаем кнопку отправки смс-кода
    # def click-header_send_sms_code_button(self):
    #     send_sms_code_button = self.browser.find_element(*HeaderLocators.HEADER_LOGIN_POPUP_SEND_SMS_CODE_BUTTON)
    #     send_sms_code_button.click()















