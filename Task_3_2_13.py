import unittest
from selenium import webdriver
import time

answer = 'Congratulations! You have successfully registered!'


class TestTsk(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector(
            '[placeholder="Input your ' \
            'first name"]')
        input1.send_keys("Alex")
        input2 = browser.find_element_by_css_selector(
            '[placeholder="Input your ' \
            'last name"]')

        input2.send_keys("Lis")
        input3 = browser.find_element_by_css_selector(
            '[placeholder="Input your ' \
            'email"]')
        input3.send_keys("lis@mail.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")

        # записываем в переменную welcome_text текст из  элемента
        # welcome_text_elt
        welcome_text = welcome_text_elt.text

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(2)

        # закрываем браузер после всех манипуляций
        browser.quit()

        self.assertEqual(welcome_text, answer, "Should be successfully "
                                            "registered")

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector(
            '[placeholder="Input your first name"]')
        input1.send_keys("Alex")
        input2 = browser.find_element_by_css_selector(
            '[placeholder="Input your last name"]')

        input2.send_keys("Lis")
        input3 = browser.find_element_by_css_selector(
            '[placeholder="Input your email"]')
        input3.send_keys("lis@mail.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")

        # записываем в переменную welcome_text текст из  элемента
        # welcome_text_elt
        welcome_text = welcome_text_elt.text

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(2)

        # закрываем браузер после всех манипуляций
        browser.quit()
        self.assertEqual(welcome_text, answer, "Should be successfully "
                                               "registered")


if __name__ == "__main__":
    unittest.main()

