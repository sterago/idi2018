from needle.cases import NeedleTestCase
from needle.driver import NeedleRemote
from selenium.webdriver import DesiredCapabilities


class HomepageTests(NeedleTestCase):
    @classmethod
    def get_web_driver(cls):
        return NeedleRemote(desired_capabilities=DesiredCapabilities.CHROME)

    def test_homepage(self):
        self.driver.get('http://www.bbc.co.uk/news/')
        self.assertScreenshot('#blq-mast', 'bbc-masthead')
