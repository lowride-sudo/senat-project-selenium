# Данный скрипт автоматизирует выполнение перехода по любой ссылке на главной странице в зависимости от необходимости.

import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


main_page = "https://senatnn.ru/"


try:
    driver = webdriver.Chrome()
    driver.get(main_page)

# Jivosite должен успеть подгрузиться чтобы мы его отключили, поэтому ставим таймер
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.TAG_NAME, "jdiv")))
    driver.execute_script("document.getElementsByTagName('jdiv')[0].remove()")
    

#HEADER
    # WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.LINK_TEXT, "Акции"))).click() # Переход по ссылке в Акции
    # WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.LINK_TEXT, "Новинки"))).click() 
    # WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.LINK_TEXT, "Магазины"))).click() 
    # WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.LINK_TEXT, "О компании"))).click() 

    # WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.logo"))).click() #ссылка в логотипе на главную 

    # WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".header-control #want"))).click() # Избранное 
    # WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".header-control #bx_basketFKauiI"))).click() # Корзина 
    
    # # Переходим в категорию каталога через выпадающий блок "Каталог"
    # action = ActionChains(driver)
    # header_catalog_block = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".main-menu-list__item.nonehref-li:nth-child(1)")))
    # action.move_to_element(header_catalog_block).perform() # 
    # header_catalog_block_categories = driver.find_elements(By.XPATH, "//*[@class='main-submenu']//a")
    # random.choice(header_catalog_block_categories).click()

    # # Переходим в категорию каталога через выпадающий блок "Свадьба", 1й уровень ссылок
    # action = ActionChains(driver)
    # header_wedding_block = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".main-menu-list__item.nonehref-li:nth-child(2)")))
    # action.move_to_element(header_wedding_block).perform()
    # header_wedding_block_categories = driver.find_elements(By.XPATH, "//li[@data-elemsection='white-section-bottom']//ul[@class='main-submenu-section']//li[@class='hover-submenu-trigger' and not (@data-contentclass)]/a")
    # random.choice(header_wedding_block_categories).click()

    
    
    # # Переходим в категорию каталога через выпадающий блок "Свадьба", выпадающий блок "Украшения для невесты"
    # action = ActionChains(driver)
    # header_wedding_block = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".main-menu-list__item.nonehref-li:nth-child(2)")))
    # action.move_to_element(header_wedding_block).perform()
    # bride_jewels_block = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//*[@data-contentclass='bride']")))
    # action.move_to_element(bride_jewels_block).perform()
    # header_wedding_block_url = driver.find_elements(By.CSS_SELECTOR, ".bride.hidden-content-menu > ul > li > a")
    # random.choice(header_wedding_block_url).click()

    # Переходим в категорию каталога через выпадающий блок "Свадьба", выпадающий блок "Украшения для жениха"
    action = ActionChains(driver)
    header_wedding_block = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".main-menu-list__item.nonehref-li:nth-child(2)")))
    action.move_to_element(header_wedding_block).perform()
    groom_jewels_block = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//*[@data-contentclass='groom']")))
    action.move_to_element(groom_jewels_block).perform()
    driver.find_element(By.CSS_SELECTOR, ".groom.hidden-content-menu > ul > li > a").click()

    # # Кликаем ссылку Коллекции
    # WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//*[@class='main-menu-item href'][text()='Коллекции']"))).click() # Коллекции
    
    # Используем поле поиска
    # search_phrase = 'something' #Фраза для поиска
    # search_field = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//input[@class='inpt'][@placeholder='Поиск']"))) # Локатор поля Поиск 
    # search_field.send_keys(search_phrase) # Вводим фразу
    # search_field.submit() # Отправляем фразу 


#BODY
    # Активная акция в слайдере
    # WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".slick-current.slick-active"))).click() 

    # Блок Коллекции: выбираем и кликаем на случайную карточку
    # collection_cards = driver.find_elements(By.CSS_SELECTOR, ".collection-list > .col-item") # Массив с коллекциями
    # random.choice(collection_cards).click()

    # Блок Каталог: выбираем и кликаем на случайную карточку
    # catalog_cards = driver.find_elements(By.CSS_SELECTOR, ".senat-section-list > .senat-section-item") # Массив с карточками каталога
    # random.choice(catalog_cards).click()

    # Блок Акции: выбираем и кликаем на случайную карточку
    # promotions_cards = driver.find_elements(By.CSS_SELECTOR, ".svk.akcii .item") # Массив с акциями
    # random.choice(promotions_cards).click()

    # Блок Подарки за регистрацию, заполняем и отправляем телефон
    # WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "PHONE_FID11"))).send_keys("+71234567890")
    # driver.find_element(By.ID, 'PHONE_FID11').send_keys("+71234567890")
    # driver.find_element(By.CSS_SELECTOR, "input.fb_close.afbf_btn").click()

    # Блок Сервис: выбираем и кликаем на случайную карточку
    # service_cards = driver.find_elements(By.CSS_SELECTOR, ".main-link-list > .main-link-item") # Массив с акциями
    # random.choice(service_cards).click()
    
#FOOTER
    # WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//*[@class='col col-xs-3']//*[text()='Философия']"))).click()
    # WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//*[@class='col col-xs-3']//*[text()='Сотрудничество']"))).click()
    # WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//*[@class='col col-xs-3']//*[text()='Отзывы']"))).click()
    # WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//*[@class='col col-xs-3']//*[text()='Политика конфиденциальности']"))).click()
    
    # WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//*[@class='col col-xs-3']//*[text()='Акции']"))).click()
    # WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//*[@class='col col-xs-3']//*[text()='Новости']"))).click()
    # WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//*[@class='col col-xs-3']//*[text()='Адреса магазинов']"))).click()

    # WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//*[@class='col col-xs-3']//*[text()='Сертификаты']"))).click()
    # WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//*[@class='col col-xs-3']//*[text()='Ювелирная мастерская']"))).click()
    # WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//*[@class='col col-xs-3']//*[text()='Памятка покупателя']"))).click()
    # WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//*[@class='col col-xs-3']//*[text()='Программа лояльности']"))).click()
    # WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//*[@class='col col-xs-3']//*[text()='Доставка и оплата']"))).click()
    
    # WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//*[@class='col col-xs-3']//*[text()='Вакансии']"))).click()

    # WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".footer-logo"))).click() # Ссылка в логотипе футера на главную 

    
finally:
    time.sleep(10)
    driver.quit()
