import unittest
from selenium import webdriver
import time
from helpers import functional_helpers as fh


class MainTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Python\Test\chromedriver.exe')
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.login_url = self.base_url + 'login'
        self.sample_product_url = self.base_url + 'men/1-1-hummingbird-printed-t-shirt.html'

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def assert_element_text(self, driver, xpath, expected_text):
        """Comparing expected text with observed value from web element

        :param driver:  webdriver element
        :param xpath:   xpath to the element with text to be observed
        :param expected_text:   text which we expect to find
        return: None
        """
        element = driver.find_element_by_xpath(xpath)
        element_text = element.text
        self.assertEqual(expected_text, element_text,
                         f'Actual header text differs from actual on the page: {driver.current_url}')

    def test_login_form_header(self):
        driver = self.driver
        driver.get(self.login_url)
        self.assert_element_text(driver, '//*[@class="page-header"]/h1', 'Log in to your account')

    def test_successful_login(self):
        driver = self.driver
        driver.get(self.login_url)
        user_email = 'test@test.com'
        user_password = 'Password1'
        fh.user_login(driver, user_email, user_password)
        time.sleep(3)
        self.assert_element_text(driver, '//*[@class="account"]/*[@class="hidden-sm-down"]', "TestDude TestMate")

    def test_product_name_validation(self):
        driver = self.driver
        driver.get(self.sample_product_url)
        self.assert_element_text(driver, '//*[@class="col-md-6"]/*[@itemprop="name"]', 'HUMMINGBIRD PRINTED T-SHIRT')

    def test_product_price_validation(self):
        driver = self.driver
        driver.get(self.sample_product_url)
        self.assert_element_text(driver, '//*[@class="current-price"]/span', 'PLN23.52')

    def test_failed_login_attempt(self):
        driver = self.driver
        driver.get(self.login_url)
        user_email = 'test2@test.com'
        user_password = 'Password2'
        fh.user_login(driver, user_email, user_password)
        time.sleep(3)
        self.assert_element_text(driver, '//*[@class="alert alert-danger"]', "Authentication failed.")