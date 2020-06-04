from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import math

browser = webdriver.Chrome()

# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

link = "http://suninjuly.github.io/math.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открыть страницу http://suninjuly.github.io/explicit_wait2.html
    browser.get(link)

    people_radio = browser.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"


finally:
    browser.quit()