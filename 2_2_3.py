# Напишите здесь свой код :-)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_el = browser.find_element(By.CSS_SELECTOR, "#num1").text
    y_el = browser.find_element(By.CSS_SELECTOR, "#num2").text
    print(x_el, y_el)
    res = int(x_el) + int(y_el)
    print(res)
    select = Select(browser.find_element(By.TAG_NAME, "select")).select_by_value(str(res))
    btn = browser.find_element(By.CSS_SELECTOR, "button").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
