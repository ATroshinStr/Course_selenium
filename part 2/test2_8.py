# импорт вебдрайвер и времени
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time 
import math

#Создаем переменную с ссылкой на страницу
link = "http://suninjuly.github.io/explicit_wait2.html"
#Создаем переменную, в котором путь до вебдрайвера
browser = webdriver.Chrome('/Users/alexnder/Documents/python/chromedriver')
#Получение ссылки для взаимодействие с вебдрайвером
browser.get(link)

try:
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    ) 
    browser.find_element_by_tag_name('button').click()

    browser.execute_script("window.scrollBy(0, 150);")
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    #Поиск селектора, в котором находится Х и его значения
    takeX = browser.find_element_by_id('input_value')
    #Получение значения Х
    x = takeX.text
    #Получение решения уравнения
    y = calc(x)
    #Поиск формы и ввод значения Y
    browser.find_element_by_id('answer').send_keys(y)
    browser.find_element_by_id('solve').click()

finally:
    time.sleep(5)
    browser.quit()
