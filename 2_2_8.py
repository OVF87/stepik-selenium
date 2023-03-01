# Напишите здесь свой код :-)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    element = browser.find_element(By.NAME, "firstname").send_keys("М")
    element = browser.find_element(By.NAME, "lastname").send_keys("o")
    element = browser.find_element(By.NAME, "email").send_keys("@М")

    element = browser.find_element(By.CSS_SELECTOR, "#file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, '1.txt')           # добавляем к этому пути имя файла
    element.send_keys(file_path)

    btn = browser.find_element(By.CSS_SELECTOR, "button").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
