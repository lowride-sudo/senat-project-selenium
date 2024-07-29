import allure

from .base_page import BasePage
from .locators import JewelryCardPageLocators
from .locators import JewelryCardAndAddToCartPopupsLocators


class JewelryPage(BasePage):

# Кликаем на первый элемент размера
    def click_size_choice_card(self):
        size_button = self.browser.find_elements(*JewelryCardPageLocators.JEWELRY_PAGE_SIZES_CONTAINER_ELEMENT)
        with allure.step("Выбираем размер изделия"):
            size_button[0].click()

# Кликаем на кнопку в корзину
    def click_add_to_cart_button(self):
        add_to_cart_button = self.browser.find_element(*JewelryCardPageLocators.JEWELRY_PAGE_ADD_TO_CART_BUTTON)
        with allure.step("Добавить изделие в корзину"):
            add_to_cart_button.click()

# Появляется попап о том что изделие добавлено - переходим через него в корзину
    def go_to_cart_page_button(self):
        cart_page_button = self.browser.find_element(*JewelryCardAndAddToCartPopupsLocators.JEWELRY_ADDED_TO_CART_POPUP_GO_TO_CART_BUTTON)
        with allure.step("Переходим в корзину через попап"):
            cart_page_button.click()


## Покупка изделия с размером в 1 клик (кликаем на первую карточку размера)
## Покупка изделия без размера в 1 клик
    
    # Кликаем кнопку "Купить в 1 клик"
    def click_buy_in_1_click_button(self):
        buy_in_one_click_button = self.browser.find_element(*JewelryCardPageLocators.JEWELRY_PAGE_BUY_IN_ONE_CLICK_POPUP_OPEN_BUTTON)
        with allure.step('Кликаем кнопку <Купить в 1 клик>'):
            buy_in_one_click_button.click()

    # Вводим данные тестового пользователя
    def fill_name_input_field(self, buy_one_click_data):
        name_input_field = self.browser.find_element(*JewelryCardPageLocators.JEWELRY_PAGE_BUY_IN_ONE_CLICK_NAME_INPUT_FIELD)
        with allure.step("Указываем имя получателя"):
            name_input_field.send_keys(buy_one_click_data)
    
    def fill_phone_input_field(self, buy_one_click_data):
        phone_input_field = self.browser.find_element(*JewelryCardPageLocators.JEWELRY_PAGE_BUY_IN_ONE_CLICK_PHONE_INPUT_FIELD)
        with allure.step("Указываем телефон получателя"):
            phone_input_field.send_keys(buy_one_click_data)

    def fill_email_input_field(self, buy_one_click_data):
        email_input_field = self.browser.find_element(*JewelryCardPageLocators.JEWELRY_PAGE_BUY_IN_ONE_CLICK_EMAIL_INPUT_FIELD)
        with allure.step("Указываем почту получателя"):
            email_input_field.send_keys(buy_one_click_data)

    def fill_comment_input_field(self, buy_one_click_data):
        comment_input_field = self.browser.find_element(*JewelryCardPageLocators.JEWELRY_PAGE_BUY_IN_ONE_CLICK_COMMENT_INPUT_FIELD)
        with allure.step("Указываем комментарий"):
            comment_input_field.send_keys(buy_one_click_data)

    # Принимаем политику конфиденциальности
    def check_agreement_checkbox(self):
        agreement_checkbox = self.browser.find_element(*JewelryCardPageLocators.JEWELRY_PAGE_BUY_IN_ONE_CLICK_AGREEMENT_CHECKBOX)
        with allure.step("Соглашаемся с пользовательским соглашением"):
            agreement_checkbox.click()
    
    # Отправляем заказ
    def send_offer_data_button(self):
        offer_data_button = self.browser.find_element(*JewelryCardPageLocators.JEWELRY_PAGE_BUY_IN_ONE_CLICK_SEND_DATA_BUTTON)
        with allure.step("Кликаем кнопку <Отправить>"):
            offer_data_button.click()

    # Закрываем информационный попап
    def click_popup_close_button(self):
        popup_close_button = self.browser.find_element(*JewelryCardPageLocators.JEWELRY_PAGE_BUY_IN_ONE_CLICK_POPUP_CLOSE_BUTTON)
        with allure.step("Закрываем информационный попап"):
            popup_close_button.click()

# Переходим на случайный товар из слайдера с предложениями
    def click_some_jewelry_card(self):
        jewelry_pages_list = self.browser.find_elements(*JewelryCardAndAddToCartPopupsLocators.JEWELRY_CARD_JEWELRY_PAGE_LINK)
        with allure.step("Переходим на страницу изделия из слайдеров с предложениями"):
            jewelry_pages_list[0].click()
