from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math

link = " http://www.google.com"
alert_script = "Robots at work"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Send alert via execute_script

    browser.execute_script("alert('" + alert_script + "');")

    # Get alert message

    alert = browser.switch_to.alert
    text = alert.text
    time.sleep(1)

    # с помощью assert проверяем, что ожидаемый текст совпадает с введенным текстом

    assert text == alert_script, "Alert text mismatches with entered data"

    # Close alert message

    alert.accept()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла