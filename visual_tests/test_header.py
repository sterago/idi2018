import pytest
from flask import url_for


@pytest.mark.usefixtures('live_server')
@pytest.mark.element
def test_navbar(needle):

    # Navigate to web page

    url = url_for('frontend.index', _external=True)
    needle.driver.get(url)

    xpath = "//*[@class='navbar navbar-default']"
    navbar = needle.driver.find_element_by_xpath(xpath)

    # Take an element screen diff
    needle.assert_screenshot('navbar', element_or_selector=navbar)
