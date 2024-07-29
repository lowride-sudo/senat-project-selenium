import allure

from .base_page import BasePage
from .locators import PersonalCabinetLocators


class PersonalMyOrdersPage(BasePage):

    # Кликаем на кнопку оплаты последнего заказа    
    def click_personal_cabinet_my_orders_pay_button(self):
        my_orders_pay_button = self.browser.find_element(*PersonalCabinetLocators.ORDERS_PAGE_ORDER_CARD_PAY_BUTTON)
        with allure.step("Кликаем в первой карточке заказа на кнопку <Оплатить>"):
            my_orders_pay_button.click()
