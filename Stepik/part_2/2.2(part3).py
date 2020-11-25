import time
from selenium import webdriver
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    browser.find_element_by_css_selector(
        'input.form-control[name="firstname"]'
    ).send_keys("text")
    browser.find_element_by_css_selector(
        'input.form-control[name="lastname"]'
    ).send_keys("text")
    browser.find_element_by_css_selector(
        'input.form-control[name="email"]'
    ).send_keys("text")
    element = browser.find_element_by_id("file")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element.send_keys(file_path)
    browser.find_element_by_css_selector("button.btn.btn-primary").click()
finally:
    time.sleep(30)
    browser.quit()

