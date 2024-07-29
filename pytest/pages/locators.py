from selenium.webdriver.common.by import By


class HeaderLocators():
    """
    Локаторы в хеадере
    """

## HEADER

    HEADER_BANNER_TOP_LINK = (By.CSS_SELECTOR, ".bannerTop__link")
    
    # Popup city_confirm
    HEADER_CITY_CONFIRM_POPUP = (By.CSS_SELECTOR, "#geoWrapper")
    HEADER_CITY_CONFIRM_FALSE_BUTTON = (By.CSS_SELECTOR, ".geo-button-city.geoCityFancybox")
    HEADER_CITY_CONFIRM_TRUE_BUTTON = (By.CSS_SELECTOR, "button.geo-button-confirm")


    # Popup city_search
    HEADER_CITY_SEARCH_POPUP_LINK = (By.CSS_SELECTOR, ".icon.geo.geoCityFancybox")
    HEADER_CITY_SEARCH_POPUP = (By.CSS_SELECTOR, "#geoCity")
    HEADER_CITY_SEARCH_POPUP_FORM = (By.CSS_SELECTOR, ".lk-form-input")
    HEADER_CITY_SEARCH_POPUP_CITY_ELEMENT = (By.CSS_SELECTOR, ".geo-city-item")
    HEADER_CITY_SEARCH_POPUP_CITY_NN = (By.CSS_SELECTOR, "[data-value='Нижний Новгород']")
    HEADER_CITY_SEARCH_POPUP_CITY_MOS = (By.CSS_SELECTOR, "[data-value='Москва']")
    HEADER_CITY_SEARCH_POPUP_FORM_CLOSE_BUTTON = (By.CSS_SELECTOR, ".geo-popup .fancybox-button.fancybox-close-small")
    
    # Actual_city_label
    HEADER_ACTUAL_CITY_LABEL = (By.CSS_SELECTOR, ".headre-geo span", 'Нижний Новгород')

    # Header_logo container
    HEADER_LOGO_LINK = (By.CSS_SELECTOR, "a.logo")

    # Stores and About_company container 
    HEADER_STORES_LINK = (By.CSS_SELECTOR, ".rightblock a:nth-child(1)")
    HEADER_ABOUT_COMPANY_LINK = (By.CSS_SELECTOR, ".rightblock a:nth-child(2)")
    

    # Promo_action and Novelty container
    HEADER_PROMO_ACTION_LINK = (By.CSS_SELECTOR, ".header-middle .headre-geo p:nth-child(1) .main-menu-item")
    HEADER_NOVELTY_LINK = (By.CSS_SELECTOR, ".header-middle .headre-geo p:nth-child(2) .main-menu-item")
    

    # Login, Favorites, Cart container
    HEADER_LOGIN_ICON = (By.CSS_SELECTOR, "a#log-in")
    
    HEADER_FAVORITES_ICON = (By.CSS_SELECTOR, "#want")
    HEADER_FAVORITES_ICON_COUNTER = (By.CSS_SELECTOR, "#want span.col")

    HEADER_CART_ICON = (By.CSS_SELECTOR, "#bx_basketFKauiI > a")
    HEADER_CART_ICON_COUNTER = (By.CSS_SELECTOR, "#bx_basketFKauiI > a span")

    # Cart header popup
    HEADER_CART_POPUP = (By.CSS_SELECTOR, "#bx_basketFKauiIproducts")
    HEADER_CART_POPUP_JEWELRY_LINK = (By.CSS_SELECTOR, "#bx_basketFKauiIproducts > div .ttl") 
    HEADER_CART_POPUP_JEWELRY_REMOVE_FROM_CART_BUTTON = (By.CSS_SELECTOR, "#bx_basketFKauiIproducts > div .senat-cart-item-remove") 
    HEADER_CART_POPUP = (By.CSS_SELECTOR, "#bx_basketFKauiIproducts > div .senat-cart-item-data")
    
    # Login popup
    HEADER_LOGIN_POPUP = (By.CSS_SELECTOR, ".fancybox-custom.fancybox-custom-sm.fancybox-content")
    HEADER_LOGIN_POPUP_CLOSE_BUTTON = (By.CSS_SELECTOR, ".fancybox-custom-sm .fancybox-button.fancybox-close-small")
    HEADER_LOGIN_POPUP_PHONE_INPUT_FIELD = (By.CSS_SELECTOR, "#sign-bycode-phone")
    HEADER_LOGIN_POPUP_SEND_PHONE_BUTTON = (By.CSS_SELECTOR, ".lk-form-button .lk-btn")

    HEADER_LOGIN_POPUP_CHANGE_PHONE_BUTTON = (By.CSS_SELECTOR, ".lk-form-hide.signin-byphonecode-to-sign")
    HEADER_LOGIN_POPUP_SMS_CODE_INPUT_FIELD = (By.CSS_SELECTOR, ".lk-form-input.signin-byphonecode-code")
    HEADER_LOGIN_POPUP_RESEND_CODE = (By.CSS_SELECTOR, ".resend-code-link")
    HEADER_LOGIN_POPUP_SEND_SMS_CODE_BUTTON = (By.CSS_SELECTOR, "input[value='Подтвердить']")

    # Login popup authorized
    HEADER_LOGIN_POPUP_AUTHORIZED = (By.CSS_SELECTOR, ".lk-dropdown.active")
    HEADER_LOGIN_POPUP_AUTHORIZED_PERSONAL_DATA_PROFILE_LINK = (By.CSS_SELECTOR, ".lk-dropdown [href='/personal/orders/']")
    HEADER_LOGIN_POPUP_AUTHORIZED_MY_ORDERS_LINK = (By.CSS_SELECTOR, ".lk-dropdown [href='/personal/orders/']")
    HEADER_LOGIN_POPUP_AUTHORIZED_FAVORITES_LINK = (By.CSS_SELECTOR, ".lk-dropdown [href='/favorites/']")
    HEADER_LOGIN_POPUP_AUTHORIZED_LOGOUT_LINK = (By.CSS_SELECTOR, ".lk-dropdown .lk-nav-exit")
    
    # Catalog, Promo container
    HEADER_CATALOG_LINK = (By.CSS_SELECTOR, ".main-menu-list__item:nth-child(1) .main-menu-item.href")
    HEADER_PROMO_LINK1 = (By.CSS_SELECTOR, ".main-menu-list__item:nth-child(2) .main-menu-item.href")
    HEADER_PROMO_LINK2 = (By.CSS_SELECTOR, ".main-menu-list__item:nth-child(3) .main-menu-item.href")

    # Catalog menu container
    HEADER_CATALOG_MENU_CONTAINER = (By.CSS_SELECTOR, ".main-submenu")
    HEADER_CATALOG_MENU_CATEGORIES_LINK = (By.CSS_SELECTOR, ".main-submenu-section__link")
    HEADER_CATALOG_MENU_DIFFERENT_ENTITIES_SORT_LINK = (By.CSS_SELECTOR, ".main-submenu-list__link")

    
    # Search form container
    HEADER_SEARCH_INPUT_FIELD_ = (By.CSS_SELECTOR, ".header-search .inpt")
    HEADER_SEARCH_SEARCH_BUTTON = (By.CSS_SELECTOR, ".header-search .search-submit")
    
    # Breadcrumbs container
    BREADCRUMBS_CONTAINER =  (By.CSS_SELECTOR, ".bx-breadcrumb")
    BREADCRUMBS_LINK =  (By.CSS_SELECTOR, "#navigation a")

## ELEMENTS TO DELETE
    HEADER_BOTTOM_MENU = (By.CSS_SELECTOR, ".header-search .search-submit") # имеет смысл его удалить чтобы он не мешал при кликах
    JIVOSITE_CHAT = (By.CSS_SELECTOR, ".header-search .search-submit") # тоже удалить 
    

class MainPageLocators():
    """
    Локаторы на главной странице
    """
    PAGE_TOP_BANNER_IMAGE_LINK = (By.CSS_SELECTOR, ".main-slider .slick-track .slick-active")
    


class FiltersAndSortingLocators():
    """
    Фильтры используются в каталоге, поиске
    Сортировка используется в каталоге, избранном
    """

## ССЫЛКИ КАТЕГОРИИ
    # 0-й элемент в списке это общая категория украшения - ее не нужно использовать
    CATEGORIES_LINK = (By.CSS_SELECTOR, ".filter-categories__list.acco.acco_filter a") 


## ФИЛЬТРЫ
    # Фильтр по цене
    MIN_PRICE_INPUT_FIELD = (By.CSS_SELECTOR, "#arrfilter_P1_MIN") 
    MAX_PRICE_INPUT_FIELD = (By.CSS_SELECTOR, "#arrfilter_P1_MAX") 
    
    # Фильтр Для_кого
    FOR_WHO_FILTER_CHECKBOX = (By.CSS_SELECTOR, "#SMARTFILTER_FORM > .row:first-child > div:nth-child(4) .checkbox input:not([disabled])") 
    FOR_WHO_FILTER_CLEAR = (By.CSS_SELECTOR, "#SMARTFILTER_FORM > .row:first-child > div:nth-child(4) > .senat-filter-parameters-box-title a")
    FOR_WHO_FILTER_APPLY = (By.CSS_SELECTOR, "#SMARTFILTER_FORM > .row:first-child > div:nth-child(4) #modef a")
    
    # Фильтр Камень_основной_вставки
    GEM_FILTER_CHECKBOX = (By.CSS_SELECTOR, "#SMARTFILTER_FORM > .row:first-child > div:nth-child(5) .checkbox input:not([disabled])")     
    GEM_FILTER_CLEAR = (By.CSS_SELECTOR, "#SMARTFILTER_FORM > .row:first-child > div:nth-child(5) > .senat-filter-parameters-box-title a")
    GEM_FILTER_APPLY = (By.CSS_SELECTOR, "#SMARTFILTER_FORM > .row:first-child > div:nth-child(5) #modef a")
    
    # Фильтр Бренд
    BRAND_FILTER_CONTAINER = (By.CSS_SELECTOR, "div.senat-filter-parameters-box:nth-child(6)") 
    BRAND_FILTER_CONTAINER_SOKOLOV = (By.CSS_SELECTOR, "div.senat-filter-parameters-box:nth-child(6)") 
    BRAND_FILTER_CHECKBOX = (By.CSS_SELECTOR, "div.senat-filter-parameters-box:nth-child(6) .checkbox input:not([disabled])") 
    BRAND_FILTER_TITLE = (By.XPATH, "//div/span[contains(text(),'Бренд')]") 
    BRAND_FILTER_SOKOLOV_CHECKBOX = (By.CSS_SELECTOR, ".senat-filter-param-text[title='Sokolov']") 
    BRAND_FILTER_CLEAR = (By.CSS_SELECTOR, "#SMARTFILTER_FORM > .row:first-child > div:nth-child(6) > .senat-filter-parameters-box-title a")
    BRAND_FILTER_APPLY = (By.CSS_SELECTOR, ".senat-filter-container-modef #modef a")
    
    # Фильтр Проба
    FINENESS_FILTER_CHECKBOX = (By.CSS_SELECTOR, "#SMARTFILTER_FORM > .row:first-child > div:nth-child(7) .checkbox input:not([disabled])") 
    FINENESS_FILTER_CLEAR = (By.CSS_SELECTOR, "#SMARTFILTER_FORM > .row:first-child > div:nth-child(7) > .senat-filter-parameters-box-title a")
    FINENESS_FILTER_APPLY = (By.CSS_SELECTOR, "#SMARTFILTER_FORM > .row:first-child > div:nth-child(7) #modef a")

    # Фильтр Цвет_металла/покрытие
    METAL_COVER_PLATING_FILTER_CHECKBOX = (By.CSS_SELECTOR, "#SMARTFILTER_FORM > .row:first-child > div:nth-child(8) .checkbox input:not([disabled])") 
    METAL_COVER_PLATING_FILTER_CLEAR = (By.CSS_SELECTOR, "#SMARTFILTER_FORM > .row:first-child > div:nth-child(8) > .senat-filter-parameters-box-title a") 
    METAL_COVER_PLATING_FILTER_APPLY = (By.CSS_SELECTOR, "#SMARTFILTER_FORM > .row:first-child > div:nth-child(8) #modef a") 

    # Фильтр Материал
    MATERIAL_FILTER_CHECKBOX = (By.CSS_SELECTOR, "#SMARTFILTER_FORM > .row:first-child > div:nth-child(9) .checkbox input:not([disabled])") 
    MATERIAL_FILTER_CLEAR = (By.CSS_SELECTOR, "#SMARTFILTER_FORM > .row:first-child > div:nth-child(9) > .senat-filter-parameters-box-title a") 
    MATERIAL_FILTER_APPLY = (By.CSS_SELECTOR, "#SMARTFILTER_FORM > .row:first-child > div:nth-child(9) #modef a") 

    # Фильтр Акции
    PROMO_FILTER_CHECKBOX = (By.CSS_SELECTOR, "#SMARTFILTER_FORM > .row:first-child > div:nth-child(10) .checkbox input:not([disabled])") 
    PROMO_FILTER_CLEAR = (By.CSS_SELECTOR, "#SMARTFILTER_FORM > .row:first-child > div:nth-child(10) > .senat-filter-parameters-box-title a") 
    PROMO_FILTER_APPLY = (By.CSS_SELECTOR, "#SMARTFILTER_FORM > .row:first-child > div:nth-child(10) #modef a") 

    # Фильтр Размер
    SIZE_FILTER_CHECKBOX = (By.CSS_SELECTOR, "#SMARTFILTER_FORM > .row:first-child > div:nth-child(11) .checkbox input:not([disabled])") 
    SIZE_FILTER_CLEAR = (By.CSS_SELECTOR, "#SMARTFILTER_FORM > .row:first-child > div:nth-child(11) > .senat-filter-parameters-box-title a") 
    SIZE_FILTER_APPLY = (By.CSS_SELECTOR, "#SMARTFILTER_FORM > .row:first-child > div:nth-child(11) #modef a") 

    # Кнопки Фильтров
    FILTER_APPLY_BUTTON = (By.CSS_SELECTOR, ".btn-filter-apply") 
    FILTER_CLEAR_BUTTON = (By.CSS_SELECTOR, ".btn-filter-clear") 

    # Панель тегов фильтров
    FILTER_TAG = (By.CSS_SELECTOR, "#DESCTOP_SUBFILTER_INNER .senat-filter-selected-item:not([style])") 
    FILTER_TAG_DELETE_APPLY = (By.CSS_SELECTOR, "#SUBFILTER_APPLY") 
    FILTER_TAGS_RESET = (By.CSS_SELECTOR, ".senat-filter-selected-reset:not(.submitfilter)") 

## Панель сортировки
    SORT_TYPE_LINK = (By.CSS_SELECTOR, ".sort__link:not(.active)") 
    SORT_TYPE_PRICE_DESCENDING = (By.CSS_SELECTOR, ".sort__item:nth-child(3) .sort__link") 
    SORT_TYPE_PRICE_ASCENDING = (By.CSS_SELECTOR, ".sort__item:nth-child(2) .sort__link") 


class JewelryCardAndAddToCartPopupsLocators():
    """ 
    Элементы каталога представляют собой карточки товара. 
    Эти локаторы используются в каталоге, промо-слайдерах, в поиске, в избранном
    """

    # Карточка товара
    JEWELRY_CARD = (By.CSS_SELECTOR, "[data-entity='item']")
    JEWELRY_CARD_ADD_TO_FAVORITES_BUTTON = (By.CSS_SELECTOR, "[data-entity='item'] .senat-item-label.favor.LIKE") # На странице Избранное не используется
    JEWELRY_CARD_TAKE_FROM_FAVORITES_BUTTON = (By.CSS_SELECTOR, "[data-entity='item'] .senat-item-label.favor.LIKE.active") # На странице Избранное не используется
    JEWELRY_CARD_JEWELRY_PAGE_LINK = (By.CSS_SELECTOR, "[data-entity='item'] a.senat-item-image-wrapper")
    JEWELRY_CARD_ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[data-entity='item'] span.btn")

    # Попап выбора размера - через карточку товара
    JEWELRY_SIZE_POPUP = (By.CSS_SELECTOR, ".senat-catalog__modal.active .catalogModal_sizes") # У товара без размера данного попапа не будет
    JEWELRY_SIZE_POPUP_CLOSE = (By.CSS_SELECTOR, ".active .catalogModal__btn_close")
    JEWELRY_SIZE_POPUP_HOW_TO_CHOOSE_URL = (By.CSS_SELECTOR, ".active .catalogModal__whatSize a")
    JEWELRY_SIZE_POPUP_SIZE_CARD = (By.CSS_SELECTOR, ".active .catalogModal__sizesList .catalogModal__sizesLink")
    JEWELRY_SIZE_POPUP_SIZE_ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".active button:not(.inactive)") # Нужно обязательно выбрать размер

    # Попап добавления в корзину - после выбора размера
    JEWELRY_ADDED_TO_CART_POPUP = (By.CSS_SELECTOR, "#ADD2BASKET_POPUP")
    JEWELRY_ADDED_TO_CART_POPUP_CLOSE = (By.CSS_SELECTOR, ".fancybox-button.fancybox-close-small")
    JEWELRY_ADDED_TO_CART_POPUP_JEWELRY_CARD = (By.CSS_SELECTOR, ".popup-slider-list > div")
    JEWELRY_ADDED_TO_CART_POPUP_CONTINUE_SHOPPING_BUTTON = (By.CSS_SELECTOR, ".popup-buttons button")
    JEWELRY_ADDED_TO_CART_POPUP_GO_TO_CART_BUTTON = (By.CSS_SELECTOR, ".popup-buttons > a")

class PaginationContainerLocators():
    """
    Локаторы для взаимодействия с меню пагинации. 
    Используются в каталоге, поиске, избранном.
    """
    PAGINATION_CONTAINER = (By.CSS_SELECTOR, ".senat-page-navigation")
    PAGINATION_PREVIOUS_PAGE_BUTTON = (By.CSS_SELECTOR, ".senat-page-previous")
    PAGINATION_NEXT_PAGE_BUTTON = (By.CSS_SELECTOR, ".senat-page-next")
    PAGINATION_ALL_ITEMS_BUTTON = (By.CSS_SELECTOR, ".senat-page-all")


class CatalogPageLocators():
    """
    Локаторы для взаимодействия с карточками товара в Каталоге 
    находятся в классе JewelryCardAndAddToCartPopupsLocators.
    Используются локаторы фильтров из FiltersAndSortingLocators.
    А также используются локаторы пагинации из PaginationContainerLocators.
    """
    

class JewelryCardPageLocators():
    """
    Локаторы для страницы товара
    """
    # Ссылка на попап выбора размера
    JEWELRY_PAGE_HOW_TO_KNOW_SIZE_POPUP_LINK = (By.CSS_SELECTOR, ".raz a")
    
    # Кнопка с размером
    JEWELRY_PAGE_SIZES_CONTAINER_ELEMENT = (By.CSS_SELECTOR, ".cat-element-offer-list > li")
    
    # Кнопка добавления в корзину
    JEWELRY_PAGE_ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-buy-wrap .btn.btn-link")
    
    # Локаторы для покупки в 1 клик
    JEWELRY_PAGE_BUY_IN_ONE_CLICK_POPUP_OPEN_BUTTON = (By.CSS_SELECTOR, "#oneclick-start")
    JEWELRY_PAGE_BUY_IN_ONE_CLICK_POPUP = (By.CSS_SELECTOR, "#one-click")
    JEWELRY_PAGE_BUY_IN_ONE_CLICK_POPUP_CLOSE_BUTTON = (By.CSS_SELECTOR, "#one-click .fancybox-close-small")
    JEWELRY_PAGE_BUY_IN_ONE_CLICK_NAME_INPUT_FIELD = (By.CSS_SELECTOR, "#ONECLICK_INNER > form > div:nth-child(2) input")
    JEWELRY_PAGE_BUY_IN_ONE_CLICK_PHONE_INPUT_FIELD = (By.CSS_SELECTOR, "#ONECLICK_INNER > form > div:nth-child(3) input")
    JEWELRY_PAGE_BUY_IN_ONE_CLICK_EMAIL_INPUT_FIELD = (By.CSS_SELECTOR, "#ONECLICK_INNER > form > div:nth-child(4) input")
    JEWELRY_PAGE_BUY_IN_ONE_CLICK_COMMENT_INPUT_FIELD = (By.CSS_SELECTOR, "#ONECLICK_INNER > form > div:nth-child(5) textarea")
    JEWELRY_PAGE_BUY_IN_ONE_CLICK_AGREEMENT_CHECKBOX = (By.CSS_SELECTOR, "#ONECLICK_CHECKBOX")
    JEWELRY_PAGE_BUY_IN_ONE_CLICK_SEND_DATA_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    JEWELRY_PAGE_BUY_IN_ONE_CLICK_AFTER_POPUP_CLOSE_BUTTON = (By.CSS_SELECTOR, "button[type='button'][title='Close']")

    # Добавление вы избранное
    JEWELRY_PAGE_ADD_TO_FAVORITES_BUTTON = (By.CSS_SELECTOR, ".cat-element-control .cat-element-favorite.favor")    
    JEWELRY_PAGE_TAKE_FROM_FAVORITES_BUTTON = (By.CSS_SELECTOR, ".cat-element-control .cat-element-favorite.favor.active")
    
    # Информация о доставке
    JEWELRY_PAGE_SHIPPING_DETAILS_LINK = (By.CSS_SELECTOR, ".cat-element-delivery-link")
    

class CartPageLocators():
    """
    Локаторы для корзины (оформления заказа)
    """

    CART_PAGE_JEWELRY_IN_CART_CARD = (By.CSS_SELECTOR, "[data-entity='basket-item']")
    CART_PAGE_JEWELRY_IN_CART_LINK = (By.CSS_SELECTOR, ".basket-item-block-image > a")

    CART_PAGE_JEWELRY_IN_CART_ITEM_QUANTITY_MINUS_BUTTON = (By.CSS_SELECTOR, "[data-entity='basket-item-quantity-minus']")
    CART_PAGE_JEWELRY_IN_CART_ITEM_QUANTITY_PLUS_BUTTON = (By.CSS_SELECTOR, "[data-entity='basket-item-quantity-plus']")
    
    CART_PAGE_JEWELRY_IN_CART_ADD_TO_FAVORITES_BUTTON = (By.CSS_SELECTOR, ".product__bottom_desktop .favor.CART.text-favor.addInFav__text")
    CART_PAGE_JEWELRY_IN_CART_TAKE_FROM_FAVORITES_BUTTON = (By.CSS_SELECTOR, ".product__bottom_desktop .favor.CART.text-favor.addInFav__text.active")
    
    CART_PAGE_JEWELRY_IN_CART_DELETE_FROM_CART_BUTTON = (By.CSS_SELECTOR, ".product__bottom_desktop [data-entity='basket-item-delete']")
    
    # Промокоды
    CART_PAGE_PROMO_CODE_INPUT_FIELD = (By.CSS_SELECTOR, "#COUPON_INPUT")
    CART_PAGE_PROMO_CODE_APPLY_BUTTON = (By.CSS_SELECTOR, "#COUPON_SET")
    
    # Поле ввода адреса доставки (по умолчанию стоит выбранный при первом заходе на сайт город)
    CART_PAGE_JEWELRY_IN_CART_CITY_INPUT_FIELD = (By.CSS_SELECTOR, "input.bx-ui-sls-fake")

    # Доставка в отделение Почты России (нужно проверить!!! кривые очень элементы - нужно наводиться на видимый элемент)
    CART_PAGE_OTHER_CITY_POST_CHOICE_POPUP_OPEN_BUTTON = (By.CSS_SELECTOR, "#russianpost_btn_openmap")
    CART_PAGE_OTHER_CITY_POST_CHOICE_POPUP = (By.CSS_SELECTOR, "#popup-message")
    CART_PAGE_OTHER_CITY_POST_CHOICE_POPUP_FULL_WINDOW_OPEN_BUTTON = (By.CSS_SELECTOR, "#full-btn")
    CART_PAGE_OTHER_CITY_POST_POINT_POPUP_CLOSE_BUTTON = (By.CSS_SELECTOR, ".popup-window-titlebar-close-icon")
    CART_PAGE_OTHER_CITY_POST_POINT_POPUP_CHOICE_MARK = (By.CSS_SELECTOR, "ymaps.ymaps-2-1-79-places-pane")
    CART_PAGE_OTHER_CITY_POST_POINT_POPUP_CHOICE_BUTTON = (By.CSS_SELECTOR, ".balloon button")


    # Выбор доставки курьером Почты России форма
    # Поля ввода адреса
    
    # Кнопка выбора вида доставки
    CART_PAGE_NN_COURIER_BUTTON = (By.CSS_SELECTOR, '#bx-soa-delivery .bx-soa-pp-item-container > div:nth-child(3)')
    CART_PAGE_NOT_NN_COURIER_BUTTON = (By.CSS_SELECTOR, '#bx-soa-delivery .bx-soa-pp-item-container > div:nth-child(2)')
    CART_PAGE_ADDRESS_FORM_ZIP_INPUT_FIELD = (By.CSS_SELECTOR, "input#soa-property-ZIP")

    # Общие поля для ввода адреса в случае доставки курьером
    CART_PAGE_CITY_ADDRESS_FORM = (By.CSS_SELECTOR, "[id='props_block']")
    CART_PAGE_CITY_ADDRESS_FORM_STREET_INPUT_FIELD = (By.CSS_SELECTOR, "input#soa-property-22")
    CART_PAGE_CITY_ADDRESS_FORM_APARTMENT_INPUT_FIELD = (By.CSS_SELECTOR, "input#soa-property-23")
    CART_PAGE_CITY_ADDRESS_FORM_FLOOR_INPUT_FIELD = (By.CSS_SELECTOR, "input#soa-property-24")
    CART_PAGE_CITY_ADDRESS_FORM_ENTRANCE_INPUT_FIELD = (By.CSS_SELECTOR, "input#soa-property-25")
    CART_PAGE_CITY_ADDRESS_FORM_INTERCOM_INPUT_FIELD = (By.CSS_SELECTOR, "input#soa-property-26")
    # Кнопка сохранения адреса
    CART_PAGE_CITY_ADDRESS_FORM_SAVE_BUTTON = (By.CSS_SELECTOR, "a.bx-soa-props-submit")

    # Выбор альтернативного эквайринга для оплаты
    CART_PAGE_PAY_METHOD_CHECKBOX = (By.CSS_SELECTOR, "#order-paysystem .howToPay__type input:not([checked])")
    
## ВВОД ДАННЫХ ПОЛУЧАТЕЛЯ

    # Пользователь незарегистрирован/неавторизован
    CART_PAGE_CHECKOUT_BUTTON = (By.CSS_SELECTOR, '[data-entity="basket-checkout-button"]')
    CART_PAGE_RECIPIENT_PHONE_INPUT_FIELD = (By.CSS_SELECTOR, "input#sign-bycode-phone")
    CART_PAGE_RECIPIENT_PHONE_SEND_BUTTON = (By.CSS_SELECTOR, "div.lk-form-button input:not([disabled])")
    CART_PAGE_RECIPIENT_PHONE_CHANGE_BUTTON = (By.CSS_SELECTOR, ".signin-byphonecode-to-sign")
    CART_PAGE_RECIPIENT_PHONE_SMS_CODE_INPUT_FIELD = (By.CSS_SELECTOR, "#signin-byphonecode-code")

    CART_PAGE_RECIPIENT_PHONE_RESEND_CODE = (By.CSS_SELECTOR, ".resend-code-available > a") # есть несколько элементов, однако нужен первый элемент, так что годится
    CART_PAGE_RECIPIENT_PHONE_SEND_SMS_CODE_BUTTON = (By.CSS_SELECTOR, "[value='Подтвердить']:not([disabled])") #тут такой же адрес кнопки


    # Пользователь авторизован
    # Ввод имени-почты
    CART_PAGE_RECIPIENT_NAME_INPUT_FIELD = (By.CSS_SELECTOR, "#cart-personal-details-name")
    CART_PAGE_RECIPIENT_EMAIL_INPUT_FIELD = (By.CSS_SELECTOR, "#cart-personal-details-email")

    # Блок итого
    CART_PAGE_PROMO_CODE_DELETE_BUTTON = (By.CSS_SELECTOR, "[data-entity='basket-coupon-delete']")
    CART_PAGE_AGREEMENT_CHECKBOX = (By.CSS_SELECTOR, ".allPrice__agreement input")
    CART_PAGE_AGREEMENT_CHECKBOX_NEED_TO_APPROVE_POPUP_WARNING = (By.CSS_SELECTOR, "#popup-window-titlebar-popup-message-2")
    # Кнопка оформления заказа
    CART_PAGE_SEND_OFFER_BUTTON = (By.CSS_SELECTOR, "a.btn-order-save")
    
# Ошибки при оформлении заказа: попап и предупреждения

    # Нет возможности привязаться к конкретному предупреждению в форме доставки
    CART_PAGE_CITY_ADDRESS_FORM_ERROR_WARNING = (By.CSS_SELECTOR, ".errorBox_fromCourier.active") 
    CART_PAGE_PROMO_CODE_INPUT_FIELD_WARNING = (By.CSS_SELECTOR, "#COUPON_ERROR_TEXT")
    CART_PAGE_DELIVERY_NEED_TO_APPROVE_WARNING = (By.CSS_SELECTOR, "#c-errors")


class PersonalCabinetLocators():
    """
    Локаторы для страницы личного кабинета и вложенных страниц
    """
    # Блок Sidebar-menu
    PERSONAL_CABINET_PERSONAL_DATA_PAGE_LINK = (By.CSS_SELECTOR, ".lk .lk-nav a[href='/personal/user/']")
    PERSONAL_CABINET_ORDERS_PAGE_LINK = (By.CSS_SELECTOR, ".lk .lk-nav a[href='/personal/orders/']")
    PERSONAL_CABINET_FAVORITES_PAGE_LINK = (By.CSS_SELECTOR, ".lk .lk-nav a[href='/favorites/']")
    PERSONAL_CABINET_LOGOUT_LINK = (By.CSS_SELECTOR, ".lk .lk-nav a[href='/?logout=yes']")
    
    # Страница Личные данные
    PERSONAL_DATA_PAGE_NAME_INPUT_FIELD = (By.CSS_SELECTOR, "#profileedit-name")
    PERSONAL_DATA_PAGE_GENDER_FEMALE_RADIOBUTTON = (By.CSS_SELECTOR, "#sexFemale")
    PERSONAL_DATA_PAGE_GENDER_MALE_RADIOBUTTON = (By.CSS_SELECTOR, "#sexMale")
    PERSONAL_DATA_PAGE_EMAIL_INPUT_FIELD = (By.CSS_SELECTOR, "#profileedit-email")
    PERSONAL_DATA_PAGE_BIRTHDATE_INPUT_FIELD = (By.CSS_SELECTOR, "#profileedit-birthday")
    PERSONAL_DATA_PAGE_BIRTHDATE_INPUT_DROPDOWN_MODULE = (By.CSS_SELECTOR, "#ui-datepicker-div")
    PERSONAL_DATA_PAGE_SAVE_BUTTON = (By.CSS_SELECTOR, ".lk-form-button .lk-btn[value='Сохранить']")

    # Страница Мои заказы
    ORDERS_PAGE_ORDER_CARD = (By.CSS_SELECTOR, ".lk-orders-item")
    ORDERS_PAGE_ORDER_CARD_PRODUCT_CARD = (By.CSS_SELECTOR, ".lk-orders-product")
    ORDERS_PAGE_ORDER_CARD_JEWELRY_PAGE_LINK = (By.CSS_SELECTOR, ".lk-orders-product-img")
    ORDERS_PAGE_ORDER_CARD_JEWELRY_PAGE_ALT_LINK = (By.CSS_SELECTOR, ".lk-orders-product-name a")
    ORDERS_PAGE_ORDER_CARD_INFO = (By.CSS_SELECTOR, ".lk-orders-info")
    ORDERS_PAGE_ORDER_CARD_STATUS_CONTAINER = (By.CSS_SELECTOR, ".lk-orders-item .lk-orders-status")
    ORDERS_PAGE_ORDER_CARD_PAY_BUTTON = (By.CSS_SELECTOR, ".lk-orders-link-btn")
    ORDERS_PAGE_ORDER_CARD_ORDER_LINK = (By.CSS_SELECTOR, ".lk-orders-link a:last-child")
    ORDERS_PAGE_PAGINATION_CONTAINER = (By.CSS_SELECTOR, ".lk-orders-link a:last-child")
    ORDERS_PAGE_PAGINATION_PREVIOUS_BUTTON = (By.XPATH, "//a[contains(text(),'Предыдущая')]")
    ORDERS_PAGE_PAGINATION_NEXT_BUTTON = (By.XPATH, "//a[contains(text(),'Следующая')]")

    # Страница Заказа
    ORDER_PAGE_PAY_BUTTON = (By.CSS_SELECTOR, ".lk-payment-btn")


class FavoritesPageLocators():
    """
    Локаторы для страницы избранное в основном находятся в классе JewelryCardAndAddToCartPopupsLocators.
    Используются локаторы сортировки из FiltersAndSortingLocators.
    А также используются локаторы пагинации из PaginationContainerLocators.
    """
    FAVORITES_PAGE_JEWELRY_CARD_DELETE_FROM_FAVORITES_BUTTON = (By.CSS_SELECTOR, ".LIKE.active")
    

class FooterLocators():
    """
    Локаторы на ссылки в футере
    """
    pass

class StoresPageLocators():
    """
    
    """
    pass

class ThankForYourPurchase():
    """
    Локаторы на странице переправления на страницу оплаты
    """

    GO_TO_PAY_PAGE_BUTTON = (By.CSS_SELECTOR, ".order-pay-form a")