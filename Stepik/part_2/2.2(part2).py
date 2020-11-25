import time
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://SunInJuly.github.io/execute_script.html")
    x = browser.find_element_by_id("input_value").text
    result = calc(x)
    browser.find_element_by_id("answer").send_keys(result)
    browser.find_element_by_id("robotCheckbox").click()

    button = browser.find_element_by_css_selector("button.btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    browser.find_element_by_id("robotsRule").click()
    browser.find_element_by_css_selector("button.btn.btn-primary").click()

finally:
    time.sleep(30)
    browser.quit()
