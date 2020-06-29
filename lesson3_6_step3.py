import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.
chrome_driver_path = "C:/chromedriver"

array = []

def add_new_value_to_array(array, attempt_message):
    return array.append(attempt_message)

# Фикстуры, которые будут открывать и закрывать браузер для каждого теста
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()



@pytest.mark.parametrize('link', [
                                    "https://stepik.org/lesson/236895/step/1",
                                    "https://stepik.org/lesson/236896/step/1",
                                    "https://stepik.org/lesson/236897/step/1",
                                    "https://stepik.org/lesson/236898/step/1",
                                    "https://stepik.org/lesson/236899/step/1",
                                    "https://stepik.org/lesson/236903/step/1",
                                    "https://stepik.org/lesson/236904/step/1",
                                    "https://stepik.org/lesson/236905/step/1"
                                    ])
def test_user_answer_is_correct(browser, link):
    # открыть страницу 
    URL= f"{link}"
    browser.get(URL)
    # Нужно вставить implicit waiter
    browser.implicitly_wait(5)
    
    
    # Ответ, который мы должны вставлять в каждый из шагов.
    answer = math.log(int(time.time() + 0.7))

    # ввести правильный ответ
    browser.find_element_by_tag_name("textarea").send_keys(str(answer))

    # нажать кнопку "Отправить" 
    browser.find_element_by_css_selector(".submit-submission").click()

    # дождаться фидбека о том, что ответ правильный

    

    # проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"

    attempt_message = browser.find_element_by_css_selector(".smart-hints__hint").text

    assert attempt_message == "Correct!", "Message text mismatches with actual result, " + attempt_message

    # создадим массив из неправильных ответов и форматируем его в строку
    if attempt_message != "Correct!":
        add_new_value_to_array(array, attempt_message)
        print(array)

print(' '.join(array))