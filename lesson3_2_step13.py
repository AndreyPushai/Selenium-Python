import unittest
from selenium import webdriver

class TestLesson1_6_11(unittest.TestCase):
    def test_registration_page_1(self):
        
        # starting cromium
        link = "http://suninjuly.github.io/registration1.html"

        browser = webdriver.Chrome()
        browser.get(link)

        # Finding and filling required inputs

        input1 = browser.find_element_by_class_name("form-control.first")
        input1.send_keys("Ivanus")

        input2 = browser.find_element_by_class_name("form-control.second")
        input2.send_keys("Petrgov")

        input3 = browser.find_element_by_class_name("form-control.third")
        input3.send_keys("Email")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Registration text mismatch: \"{welcome_text}\" displayed instead of \"Congratulations! You have successfully registered!\"")
        # quit chromium
        browser.quit()
        
    def test_registration_page_2(self):

        # starting cromium
        link = "http://suninjuly.github.io/registration2.html"

        browser = webdriver.Chrome()
        browser.get(link)

        # Finding and filling required inputs

        input1 = browser.find_element_by_css_selector("input.form-control.first[required]")
        input1.send_keys("Ivanus")

        input2 = browser.find_element_by_css_selector("input.form-control.second[required]")
        input2.send_keys("Petrgov")

        input3 = browser.find_element_by_css_selector("input.form-control.third[required]")
        input3.send_keys("Email")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Registration text mismatch: \"{welcome_text}\" displayed instead of \"Congratulations! You have successfully registered!\"")
        # quit chromium
        browser.quit()
        
if __name__ == "__main__":
    unittest.main()