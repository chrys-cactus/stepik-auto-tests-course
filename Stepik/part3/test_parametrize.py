import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

answer = math.log(int(time.time()))


@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('n', ["236898", "236899", "236905"])
class TestU():
    def test_parametrize(self, browser, n):
        link = f"https://stepik.org/lesson/{n}/step/1"
        browser.get(link)
        field = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "textarea.textarea.string-quiz__textarea.ember-text-area.ember-view")
            )
        )
        field.send_keys(str(answer))
        browser.find_element_by_css_selector(
            "button.submit-submission"
        ).click()
        message_result = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "pre.smart-hints__hint")
            )
        )
        result = message_result.text
        expected = "Correct"
        assert expected in str(result)


