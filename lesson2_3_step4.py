from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открыть страницу http://suninjuly.github.io/alert_accept.html
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    # Нажать на кнопку

    button = browser.find_element_by_css_selector(".btn-primary").click()
    time.sleep(1)
    # Принять confirm

    confirm_popup = browser.switch_to.alert.accept()
    #confirm_popup.

    # На новой странице решить капчу для роботов, чтобы получить число с ответом

    x = browser.find_element_by_css_selector("#input_value").text

    input_field = browser.find_element_by_css_selector("#answer")
    input_field.send_keys(calc(x))
    submit = browser.find_element_by_css_selector(".btn-primary").click()
    
    # Get alert message

    alert = browser.switch_to.alert
    text = alert.text
    print(text)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла