import time
from selenium import webdriver
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    browser.find_element_by_css_selector("button.trollface.btn.btn-primary").click()
    new_window = browser.window_handles[1] # получаем имя второй вкладки
    browser.switch_to.window(new_window) # переключаемся на вторую вкладку
    x = browser.find_element_by_id("input_value").text
    result = calc(x)
    print(result)
    browser.find_element_by_id("answer").send_keys(result)
    browser.find_element_by_css_selector("button.btn.btn-primary").click()
finally:
    time.sleep(30)
    browser.quit()
