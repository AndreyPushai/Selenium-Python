from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/math.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение для переменной x. - находим элемент, содержащий текст
    x_element = browser.find_element_by_id("input_value")
    # записываем в переменную x текст из элемента x_element
    x = x_element.text

    # Ввести ответ в текстовое поле
    text_input = browser.find_element_by_id("answer")
    text_input.send_keys(calc(x))

    # Отметить checkbox "I'm the robot".
    checkbox = browser.find_element_by_css_selector("input#robotCheckbox")
    checkbox.click()

    # Выбрать radiobutton "Robots rule!".
    radiobutton = browser.find_element_by_css_selector("input#robotsRule")
    radiobutton.click()

    # Нажать на кнопку Submit.
    button = browser.find_element_by_css_selector("#solve")
    button.click()
    #time.sleep(1)

    
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    #assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла