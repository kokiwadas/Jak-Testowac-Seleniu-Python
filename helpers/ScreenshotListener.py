from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
import time


class ScreenshotListener(AbstractEventListener):

    def on_exception(self, exception, driver):
        screenshot_path = rf'testScreenshots\driver_exception_{time.time()}.png'
        driver.get_screenshot_as_file(screenshot_path)
        print(f'Screenshot saved as {screenshot_path}')
