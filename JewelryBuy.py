# Данный скрипт проверяет добавление N товарных изделий в корзину через страницу товарной позиции: заходит в каталог,
# заходит в товарную позицию, добавляет позицию в корзину.
import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


catalog = "https://senatnn.ru/catalog/ukrasheniya/"
ordering = 'https://senatnn.ru/cart/ordering/'

# количество товарных позиций к покупке
jewelry_amount = 3



# функция для добавления в корзину N позиций через карточку товара
def buy_jewelry(n:int):
    for i in (range(1, n+1)):
        # Переходим в товарную позицию из каталога
        driver.find_element(By.CSS_SELECTOR, f".senat-cat-item:nth-child({i}) a").click()
        
        # Если есть размер изделия создаем список размеров, случайным образом выбираем размер и кликаем его
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-item-detail-info-container-title")))
        if driver.find_element(By.CSS_SELECTOR, ".product-item-detail-info-container-title").text == "Размер":
            sizes = driver.find_elements(By.CSS_SELECTOR, ".offer-list-item")
            # нужно убрать размер "-" из массива собранных размеров, если только он не единственный размер.
            if len(sizes) > 2:
                sizes[random.randint(0, len(sizes) - 1)].click()
            else:
                sizes[0].click()
        
        # Добавляем изделие в корзину
        driver.find_element(By.CSS_SELECTOR, ".btn.btn-link").click()
        
        # Закрываем вылезший попап
        time.sleep(1)
        # WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".popup-window .popup-window-titlebar-close-icon")))
        popups = driver.find_elements(By.CSS_SELECTOR, ".popup-window .popup-window-titlebar-close-icon") #здесь мы создаем массив крестиков закрытия попапов, 
        popups[i-1].click() # здесь мы кликаем последний созданный крестик закрытия.
        
        #Возвращаемся на страницу назад
        driver.back()

        # ДЛЯ БУДУЩИХ СЦЕНАРИЕВ
        # Опционально: добавляем изделие в избранное
        # driver.find_element(By.CSS_SELECTOR, ".cat-element-favorite.favor").click()

        # СЦЕНАРИЙ ПОКУПКИ В 1 КЛИК, НУЖНО НАХОДИТЬСЯ НА СТРАНИЦЕ ИЗДЕЛИЯ 
        # driver.find_element(By.CSS_SELECTOR, ".btn.show-order-form").click()
        # driver.find_element(By.ID, "one_click_order_1").send_keys("Test Automation")
        # driver.find_element(By.ID, "one_click_order_2").send_keys("7777777777")
        # driver.find_element(By.ID, "one_click_order_3").send_keys("test@test.test")
        # driver.find_element(By.ID, ".nx-call-submit-outer.orange input").click()



try:
    driver = webdriver.Chrome()
    driver.get(catalog)

    # Jivosite должен успеть подгрузиться чтобы мы его отключили, поэтому ждем его появления
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.TAG_NAME, "jdiv")))
    driver.execute_script("document.getElementsByTagName('jdiv')[0].remove()")

    # Добавляем n изделий в корзину    
    buy_jewelry(jewelry_amount)

    
# Оформляем заказ через переход по ссылке на страницу оформления заказа.
    # Переходим на страницу оформления заказа
    # driver.get(ordering)
    # time.sleep(3)
    
    # Создаем массив с локаторами полей ввода
    # input_fields = driver.find_elements(By.CSS_SELECTOR, ".r3x1 input")  

    # Задаём данные тестового пользователя
    # credentials = ["automated test user", "test@test.test", "+71234567890"] 
    
    # Заносим данные пользователя в поля 
    # for i in range(3):
    #     input_fields[i].send_keys(credentials[i])

    # Оформляем заказ
    # driver.find_element(By.CSS_SELECTOR, ".checkout").click()

finally:
    time.sleep(5)
    driver.quit()
