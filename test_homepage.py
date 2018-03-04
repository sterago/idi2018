from time import sleep

import pytest
from selenium.webdriver.common.by import By
from flask import url_for


@pytest.mark.usefixtures('live_server')
@pytest.mark.element
def test_example_element(needle):
    """Example for comparing individual elements

    :param NeedleDriver needle: NeedleDriver instance
    :return:
    """

    # Navigate to web page

    url = url_for('index', _external=True)
    needle.driver.get(url)

    sleep(1000)

    # Take an element screen diff
    needle.assert_screenshot('search_field', (By.ID, 'tsf'))
