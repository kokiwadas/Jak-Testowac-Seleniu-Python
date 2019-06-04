import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def wait_for_elements(driver, xpath, max_seconds_to_wait=5, number_of_expected_elements=1):
    """Checking every second if list of elements under specified xpath was found.

    :param driver: webdriver instance
    :param xpath: xpath of the element
    :param max_seconds_to_wait: max amount of second to wait (default = 5)
    :param number_of_expected_elements: minimum number of elements to be found (default = 1)
    :return: list of found items
    """

    for seconds in range(1, max_seconds_to_wait + 1):
        elements = driver.find_elements_by_xpath(xpath)
        number_of_found_elements = len(elements)
        print(f'Total waiting time {seconds}s')
        print(f'Found {number_of_found_elements}')
        if elements:
            return elements
        if seconds == max_seconds_to_wait:
            print('End of wait')
            assert len(elements) >= number_of_expected_elements, f'Expected {number_of_expected_elements} elements but found {len(elements)} for xpath {xpath} in time of {max_seconds_to_wait}s'
        time.sleep(1)


def visibility_of_element_wait(driver, xpath, seconds_to_wait=10):
    """Waiting provided number of seconds until web element is visible

    :param driver: webdriver instance
    :param xpath: xpath of web element
    :param seconds_to_wait: number of seconds to wait (default = 10)
    :return: WebDriverWait instance
    """
    timeout_message = f"Element for xpath: '{xpath}' and url: {driver.current_url} not found in {seconds_to_wait} seconds"

    locator = (By.XPATH, xpath)
    element_located = EC.visibility_of_element_located(locator)
    wait = WebDriverWait(driver.wrapped_driver, seconds_to_wait)
    return wait.until(element_located, timeout_message)


def check_exists_by_xpath(driver, xpath):
    """Checks if element with provided xpath exists

    :param driver: webdriver instance
    :param xpath: xpath of the element
    :return: returns True if element exists or False if it does not
    """
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True
