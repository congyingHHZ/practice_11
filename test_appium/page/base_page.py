from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    _driver: WebDriver

    def __init__(self, driver: WebDriver = None):
        self._driver = driver
        self._black_list = [
            (By.ID, 'tv_agree'),
            (By.XPATH, '//*[@text="确定"]'),
            (By.ID, 'image_cancel'),
            (By.XPATH, '//*[@text="下次再说"]')]
        self.error_max = 3

    def find(self, by, locator=None):
        error_count = 0
        try:
            find_element = self._driver.find_element(*by) if isinstance(by, tuple) else self._driver.find_element(by,
                                                                                                                  locator)
            return find_element
        except Exception as e:
            error_count += 1
            if error_count == self.error_max:
                raise e
            for black_locator in self._black_list:
                black_elements = self._driver.find_elements(*black_locator)
                if not black_elements == []:
                    black_elements[0].click()
                    return self.find(by, locator=None)
            raise e

    def find_elements(self, by, locator=''):
        if isinstance(by, tuple):
            return self._driver.find_elements(*by)
        else:
            return self._driver.find_elements(by, locator)
