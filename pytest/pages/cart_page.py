import allure

from .base_page import BasePage
from .locators import CartPageLocators
from .locators import ThankForYourPurchase
from .personal_data import PersonalData
from selenium.webdriver.common.keys import Keys

login_data = PersonalData.login_data

class CartPageContainer(BasePage):
    """
    Функции для взаимодействия со страницей оформления заказа (корзина)
    """

    def click_cart_page_checkout_button(self):
        # courier_delivery_button = self.browser.find_element(*CartPageLocators.CART_PAGE_OTHER_CITY_COURIER_BUTTON)
        # courier_delivery_button.click()
        with allure.step("Нажимаем кнопку <Перейти к оформлению>"):
            self.browser.execute_script(f"document.querySelector('{CartPageLocators.CART_PAGE_CHECKOUT_BUTTON[1]}').click()") 
    
    def fill_recipient_phone_input_field(self):
        # Вводим номер телефона через JS
        with allure.step("Указываем номер телефона получателя"):
            self.browser.execute_script(f"const input = document.querySelector('{CartPageLocators.CART_PAGE_RECIPIENT_PHONE_INPUT_FIELD[1]}'); input.value = '{PersonalData.login_data[0]}';")
        phone_input_field = self.browser.find_element(*CartPageLocators.CART_PAGE_RECIPIENT_PHONE_INPUT_FIELD)
        # phone_input_field.send_keys(login_data[0]) # Вводим номер телефона
        with allure.step("Отправляем номер телефона"):
            phone_input_field.send_keys(Keys.RETURN) # нажимаем Ввод чтобы активировать кнопку
        

    def click_cart_send_recipient_phone_button(self):
        send_code_buttons_element_list = self.browser.find_elements(*CartPageLocators.CART_PAGE_RECIPIENT_PHONE_SEND_BUTTON)
        with allure.step("Указываем этаж получателя"):
            send_code_buttons_element_list[0].click()

    def fill_sms_code_input_field(self):
        code_input_field = self.browser.find_element(*CartPageLocators.CART_PAGE_RECIPIENT_PHONE_SMS_CODE_INPUT_FIELD)
        with allure.step("Вводим SMS-код"):
            code_input_field.send_keys(PersonalData.login_data[1])

    def click_cart_send_sms_code_button(self):
        send_sms_code_button = self.browser.find_element(*CartPageLocators.CART_PAGE_RECIPIENT_PHONE_SEND_SMS_CODE_BUTTON)
        with allure.step("Отправляем SMS-код"):
            send_sms_code_button.click()

    
    # Выбираем для доставки в НН вид курьерской доставки    

    # Выбираем для доставки в НН вид курьерской доставки    
    def click_courier_nn_delivery_button(self):
        # courier_delivery_button = self.browser.find_element(*CartPageLocators.CART_PAGE_OTHER_CITY_COURIER_BUTTON)
        # courier_delivery_button.click()
        with allure.step("Выбираем курьерскую доставку в НН"):
            self.browser.execute_script(f"document.querySelector('{CartPageLocators.CART_PAGE_NN_COURIER_BUTTON[1]}').click()") 

    def click_courier_not_nn_delivery_button(self):
        # courier_delivery_button = self.browser.find_element(*CartPageLocators.CART_PAGE_OTHER_CITY_COURIER_BUTTON)
        # courier_delivery_button.click()
        with allure.step("Выбираем курьерскую доставку не в НН "):
            self.browser.execute_script(f"document.querySelector('{CartPageLocators.CART_PAGE_NOT_NN_COURIER_BUTTON[1]}').click()") # Делаем клик на контейнер с помощью Javascript

# Заполняем и сохраняем адрес
    def fill_street_input_field(self, address_data):
        street_input_field = self.browser.find_element(*CartPageLocators.CART_PAGE_CITY_ADDRESS_FORM_STREET_INPUT_FIELD)
        with allure.step("Указываем улицу получателя"):
            street_input_field.send_keys(address_data)

    def fill_apartment_input_field(self, address_data):
        apart_input_field = self.browser.find_element(*CartPageLocators.CART_PAGE_CITY_ADDRESS_FORM_APARTMENT_INPUT_FIELD)
        with allure.step("Указываем номер дома получателя"):
            apart_input_field.send_keys(address_data)

    def fill_floor_input_field(self, address_data):
        floor_input_field = self.browser.find_element(*CartPageLocators.CART_PAGE_CITY_ADDRESS_FORM_FLOOR_INPUT_FIELD)
        with allure.step("Указываем этаж получателя"):
            floor_input_field.send_keys(address_data)

    def fill_entrance_input_field(self, address_data):
        entrance_input_field = self.browser.find_element(*CartPageLocators.CART_PAGE_CITY_ADDRESS_FORM_ENTRANCE_INPUT_FIELD)
        with allure.step("Указываем подъезд получателя"):
            entrance_input_field.send_keys(address_data)

    def fill_intercom_input_field(self, address_data):
        intercom_input_field = self.browser.find_element(*CartPageLocators.CART_PAGE_CITY_ADDRESS_FORM_INTERCOM_INPUT_FIELD)
        with allure.step("Указываем код домофона получателя"):
            intercom_input_field.send_keys(address_data)

    def click_save_address_button(self):
        # save_address_button = self.browser.find_element(*CartPageLocators.CART_PAGE_CITY_ADDRESS_FORM_SAVE_BUTTON_CONTAINER) # Событие на кнопку не работает, работает клик на контейнер
        # save_address_button.click()
        with allure.step("Сохраняем адрес получателя"):
            self.browser.execute_script(f"document.querySelector('{CartPageLocators.CART_PAGE_CITY_ADDRESS_FORM_SAVE_BUTTON[1]}').click()") # Делаем клик на контейнер с помощью Javascript



    
    # # Соглашаемся с пользовательским соглашением
    # def check_agreement_checkbox(self):
    #     # agreement_checkbox = self.browser.find_element(*CartPageLocators.CART_PAGE_AGREEMENT_CHECKBOX)
    #     # agreement_checkbox.click()
    #     with allure.step("Соглашаемся с пользовательским соглашением"):
    #         self.browser.execute_script(f"document.querySelector('{CartPageLocators.CART_PAGE_AGREEMENT_CHECKBOX[1]}').click()") # Делаем клик на кнопку с помощью Javascript


    # Кликаем кнопку оформления заказа
    def click_checkout_button(self):
        # checkout_button = self.browser.find_element(*CartPageLocators.CART_PAGE_SEND_OFFER_BUTTON)
        # checkout_button.click()
        with allure.step("Отправляем заказ"):
            self.browser.execute_script(f"document.querySelector('{CartPageLocators.CART_PAGE_SEND_OFFER_BUTTON[1]}').click()") # Делаем клик на кнопку с помощью Javascript


    # Проверяем наличие кнопки оплаты на странице и после кликаем на ссылку главной страницы
    def should_be_go_to_pay_page_button(self):
        assert self.browser.is_element_present(*ThankForYourPurchase.GO_TO_PAY_PAGE_BUTTON), "Отсутствует кнопка перехода на страницу оплаты"







