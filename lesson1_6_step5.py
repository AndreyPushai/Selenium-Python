from selenium import webdriver
import time 
import math

mainlink = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_link_text")

    formula = str(math.ceil(math.pow(math.pi, math.e)*10000))
    link = browser.find_element_by_link_text(formula)
    link.click()
    
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivanus")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrgov")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Shmolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Prussia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(16)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла