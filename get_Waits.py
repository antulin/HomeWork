from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/cats.html'
    browser.implicitly_wait(5)
    browser.get(link)
    
    button = browser.find_element_by_id("button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()