from helpers.screenshot_listener import ScreenshotListener
from helpers.screenshot_listener import make_screenshot


def screenshot_decorator(test_func):

    def wrapper(self):
        try:
            return test_func(self)
        except AssertionError as ex:
            make_screenshot(self.ef_driver, 'assertion')
            print('Error!')
            raise ex

    return wrapper

