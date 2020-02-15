import time

from selenium import webdriver
from time import sleep

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _base_url = ''

    def __init__(self, driver: webdriver = None, reuse=False):

        if driver is None:
            if reuse:
                # 是否复用
                chrome_options = webdriver.ChromeOptions()
                # chrome.exe --remote-debugging-port=9222
                chrome_options.debugger_address = '127.0.0.1:9222'
                self._driver = webdriver.Chrome(options=chrome_options)
                # self.driver = webdriver.Chrome()
            else:
                self._driver = webdriver.Chrome()

            self._driver.implicitly_wait(10)
        else:
            self._driver = driver

        if self._base_url:
            self._driver.get(self._base_url)

    def find(self, by, locator='') -> WebElement:
        if isinstance(by, tuple):
            return self._driver.find_element(*by)
        else:
            return self._driver.find_element(by, locator)

    def find_elements(self,by, locator=''):
        if isinstance(by, tuple):
            return self._driver.find_elements(*by)
        else:
            return self._driver.find_elements(by, locator)

    def wait_page_jump(self, time_out, selector, next_selector):
        """
        判断是否跳转，没有跳转重复点击
        :param time_out: 超时时间
        :param selector: 元素选择器
        :return:
        """
        # selector = (By.CSS_SELECTOR, '.js_no_member .js_add_member')
        time_deadline = time.time() + time_out
        while True:
            elements = self.find_elements(next_selector)
            if len(elements) < 1:
                self.find(*selector).click()

            elif len(elements) >= 1:
                break
            if time.time() == time_deadline:
                break

    def wait(self, time_out, method):
        WebDriverWait(self._driver, time_out).until(method)

    def close(self):
        sleep(20)
        self._driver.quit()
