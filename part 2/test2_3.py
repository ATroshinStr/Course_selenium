# импорт вебдрайвер и времени
from selenium import webdriver
#подключение библиотеки селект для выбора элементов из списка
from selenium.webdriver.support.ui import Select
import time 
import math

#Создаем переменную с ссылкой на страницу
link = "http://suninjuly.github.io/selects1.html"
#Создаем переменную, в котором путь до вебдрайвера
browser = webdriver.Chrome('/Users/alexnder/Documents/python/chromedriver')
#Получение ссылки для взаимодействие с вебдрайвером
browser.get(link)

try:
    #Поиск двух чисел
    n1 = browser.find_element_by_id('num1')
    n2 = browser.find_element_by_id('num2')
    #Перевод чисел в инт
    n1_2 = int(n1.text)
    n2_2 = int(n2.text)
    #Сложение чисел и перевод их суммы в стр
    sum = n1_2 + n2_2
    sum = str(sum)
    #Поиск селекта
    browser.find_element_by_class_name('custom-select').click()
    #Подключение селекта. Поиск по всем значениям селекта нужное значение
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum)
    #Поиск и нажатие на кнопку
    browser.find_element_by_class_name('btn-default').click()
    
finally:    
    time.sleep(15)
    browser.quit()
    #Закрытие теста