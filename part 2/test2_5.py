# импорт вебдрайвер и времени
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

#Создаем переменную с ссылкой на страницу
link = "http://suninjuly.github.io/file_input.html"
#Создаем переменную, в котором путь до вебдрайвера
browser = webdriver.Chrome('/Users/alexnder/Documents/python/chromedriver')
#Получение ссылки для взаимодействие с вебдрайвером
browser.get(link)

try:
    browser.find_element_by_name('firstname').send_keys('123')
    browser.find_element_by_name('lastname').send_keys('123')
    browser.find_element_by_name('email').send_keys('123')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "test2_5.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element_by_id('file')
    element.send_keys(file_path)

    browser.find_element_by_class_name('btn-primary').click()

finally:
    time.sleep(10)
    browser.quit()    