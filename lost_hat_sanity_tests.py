import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from helpers import operational_helpers as oh

class LostHatSanityTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.login_url = self.base_url + 'login'
        self.clothes_product_url = self.base_url + '3-clothes'
        self.accessories_product_url = self.base_url + '6-accessories'
        self.art_product_url = self.base_url + '9-art'
        self.driver = webdriver.Chrome(executable_path=r"C:\Python\Test\chromedriver.exe")

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

