import unittest

from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

from helpers.screenshot_listener import ScreenshotListener


class BaseTestClass(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.login_url = self.base_url + 'login'
        self.product_url = self.base_url + 'art/12-mountain-fox-vector-graphics.html'
        self.sample_product_url = self.base_url + 'men/1-1-hummingbird-printed-t-shirt.html'
        self.clothes_product_url = self.base_url + '3-clothes'
        self.accessories_product_url = self.base_url + '6-accessories'
        self.art_product_url = self.base_url + '9-art'
        driver = webdriver.Chrome(executable_path=r"C:\Personal_Belongings\Python\Chromedriver\chromedriver.exe")
        self.ef_driver = EventFiringWebDriver(driver, ScreenshotListener())

    @classmethod
    def tearDown(self):
        self.ef_driver.quit()
