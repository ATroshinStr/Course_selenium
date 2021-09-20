# импорт вебдрайвер и времени
from selenium import webdriver
import time 

#путь до вебдрайвера
driver = webdriver.Chrome('/Users/alexnder/Documents/python/chromedriver')
#путь сайта 
driver.get('http://suninjuly.github.io/find_xpath_form')

#Заполяем форму и нажимаем отправить
input1 = driver.find_element_by_tag_name('input')
input1.send_keys("Ivan")
input2 = driver.find_element_by_name('last_name')
input2.send_keys("Petrov")
input3 = driver.find_element_by_class_name('city')
input3.send_keys("Smolensk")
input4 = driver.find_element_by_id('country')
input4.send_keys("Russia")
button = driver.find_element_by_xpath('//button[text()="Submit"]')
button.click()

time.sleep(10)
    # закрываем браузер после всех манипуляций
driver.quit()