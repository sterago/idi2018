from selenium.webdriver.common.by import By
import pytest


@pytest.mark.element
def test_example_element(needle):
    """Example for comparing individual elements

    :param NeedleDriver needle: NeedleDriver instance
    :return:
    """

    # Navigate to web page
    needle.driver.get('https://www.google.com')

    # Take an element screen diff
    needle.assert_screenshot('search_field', (By.ID, 'tsf'))
