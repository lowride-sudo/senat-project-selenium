import allure

from .base_page import BasePage
from .locators import FiltersAndSortingLocators
from .locators import JewelryCardAndAddToCartPopupsLocators

class CatalogPage(BasePage):
    """
    Функции для взаимодействия с фильтрами оформления заказа (корзина)
    """

# Проверить фильтрацию по бренду Соколов, сортировку по убыванию цены, сортировку по возрастанию цены
    def check_sokolov_brand_filter(self):
        # title = self.browser.find_element(*FiltersAndSortingLocators.BRAND_FILTER_TITLE)
        # checkbox = self.browser.find_element(*FiltersAndSortingLocators.BRAND_FILTER_SOKOLOV_CHECKBOX)
        with allure.step("Отмечаем Sokolov в фильтре бренда"):
            self.browser.execute_script(f'document.querySelector("{FiltersAndSortingLocators.BRAND_FILTER_SOKOLOV_CHECKBOX[1]}").click()') # Делаем клик на чекбокс с помощью Javascript

    def click_brand_filter_apply_button(self):
        # brand_filter_apply_button = self.browser.find_element(*FiltersAndSortingLocators.BRAND_FILTER_APPLY)
        # self.move_to_element(*FiltersAndSortingLocators.BRAND_FILTER_APPLY).click()
        with allure.step("Применяем выбранный фильтр"):
            self.browser.execute_script(f'document.querySelector("{FiltersAndSortingLocators.BRAND_FILTER_APPLY[1]}").click()') # Делаем клик на чекбокс с помощью Javascript
    

    def click_sort_catalog_price_descending_button(self):
        price_descending_link = self.browser.find_element(*FiltersAndSortingLocators.SORT_TYPE_PRICE_DESCENDING)
        with allure.step("Применяем сортировку каталога по убыванию цены"):
            price_descending_link.click()

    def click_sort_catalog_price_ascending_button(self):
        price_ascending_link = self.browser.find_element(*FiltersAndSortingLocators.SORT_TYPE_PRICE_ASCENDING)
        with allure.step("Применяем сортировку каталога по возрастанию цены"):
            price_ascending_link.click()


# Добавление изделия в корзину через каталог (с выбором размера)
    def go_to_rings_category(self):
        filter_categories_list = self.browser.find_elements(*FiltersAndSortingLocators.CATEGORIES_LINK)
        with allure.step("Переходим в категорию Кольца"):
            filter_categories_list[4].click()

    def click_card_add_to_cart_button(self): # можно сделать функцию с выбором рандомного элемента списка
        filter_categories_list = self.browser.find_elements(*JewelryCardAndAddToCartPopupsLocators.JEWELRY_CARD_ADD_TO_CART_BUTTON)
        with allure.step("Нажимаем кнопку добавления в корзину 1-й карточки в списке"):
            filter_categories_list[0].click()

    def click_jewelry_size_choice_card(self): # можно сделать функцию с выбором рандомного элемента списка
        size_choice_card = self.browser.find_elements(*JewelryCardAndAddToCartPopupsLocators.JEWELRY_SIZE_POPUP_SIZE_CARD)
        with allure.step("Выбираем размер у изделия с размером"):
            size_choice_card[0].click()
    
    def click_add_to_cart_button(self):
        add_to_card_button = self.browser.find_element(*JewelryCardAndAddToCartPopupsLocators.JEWELRY_SIZE_POPUP_SIZE_ADD_TO_CART_BUTTON)
        with allure.step("Подтверждаем выбранный размер"):
            add_to_card_button.click()

    def click_continue_shopping_button(self):
        continue_shopping_button = self.browser.find_element(*JewelryCardAndAddToCartPopupsLocators.JEWELRY_ADDED_TO_CART_POPUP_CONTINUE_SHOPPING_BUTTON)
        with allure.step('Кликаем кнопку "Продолжить покупки"'):
            continue_shopping_button.click()

# Переход в категорию изделий без размера - броши
    def go_to_brooches_category(self):
        filter_categories_list = self.browser.find_elements(*FiltersAndSortingLocators.CATEGORIES_LINK)
        with allure.step("Переходим в категорию Броши"):
            filter_categories_list[2].click()  

# Переход в категорию изделий с размером - цепи
    def go_to_chains_category(self):
        filter_categories_list = self.browser.find_elements(*FiltersAndSortingLocators.CATEGORIES_LINK)
        with allure.step("Переходим в категорию Цепи"):
            filter_categories_list[8].click()

# Заходим на страницу изделия
    def go_to_jewelry_page_from_catalog(self): # можно сделать функцию с выбором рандомного элемента списка
        jewelry_pages_list = self.browser.find_elements(*JewelryCardAndAddToCartPopupsLocators.JEWELRY_CARD_JEWELRY_PAGE_LINK)
        with allure.step("Переходим на страницу изделия из каталога"):
            jewelry_pages_list[0].click()