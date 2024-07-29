# Данный скрипт автоматизирует выбор случайных чекбоксов в фильтре, добавление товара через кнопку

import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

site_page = "https://www.develop.senatnn.ru/catalog/ukrasheniya/"


#функция для добавления в корзину N позиций через страницу каталога
# def buy_jewelry(n:int):
#     for i in (range(1, n+1)):
#         driver.find_element(By.CSS_SELECTOR, f".senat-cat-item:nth-child({i}) .btn-can-buy").click()
#         time.sleep(1)
#         popups = driver.find_elements(By.CSS_SELECTOR, ".popup-window .popup-window-titlebar-close-icon")
#         popups[i-1].click()

try:
    driver = webdriver.Chrome()
    driver.get(site_page)
    driver.implicitly_wait(5)


# Jivosite должен успеть подгрузиться чтобы мы его отключили, поэтому ставим таймер
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "jdiv"))) # При применении сортировки, снова появляется jivosite plugin
    driver.execute_script("document.getElementsByTagName('jdiv')[0].remove()")
    

#BODY
    #FILTER: выбираем случайные фильтры и кликаем на них
    
    # # Разворачиваем каждый тип фильтра
    # driver.execute_script("const filter_nodelist = document.querySelectorAll('.senat-filter-parameters-box'); filter_nodelist.forEach(element => {element.classList.add('senat-active');});")    
    
    # # Разворачиваем случайный тип фильтра
    # random_number = random.randint(1, 5) #Выбираем случайное число N
    # driver.execute_script("document.querySelector('.header-bottom').remove()") # Удаляем Header чтобы не мешал
    # driver.execute_script(f"document.querySelector('.senat-filter-parameters-box:nth-child({random_number})').classList.add('senat-active');") # Открываем N-й фильтр
    # # Делаем массив с локаторами фильтра, выбираем раскрытый элемент и протыкиваем случайное число случайных в массиве 
    # filter_checkboxes = driver.find_elements(By.CSS_SELECTOR, f".senat-filter-parameters-box:nth-child({random_number}) .senat-filter-input-checkbox")
    # # Перебираем этот массив и кликаем по случайным фильтрам
    # for i in range(random.randrange(1, len(filter_checkboxes) + 1)): # Выбираем случайное число чекбоксов
    #     WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, f".senat-filter-parameters-box:nth-child({random_number}) .senat-filter-input-checkbox"))) # Ждем появление чекбокса
    #     filter_checkboxes[random.randrange(len(filter_checkboxes))].click() # Кликаем случайный чекбокс

    # #СОРТИРОВКА
    # action = ActionChains(driver)
    # sort_dropdown = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".senat-sort-item-title"))) 
    # action.move_to_element(sort_dropdown).perform()
    # dropdown_options = driver.find_elements(By.CSS_SELECTOR, "[data-role='bx_sort_block'] > a")
    # random.choice(dropdown_options).click()
    # WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "jdiv"))) # При применении сортировки, снова появляется jivosite plugin
    # driver.execute_script("document.getElementsByTagName('jdiv')[0].remove()")

    #CATALOG Добавляем случайное изделие в корзину из каталога
    jewelry_cards_buy = driver.find_elements(By.CSS_SELECTOR, ".senat-cat-item .btn-can-buy") # Создаем массив с кнопками добавления в корзину
    random.choice(jewelry_cards_buy).click() # Кликаем случайную кнопку "Добавить в корзину"
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".senat-catalog__modal.active .catalogModal_sizes"))).click()
    size_cards_list = driver.find_elements(By.CSS_SELECTOR, ".senat-catalog__modal.active .catalogModal_sizes") # Создаем массив с размерами
    random.choice(size_cards_list).click() # Выбираем случайный размер из массива
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".active button:not(.inactive)"))).click() # Нажимаем на кнопку выбора размера
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".popup-buttons > a"))).click() # нажимаем на кнопку "перейти в корзину"
    

    # Находимся в корзине
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".popup-buttons > a"))).click() # нажимаем на кнопку "перейти в корзину"



    # #Заходим в случайную карточку изделия
    # jewelry_cards_links = driver.find_elements(By.CSS_SELECTOR, ".senat-cat-item .senat-item-image-wrapper")
    # random.choice(jewelry_cards_links).click()
    # time.sleep(2)
    # driver.back()
        
    
finally:
    time.sleep(10)
    driver.quit()
