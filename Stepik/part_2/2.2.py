import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    x = int(browser.find_element_by_id("num1").text)
    y = int(browser.find_element_by_id("num2").text)
    result = x+y
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(result))  # ищем элемент с текстом "Python"
    browser.find_element_by_css_selector("button.btn.btn-default").click()
finally:
    time.sleep(30)
    browser.quit()
