import pytest
from flask import url_for


@pytest.mark.usefixtures('live_server')
@pytest.mark.element
def test_homepage(needle):
    """Example for comparing individual elements

    :param NeedleDriver needle: NeedleDriver instance
    :return:
    """

    # Navigate to web page

    url = url_for('frontend.index', _external=True)
    needle.driver.get(url)

    import ipdb; ipdb.set_trace()

    # Take an element screen diff
    needle.assert_screenshot('body', element_or_selector='body')
