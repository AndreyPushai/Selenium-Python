from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math

link = " http://suninjuly.github.io/selects1.html"


try:
    # Открыть страницу  http://suninjuly.github.io/selects1.html
    browser = webdriver.Chrome()
    browser.get(link)

    # Посчитать сумму заданных чисел

    # Считать значение для переменной x. - находим элемент, содержащий текст
    x_element = browser.find_element_by_id("num1")
    y_element = browser.find_element_by_id("num2")

    # записываем в переменные текст и суммируем
    x = x_element.text
    y = y_element.text
    sum = int(x) + int(y)
    #print(sum)

    # Выбрать в выпадающем списке значение равное расчитанной сумме

    select = Select(browser.find_element_by_css_selector("select#dropdown"))
    select.select_by_visible_text(str(sum)) 

    # Нажать кнопку "Submit"

    # Нажать на кнопку Submit.  
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    #time.sleep(1)

    
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    #assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла