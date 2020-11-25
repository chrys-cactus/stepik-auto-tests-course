import time
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    browser.find_element_by_css_selector("button.btn.btn-primary").click()
    alert = browser.switch_to_alert()
    alert.accept()
    x = browser.find_element_by_id("input_value").text
    result = calc(x)
    browser.find_element_by_id("answer").send_keys(result)
    browser.find_element_by_css_selector("button.btn.btn-primary").click()
finally:
    time.sleep(30)
    browser.quit()
