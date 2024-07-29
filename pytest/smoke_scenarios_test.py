import time
import allure

from pages.jewelry_page import JewelryPage
from pages.header import HeaderContainer
from pages.catalog_page import CatalogPage
from pages.cart_page import CartPageContainer
from pages.personal_cabinet_page import PersonalMyOrdersPage
from pages.personal_data import PersonalData

buy_one_click_data = PersonalData.buy_one_click_data
address_data = PersonalData.address_data
login_data = PersonalData.login_data
site = 'https://develop.senatnn.ru'


@allure.epic('Smoke-тестирование основного функционала сайта')
class TestSmokeScenarios():
    
    @allure.story('Смена города на Нижний Новгород')
    def test_guest_can_change_city_to_nn(self, browser):
        link = f"{site}/?utm_source=test&utm_medium=test"
        page = HeaderContainer(browser, link)   
        page.open(link)                      
        page.click_button_to_city_change()          
        page.choose_nn_city_link()          
        time.sleep(2)
        # page.should_be_chosen_city_label_nn()          

    @allure.story('Поиск бренда Sokolov')
    def test_guest_can_search_sokolov(self, browser):
        link = f"{site}/?utm_source=test&utm_medium=test"
        text = "sokolov"
        page = HeaderContainer(browser, link)
        page.open(link)
        page.fill_text_into_input_field(text)
        page.input_field_search()

    @allure.story('Переход в каталог через меню')
    def test_guest_can_go_to_catalog_from_menu(self, browser):
        link = f"{site}/?utm_source=test&utm_medium=test"
        page = HeaderContainer(browser, link)
        page.open(link)
        time.sleep(2)
        page.click_geo_link_to_city_change()  
        page.choose_nn_city_link()          
        time.sleep(1)
        page.go_to_catalog_page()

    @allure.story('Проверка фильтра бренда и функций сортировки')
    def test_guest_can_filter_sokolov_and_sort(self, browser):
        link = f"{site}/catalog/ukrasheniya/?utm_source=test&utm_medium=test"
        page = CatalogPage(browser, link)
        page.open(link)
        time.sleep(2)
        page.check_sokolov_brand_filter()
        time.sleep(3)
        page.click_brand_filter_apply_button()
        page.click_sort_catalog_price_descending_button()
        page.click_sort_catalog_price_ascending_button()

    @allure.story('Проверка перехода в категорию колец, добавление в корзину через каталог')
    def test_guest_can_add_ring_to_cart(self, browser):
        link = f"{site}/catalog/ukrasheniya/?utm_source=test&utm_medium=test"
        page = CatalogPage(browser, link)
        page.open(link)
        page.go_to_rings_category()
        page.click_card_add_to_cart_button()
        page.click_jewelry_size_choice_card()
        page.click_add_to_cart_button()
        page.click_continue_shopping_button()
        time.sleep(2)

    @allure.story('Проверка перехода в категорию брошей, переход на страницу изделия, покупка в 1 клик, переход в корзину')
    def test_guest_can_go_to_jewelry_page_and_buy_in_one_click(self, browser):
        link = f"{site}/catalog/ukrasheniya/?utm_source=test&utm_medium=test"
        page = CatalogPage(browser, link)
        page.open(link)
        page.go_to_brooches_category()
        page.go_to_jewelry_page_from_catalog()
        jewelry_page = JewelryPage(browser, browser.current_url)
        jewelry_page.click_buy_in_1_click_button()
        jewelry_page.fill_name_input_field(buy_one_click_data[0])
        jewelry_page.fill_phone_input_field(buy_one_click_data[1])
        jewelry_page.fill_email_input_field(buy_one_click_data[2])
        jewelry_page.fill_comment_input_field(buy_one_click_data[3])
        jewelry_page.check_agreement_checkbox()
        jewelry_page.send_offer_data_button()
        jewelry_page.click_popup_close_button()

        header = HeaderContainer(browser, browser.current_url)
        header.go_to_cart_page()


    @allure.story('Оформление заказа с доставкой по Нижнему Новгороду')
    def test_guest_can_checkout_to_nn_at_cart_page(self, browser):
        link = f"{site}/?utm_source=test&utm_medium=test"
        page = HeaderContainer(browser, link)   
        page.open(link)    
        time.sleep(2)                  
        page.click_geo_link_to_city_change()
        page.choose_nn_city_link()          
        time.sleep(2)

        link_catalog = f"{site}/catalog/ukrasheniya/?utm_source=test&utm_medium=test"
        page = CatalogPage(browser, link_catalog)
        page.open(link_catalog)
        page.go_to_rings_category()
        page.click_card_add_to_cart_button()
        page.click_jewelry_size_choice_card()
        page.click_add_to_cart_button()
        page.click_continue_shopping_button()

        link_cart = f"{site}/cart/ordering/?utm_source=test&utm_medium=test"
        page = CartPageContainer(browser, link_cart)
        page.open(link_cart)
        browser.execute_script("document.querySelector('.header-bottom').remove()") # Удаляем Header чтобы не мешал

        time.sleep(1)        
        page.click_cart_page_checkout_button()
        time.sleep(1)
        page.fill_recipient_phone_input_field()
        time.sleep(1)
        page.click_cart_send_recipient_phone_button()
        time.sleep(1)
        page.fill_sms_code_input_field()
        page.click_cart_send_sms_code_button()
        time.sleep(1)

        page.click_courier_nn_delivery_button()
        page.fill_street_input_field(address_data[0])
        page.fill_apartment_input_field(address_data[1])
        page.fill_floor_input_field(address_data[2])
        page.fill_entrance_input_field(address_data[3])
        page.fill_intercom_input_field(address_data[4])
        page.click_save_address_button()

        page.click_checkout_button()
        time.sleep(10)
        
    @allure.story('Проверка авторизации и разлогин')
    def test_guest_can_login_and_logout(self, browser):
        link = f"{site}/catalog/ukrasheniya/?utm_source=test&utm_medium=test"
        page = HeaderContainer(browser, link)
        page.open(link)
        page.click_to_login_icon()
        time.sleep(1)
        page.fill_phone_input_field()
        time.sleep(1)
        page.click_send_phone_button()
        page.fill_sms_code_input_field()
        time.sleep(1)
        link = f"{site}/catalog/ukrasheniya/?utm_source=test&utm_medium=test"
        page = HeaderContainer(browser, link)
        page.open(link)
        page.open_login_menu_and_click_to_logoff_link()
        time.sleep(1)

    @allure.story('Проверка авторизации, выбор Москвы')
    def test_guest_can_login(self, browser):
        link = f"{site}/catalog/ukrasheniya/?utm_source=test&utm_medium=test"
        page = HeaderContainer(browser, link)
        page.open(link)
        page.click_to_login_icon()
        time.sleep(1)
        page.fill_phone_input_field()
        time.sleep(1)
        page.click_send_phone_button()
        page.fill_sms_code_input_field() # Отправка смс-кода идет через нажатие кода через Js
        time.sleep(1)

        link = f"{site}/catalog/ukrasheniya/?utm_source=test&utm_medium=test"
        page = HeaderContainer(browser, link)
        page.open(link) # 
        time.sleep(2)
        page.click_geo_link_to_city_change()   
        page.choose_mos_city_link()  
        time.sleep(2)
        # page.should_be_chosen_city_label_moscow()

    @allure.story('Добавление цепи в корзину, оформление товара с доставкой в Москву, оплата через личный кабинет')
    def test_guest_can_add_chain_to_cart(self, browser):
        link = f"{site}/catalog/ukrasheniya/?utm_source=test&utm_medium=test"
        page = CatalogPage(browser, link)
        page.open(link)
        page.go_to_chains_category()
        page.go_to_jewelry_page_from_catalog()
        jewelry_page = JewelryPage(browser, browser.current_url)
        jewelry_page.click_size_choice_card()
        jewelry_page.click_add_to_cart_button()
        jewelry_page.go_to_cart_page_button()

        page = CartPageContainer(browser, browser.current_url)
        page.open(link)
        time.sleep(2)
        page.click_cart_page_checkout_button()
        
        time.sleep(1)
        page.fill_recipient_phone_input_field()
        time.sleep(1)
        page.click_cart_send_recipient_phone_button()
        time.sleep(1)
        page.fill_sms_code_input_field()
        page.click_cart_send_sms_code_button()
        time.sleep(1)

        page.click_courier_not_nn_delivery_button()
        page.click_courier_nn_delivery_button()
        page.fill_street_input_field(address_data[0])
        page.fill_apartment_input_field(address_data[1])
        page.fill_floor_input_field(address_data[2])
        page.fill_entrance_input_field(address_data[3])
        page.fill_intercom_input_field(address_data[4])
        page.click_save_address_button()

        page.click_checkout_button()
        time.sleep(10) 

        link = f"{site}/?utm_source=test&utm_medium=test"
        page = HeaderContainer(browser, link)
        page.open(link)
        page.open_login_menu_and_click_to_my_orders_link()
        personal_cabinet_page = PersonalMyOrdersPage(browser, browser.current_url)
        personal_cabinet_page.click_personal_cabinet_my_orders_pay_button()
        time.sleep(10)


