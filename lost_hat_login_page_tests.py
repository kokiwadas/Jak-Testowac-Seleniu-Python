from helpers import functional_helpers as fh
from helpers.base_class_tests import BaseTestClass
from helpers.wrappers import screenshot_decorator


class LostHatLoginPageTests(BaseTestClass):

    @screenshot_decorator
    def test_login_text_header(self):
        expected_text = 'Log in to your account'
        header_xpath = '//header[@class="page-header"]'
        driver = self.ef_driver
        driver.get(self.login_url)
        self.assert_element_text(driver, header_xpath, expected_text)

    @screenshot_decorator
    def test_correct_login(self):
        # expected_text is a user name and user surname used during registration
        expected_text = 'TestDude TestMate'
        user_name_xpath = '//a[@class="account"]/*[@class="hidden-sm-down"]'
        user_email = 'testing@test.com'
        user_pass = 'Password1'
        driver = self.ef_driver
        driver.get(self.login_url)
        fh.user_login(driver, user_email, user_pass)
        self.assert_element_text(driver, user_name_xpath, expected_text)

    @screenshot_decorator
    def test_incorrect_login(self):
        # expected_text is a warning message about authentication failed
        expected_text = 'Authentication failed.'
        alert_xpath = '//*[@class="alert alert-danger"]'
        user_email = 'invalid@test.test'
        user_pass = 'abc123'
        driver = self.ef_driver
        driver.get(self.login_url)
        fh.user_login(driver, user_email, user_pass)
        self.assert_element_text(driver, alert_xpath, expected_text)

    def assert_element_text(self, driver, xpath, expected_text):
        """Comparing expected text with observed value from web element
         :param driver: webdriver instance
         :param xpath: xpath to element with text to be observed
         :param expected_text: text what we expecting to be found
         :return: None
        """
        element = driver.find_element_by_xpath(xpath)
        element_text = element.text
        self.assertEqual(expected_text, element_text, f'Expected text differ from actual on page: {driver.current_url}')
