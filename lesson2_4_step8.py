from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import math

browser = webdriver.Chrome()

# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открыть страницу http://suninjuly.github.io/explicit_wait2.html
    browser.get(link)

    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)

    price = WebDriverWait(browser, 12).until(
        expected_conditions.text_to_be_present_in_element((By.ID, "price"), "100")
        )
    
    # Нажать на кнопку "Book"
    book_button = browser.find_element_by_css_selector("#book").click()

    # Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
    x = browser.find_element_by_id("input_value").text

    text_input = browser.find_element_by_id("answer").send_keys(calc(x))
    submit = browser.find_element_by_css_selector("#solve").click()

    alert = browser.switch_to.alert

    print(alert.text)

finally:
    browser.quit()