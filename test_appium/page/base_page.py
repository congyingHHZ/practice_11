import logging
import yaml
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

error_max = 3
error_count = 0
_black_list = [
    (By.ID, 'tv_agree'),
    (By.XPATH, '//*[@text="确定"]'),
    (By.ID, 'image_cancel'),
    (By.XPATH, '//*[@text="下次再说"]')]


# def popups_handling(func):
#     def wrapper(*args,**kwargs):
#         global error_count
#         try:
#             return func(*args, **kwargs)
#         except Exception as e:
#             error_count += 1
#             if error_count == error_max:
#                 raise e
#             for black_locator in _black_list:
#                 black_elements = _driver.find_elements(*black_locator)
#                 if not black_elements == []:
#                     black_elements[0].click()
#                     return wrapper(*args,**kwargs)
#             logging.warn('black list not found!')
#             raise e

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
        self.error_count = 0

    def find(self, by, locator=None):

        try:
            find_element = self._driver.find_element(*by) if isinstance(by, tuple) else self._driver.find_element(by,
                                                                                                                  locator)
            self.error_count = 0
            return find_element
        except Exception as e:
            self.error_count += 1
            if self.error_count == self.error_max:
                raise e
            for black_locator in self._black_list:
                black_elements = self._driver.find_elements(*black_locator)
                if not black_elements == []:
                    black_elements[0].click()
                    return self.find(by, locator)
            logging.warn('black list not found!')
            raise e

    def find_elements(self, by, locator=''):
        if isinstance(by, tuple):
            return self._driver.find_elements(*by)
        else:
            return self._driver.find_elements(by, locator)

    def get_toast(self):
        return self.find(By.XPATH, "//*[@class='android.widget.Toast']").test

    def text_locator(self, key):
        return By.XPATH, f"//*[text='{key}']"

    def find_by_text(self, key):
        return self.find(self.text_locator(key))

    def id_locator(self, key):
        return MobileBy.ID, f"{key}"

    def find_by_id(self, key):
        self.find(self.id_locator(key))

    def find_and_get_text(self):
        pass

    def steps(self, path):
        with open(path, 'r+') as f:
            steps: list[dict] = yaml.safe_load(f)
            element: WebElement = None
            for step in steps:
                logging.info(step)
                if "by" in step.keys():
                    element = self.find(step["by"], step["locator"])
                if "action" in step.keys():
                    action = step["action"]
                    if action == "click":
                        element.click()
                    elif action in ["send", "input"]:
                        element.send_keys(step["value"])

