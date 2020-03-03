from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
import os


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    element = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), '$100')
        )
    button = WebDriverWait(browser, 12).until(
            EC.element_to_be_clickable((By.ID, "book"))
        )
    button.click()
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)
    print(y)
    
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
    
    button = browser.find_element_by_css_selector('#solve')
    button.click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    print (alert_text)
	
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir + '\\file', 'file.txt')          # добавляем к этому пути имя файла
    file_alert = open(file_path, "w")
    # Открываем файл "file.txt" для записи. "w" - переписать, "a" - дописать в конец.
    # Всегда используем слеши вперед, даже на виндовсе
    # Если такого файла нет и прав достаточно, то он создастся. Если нет - будет ошибка.
    # Проверить наличие файла можно функцией exists(path) из os.path

    file_alert.write(str(alert_text))
    # Записываем сюда что-то, предварительно преобразовав в строку командой str(x)

    file_alert.close()

finally:
    time.sleep(2)
    browser.quit()