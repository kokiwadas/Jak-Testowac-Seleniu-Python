import unittest
from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

from helpers import operational_helpers as oh
from helpers.ScreenshotListener import ScreenshotListener


class LostHatCartPageTests(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.base_url = 'http://autodemo.testoneo.com/en/'
        self.product_url = self.base_url + 'art/12-mountain-fox-vector-graphics.html'
        driver = webdriver.Chrome(executable_path=r"C:\Personal_Belongings\Python\Chromedriver\chromedriver.exe")
        self.ef_driver = EventFiringWebDriver(driver, ScreenshotListener())

    @classmethod
    def tearDown(self):
        self.ef_driver.quit()

    def test_add_to_cart(self):
        confirmation_modal_title_xpath = '//*[@id="myModalLabel"]'
        expected_confirmation_text = 'Product successfully added to your shopping cart'
        add_to_cart_button_xpath = '//*[@class="btn btn-primary add-to-cart"]'
        driver = self.ef_driver
        driver.get(self.product_url)
        add_to_cart_button = driver.find_element_by_xpath(add_to_cart_button_xpath)
        add_to_cart_button.click()

        # Waiting for the element using custom function
        # confirmation_modal_elements = oh.wait_for_elements(driver, confirmation_modal_title_xpath,
        # max_seconds_to_wait=10, number_of_expected_elements=1)
        # confirmation_modal_element = confirmation_modal_elements[0]

        confirmation_modal_element = oh.visibility_of_element_wait(driver, confirmation_modal_title_xpath)
        self.assertEqual(expected_confirmation_text, confirmation_modal_element.text[1:],
                         f'Expected text differ from actual on page: {driver.current_url}')
