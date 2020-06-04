from selenium import webdriver
import time 
import os

link = "http://suninjuly.github.io/file_input.html"
    
print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))

try:
    # Открыть страницу http://suninjuly.github.io/file_input.html

    browser = webdriver.Chrome()
    browser.get(link)
    
    # Заполнить текстовые поля: имя, фамилия, email

    name = browser.find_element_by_css_selector("[name=firstname]").send_keys("Test Name")
    lastname = browser.find_element_by_css_selector("[name=lastname]").send_keys("Test Lastname")
    email = browser.find_element_by_css_selector("[name=email]").send_keys("test@test.co")

    # Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'test.txt')

    input_file = browser.find_element_by_css_selector("#file").send_keys(str(file_path))

    # Нажать кнопку "Submit"

    submit = browser.find_element_by_css_selector(".btn-primary").click()

    text = browser.switch_to.alert.text
    print(text)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()