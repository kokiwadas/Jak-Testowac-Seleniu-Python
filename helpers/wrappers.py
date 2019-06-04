from helpers.screenshot_listener import ScreenshotListener
from helpers.screenshot_listener import make_screenshot
from selenium.common.exceptions import TimeoutException


def screenshot_decorator(test_func):

    def wrapper(self):
        try:
            return test_func(self)
        except AssertionError as ex:
            make_screenshot(self.ef_driver, 'assertion')
            raise ex
        except TimeoutException as ex:
            make_screenshot(self.ef_driver, 'timeout')
            raise ex

    return wrapper

