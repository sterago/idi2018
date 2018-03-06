import pytest
from flask import url_for


@pytest.mark.usefixtures('live_server')
@pytest.mark.element
def test_homepage(needle):

    # Navigate to web page

    url = url_for('frontend.index', _external=True)
    needle.driver.get(url)

    # Take an element screen diff
    needle.assert_screenshot('body', element_or_selector='body')
