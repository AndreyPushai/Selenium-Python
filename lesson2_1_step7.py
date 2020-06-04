from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открыть страницу http://suninjuly.github.io/get_attribute.html.
    
    browser = webdriver.Chrome()
    browser.get(link)

    # Найти на ней элемент-картинку, который является изображением сундука с сокровищами.

    image = browser.find_element_by_css_selector("img")

    # Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.

    valuex = image.get_attribute("valuex")
    print(valuex)

    # Посчитать математическую функцию от x (сама функция остаётся неизменной). - функция выше.

    # Ввести ответ в текстовое поле
    text_input = browser.find_element_by_id("answer")
    text_input.send_keys(calc(valuex))

    # Отметить checkbox "I'm the robot".
    checkbox = browser.find_element_by_css_selector("input#robotCheckbox")
    checkbox.click()

    # Выбрать radiobutton "Robots rule!".
    radiobutton = browser.find_element_by_css_selector("input#robotsRule")
    radiobutton.click()

    # Нажать на кнопку Submit.  
    button = browser.find_element_by_css_selector("button.btn")
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