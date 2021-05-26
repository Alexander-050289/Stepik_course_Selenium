from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1")
    x1 = num1.text
    num2 = browser.find_element_by_id("num2")
    x2 = num2.text
    summa = int(x1) + int(x2)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(summa))

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
