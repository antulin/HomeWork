from selenium import webdriver
import time
import math
import os


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir + '\\file', 'file.txt')          # добавляем к этому пути имя файла 
    print(file_path)
    
    elements = browser.find_elements_by_css_selector (".form-group .form-control")
    for element in elements:
       element.send_keys("q")
       
    element = browser.find_element_by_css_selector("#file")
    element.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()
    time.sleep(10)
    
finally:
    time.sleep(10)
    browser.quit()