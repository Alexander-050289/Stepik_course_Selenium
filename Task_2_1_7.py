from selenium import webdriver
import time
import math

link = " http://suninjuly.github.io/get_attribute.html"


def calc(value):
    return str(math.log(abs(12*math.sin(int(value)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    sunduk = browser.find_element_by_id("treasure")
    sunduk_checked = sunduk.get_attribute("valuex")

    x = sunduk_checked
    y = calc(x)

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)

    option1 = browser.find_element_by_id('robotCheckbox')
    option1.click()

    option2 = browser.find_element_by_id('robotsRule')
    option2.click()

    button = browser.find_element_by_css_selector('button.btn')
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()