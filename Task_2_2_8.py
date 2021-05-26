from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector('[placeholder="Enter first name"]')
    input1.send_keys('alex')

    input2 = browser.find_element_by_css_selector('[placeholder="Enter last name"]')
    input2.send_keys('lis')

    input3 = browser.find_element_by_css_selector('[placeholder="Enter email"]')
    input3.send_keys('blabla')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)



    button = browser.find_element_by_css_selector('button.btn')
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к
# директории текущего исполняемого файла

file_path = os.path.join(current_dir, 'file.txt') # добавляем к этому пути
# имя файла

element.send_keys(file_path)