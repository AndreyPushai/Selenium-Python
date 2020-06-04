from selenium import webdriver

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))




try:
    # Открыть страницу http://suninjuly.github.io/redirect_accept.html
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_id("button")

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()