import math
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try: 
    #link = "http://suninjuly.github.io/selects1.html"
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x = browser.find_element_by_css_selector("#num1")
    y = browser.find_element_by_css_selector("#num2")
    y = str(int(x.text) + int(y.text))
    print(y)
    
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(y) # ищем элемент с текстом "Python"
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
# ожидание чтобы визуально оценить результаты прохождения скрипта