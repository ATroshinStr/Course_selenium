# импорт вебдрайвер и времени
from selenium import webdriver
import time 
import math

#Создаем переменную с ссылкой на страницу
link = "http://suninjuly.github.io/execute_script.html"
#Создаем переменную, в котором путь до вебдрайвера
browser = webdriver.Chrome('/Users/alexnder/Documents/python/chromedriver')
#Получение ссылки для взаимодействие с вебдрайвером
browser.get(link)

try:    
    #Решение уравнения
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
    #Поиск и нажатие на чекбокс   
    browser.find_element_by_id('robotCheckbox').click()
    #Поиск и нажатие на радиокнопку
    browser.execute_script("window.scrollBy(0, 150);")
    checkbox = browser.find_element_by_id('robotsRule').click()
    #Поиск и нажати на кнопку "подтвердить"
    button = browser.find_element_by_class_name('btn-primary').click()

finally:    
    time.sleep(15)
    browser.quit()
    #Закрытие теста