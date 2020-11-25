import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

answer = math.log(int(time.time()))


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('n', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_parametrize(browser, n):
    link = f"https://stepik.org/lesson/{n}/step/1"
    browser.get(link)
    field = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "textarea.textarea.string-quiz__textarea.ember-text-area.ember-view")
        )
    )
    field.send_keys(str(answer))
    browser.find_element_by_css_selector(
        "button.submit-submission"
    ).click()
    # message_result = WebDriverWait(browser, 5).until(
    #     EC.visibility_of_element_located(
    #         (By.CSS_SELECTOR, "pre.smart-hints__hint")
    #     )
    # )
    # result = message_result.text
    result = browser.find_element_by_css_selector("pre.smart-hints__hint").text
    expected = "Correct"
    assert expected in str(result)


