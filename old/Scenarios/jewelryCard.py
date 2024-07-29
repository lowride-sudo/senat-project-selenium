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

try:
    driver = webdriver.Chrome()
    driver.get(catalog)
    driver.implicitly_wait(5)


    # Jivosite должен успеть подгрузиться чтобы мы его отключили, поэтому ждем его появления
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.TAG_NAME, "jdiv")))
    driver.execute_script("document.getElementsByTagName('jdiv')[0].remove()")
    driver.execute_script("document.querySelector('.header-bottom').remove()") # Удаляем Header чтобы не мешал


# Заходим в случайную карточку изделия
    jewelry_cards_links = driver.find_elements(By.CSS_SELECTOR, ".senat-cat-item .senat-item-image-wrapper")
    random.choice(jewelry_cards_links).click()

# Можем кликнуть и посмотреть условия рассрочки
    # driver.find_element(By.CLASS_NAME, "credit").click()

# Если есть размер изделия создаем список размеров, случайным образом выбираем размер и кликаем его
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-item-detail-info-container-title")))
    if driver.find_element(By.CSS_SELECTOR, ".product-item-detail-info-container-title").text == "Размер":
        sizes = driver.find_elements(By.CSS_SELECTOR, ".offer-list-item")
        # нужно убрать размер "-" из массива собранных размеров, если только он не единственный размер.
        if len(sizes) > 2:
            sizes[random.randint(0, len(sizes) - 1)].click()
        else:
            sizes[0].click()
    
# Кликаем на картинку и закрываем ее (сейчас это ломает сценарии покупки на странице)
    # driver.find_element(By.CSS_SELECTOR, ".slick-track > a.gallery-fancyboxArray").click()
    # driver.find_element(By.CSS_SELECTOR, "[data-fancybox-close]").click()

# Добавляем изделие в корзину(это сценарий для одного изделия)
    # driver.find_element(By.CSS_SELECTOR, ".btn.btn-link").click()
    # # Закрываем вылезший попап
    # time.sleep(1)
    # # WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".popup-window .popup-window-titlebar-close-icon")))
    # driver.find_element(By.CSS_SELECTOR, ".popup-window .popup-window-titlebar-close-icon").click() #Закрываем окно попапа крестиком 
    
    
# Добавляем изделие в избранное
    driver.find_element(By.CSS_SELECTOR, ".cat-element-favorite.favor").click()
    driver.find_element(By.CSS_SELECTOR, ".cat-element-favorite.favor").click()

# СЦЕНАРИЙ ПОКУПКИ В 1 КЛИК 
    # driver.find_element(By.CSS_SELECTOR, ".btn.show-order-form").click()
    # driver.find_element(By.ID, "one_click_order_1").send_keys("Test Automation")
    # driver.find_element(By.ID, "one_click_order_2").send_keys("7777777777")
    # driver.find_element(By.ID, "one_click_order_3").send_keys("test@test.test")
    # driver.find_element(By.ID, ".nx-call-submit-outer.orange input").click()

# Можем кликнуть и перейти по промо-карточке в акцию
    # driver.find_element(By.CSS_SELECTOR, "div.ack").click()

# Взаимодействуем со слайдером допредложений
    # first_slider_slicks = driver.find_elements(By.CSS_SELECTOR, "section .slick-dots li > button")
    # for i in range(5, -1, -1):
    #     time.sleep(0.5)
    #     first_slider_slicks[i].click()

    # second_slider_slicks = driver.find_elements(By.CSS_SELECTOR, "section .slick-dots li > button")
    # for i in range(11, 5, -1):
    #     time.sleep(0.5)
    #     second_slider_slicks[i].click()

# Кликнуть случайное изделие из доппредложений
    additional_jewelry_list = driver.find_elements(By.CSS_SELECTOR,".list-similar .slick-slide.slick-active > a")
    random.choice(additional_jewelry_list).click()

    


finally:
    time.sleep(5)
    driver.quit()
