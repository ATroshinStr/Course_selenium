# импорт вебдрайвер и времени
from selenium import webdriver
import time 
import math

#Создаем переменную с ссылкой на страницу
link = "http://suninjuly.github.io/redirect_accept.html"
#Создаем переменную, в котором путь до вебдрайвера
browser = webdriver.Chrome('/Users/alexnder/Documents/python/chromedriver')
#Получение ссылки для взаимодействие с вебдрайвером
browser.get(link)

try:
    #Определение окна браузера и работа с первым окном
    first_window = browser.window_handles[0]
    browser.execute_script("document.getElementsByTagName('button')[0].classList.remove('trollface');")
    browser.find_element_by_class_name('btn-primary').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

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

    button = browser.find_element_by_class_name('btn-primary').click()


finally:
    time.sleep(15)
    browser.quit()