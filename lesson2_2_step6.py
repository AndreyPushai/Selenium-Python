from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math

link = "http://SunInJuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    # Открыть страницу http://SunInJuly.github.io/execute_script.html.
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Считать значение для переменной x.

    x = browser.find_element_by_css_selector("#input_value").text
    time.sleep(1)

    # Посчитать математическую функцию от x.

    # Проскроллить страницу вниз.

    

    # Ввести ответ в текстовое поле.

    answer_input = browser.find_element_by_css_selector("input#answer").send_keys(calc(x))
    

    # Выбрать checkbox "I'm the robot".

    checkbox = browser.find_element_by_css_selector("#robotCheckbox").click()

    # Переключить radiobutton "Robots rule!".

    radiobutton = browser.find_element_by_css_selector("#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()

    # Нажать на кнопку "Submit".

    submit = browser.find_element_by_css_selector(".btn-primary").click()

    text = browser.switch_to.alert.text
    print(text)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла