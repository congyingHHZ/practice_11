from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.page.base_page import BasePage
from test_appium.page.main_page import Main


class App(BasePage):
    _package = "com.xueqiu.android"
    _activity = ".view.WelcomeActivityAlias"

    # def __int__(self, driver: WebDriver = None):
    #     # j继承父类会生成一个self.driver
    #     # 如果以前已经启动过，会复用 self.driver
    #     super()  # 调用super 完成父类的初始化

    def start(self):
        if self._driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "emulator-5554"
            caps["appPackage"] = self._package
            caps["appActivity"] = self._activity
            # caps["noReset"] = True
            # caps["dontStopAppOnReset"] = True
            caps["unicodeKeyboard"] = True
            caps["resetKeyboard"] = True
            # caps["skipServerInstallation"] = True
            # caps["chromedriverExecutableDir"]="/Users/seveniruby/projects/chromedriver/all"
            caps["chromedriverExecutable"] = r"D:\chromedriver\43.0.2357.0\chromedriver.exe"

            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self._driver.implicitly_wait(5)
        else:
            print(self._driver)
            # restart app ???
            self._driver.start_activity(self._package, self._activity)
        return self  # 返回实例自身，链式调用，可以继续调用类下的方法

    def restart(self):
        pass

    def main(self) -> Main:
        def wait_load(x):
            source = self._driver.page_source
            main_page_flag = ["我的", "同意", "image_cancel"]
            # return True if [i for i in main_page_flag if i in source] else False
            for i in main_page_flag:
                if i in source:
                    return True
            else:
                return False

        WebDriverWait(self._driver, 10).until(wait_load)
        return Main(self._driver)

    def kill(self):
        pass
