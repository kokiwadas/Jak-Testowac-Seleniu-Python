import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

from helpers import operational_helpers as oh
import time

from helpers.ScreenshotListener import ScreenshotListener


class LostHatSmokeTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.login_url = self.base_url + 'login'
        self.clothes_product_url = self.base_url + '3-clothes'
        self.accessories_product_url = self.base_url + '6-accessories'
        self.art_product_url = self.base_url + '9-art'
        driver = webdriver.Chrome(executable_path=r"C:\Personal_Belongings\Python\Chromedriver\chromedriver.exe")
        self.ef_driver = EventFiringWebDriver(driver, ScreenshotListener())

    @classmethod
    def tearDownClass(self):
        self.ef_driver.quit()

    def test_base_page_title(self):
        expected_title = 'Lost Hat'
        self.assert_title(self.base_url, expected_title)

    def test_product_clothes_page_title(self):
        expected_title = 'Clothes'
        self.assert_title(self.clothes_product_url, expected_title)

    def test_product_accessories_page_title(self):
        expected_title = 'Accessories'
        self.assert_title(self.accessories_product_url, expected_title)

    def test_product_art_page_title(self):
        expected_title = 'Art'
        self.assert_title(self.art_product_url, expected_title)

    def test_login_page_title(self):
        expected_title = 'Login'
        self.assert_title(self.login_url, expected_title)

    def get_page_title(self, url):
        self.ef_driver.get(url)
        return self.ef_driver.title

    def assert_title(self, url, expected_title):
        actual_title = self.get_page_title(url)
        self.assertEqual(expected_title, actual_title,
                         f'Expected {expected_title} differ from actual title {actual_title} on page: {url}')

    def test_search_bar_existance(self):
        driver = self.ef_driver
        driver.get(self.base_url)
        search_bar_xpath = '//*[@id="search_widget"]/form'
        element_existance = oh.check_exists_by_xpath(driver, search_bar_xpath)
        self.assertEqual(True, element_existance, f'Element with xpath: {search_bar_xpath} does not exist on the page with url: {driver.current_url}')

    def test_search_bar_phrase_input(self):
        driver = self.ef_driver
        driver.get(self.base_url)
        minimum_expected_elements = 5
        search_bar_xpath = '//*[@name="s"]'
        product_list_xpath = '//*[@class="product-miniature js-product-miniature"]'
        search_bar_element = driver.find_element_by_xpath(search_bar_xpath)
        search_bar_element.send_keys('mug')
        search_bar_element.send_keys(Keys.ENTER)
        product_list_element = driver.find_elements_by_xpath(product_list_xpath)
        self.assertLessEqual(minimum_expected_elements, len(product_list_element), f"Expected number {minimum_expected_elements} isn't less or equal than actual number of elements found: {len(product_list_element)}")
