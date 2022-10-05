# Данный скрипт проверяет добавление нескольких товарных изделий в корзину, ввод пользовательских данных
# и оформление заказа.

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

catalog = "https://senatnn.ru/catalog/ukrasheniya/"
ordering = 'https://senatnn.ru/cart/ordering/'
jewelry_amount = 3

#функция для добавления в корзину N позиций
def buy_jewelry(n:int):
    for i in (range(1, n+1)):
        driver.find_element(By.CSS_SELECTOR, f".senat-cat-item:nth-child({i}) .btn-can-buy").click()
        time.sleep(1)
        popups = driver.find_elements(By.CSS_SELECTOR, ".popup-window .popup-window-titlebar-close-icon")
        popups[i-1].click()

try:
    driver = webdriver.Chrome()
    driver.get(catalog)

# Jivosite должен успеть подгрузиться чтобы мы его отключили, поэтому ставим таймер
    time.sleep(5) 
    driver.execute_script("document.getElementsByClassName('globalClass_dc4a')[0].remove()",)
    
# Добавляем n изделий в корзину    
    buy_jewelry(jewelry_amount)

# Переходим на страницу оформления заказа
    driver.get(ordering)
    time.sleep(3)
    
# Создаем массив с локаторами полей ввода
    input_fields = driver.find_elements(By.CSS_SELECTOR, ".r3x1 input")  

# Задаём данные тестового пользователя
    credentials = ["automated test user", "test@test.test", "+71234567890"] 
    
# Заносим данные пользователя в поля 
    for i in range(3):
        input_fields[i].send_keys(credentials[i])

# Оформляем заказ
    driver.find_element(By.CSS_SELECTOR, ".checkout").click()

finally:
    time.sleep(10)
    driver.quit()
