from appium.webdriver.webdriver import WebDriver


class BasePage:
    _driver: WebDriver

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, by, locator=''):
        if isinstance(by, tuple):
            return self._driver.find_element(*by)
        else:
            return self._driver.find_element(by, locator)

    def find_elements(self,by, locator=''):
        if isinstance(by, tuple):
            return self._driver.find_elements(*by)
        else:
            return self._driver.find_elements(by, locator)