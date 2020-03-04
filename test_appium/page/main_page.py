from appium.webdriver.common.mobileby import MobileBy
from test_appium.page.base_page import BasePage
from test_appium.page.search_page import Search
from test_appium.page.trade_page import Trade


class Main(BasePage):

    def goto_search(self):
        search_locator = (MobileBy.ID, 'home_search')
        self.find(search_locator).click()
        return Search(self._driver)

    def goto_stocks(self):
        reade_locator = (MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/tab_name" and @text="行情"]')
        self.find(reade_locator).click()
        return Trade(self._driver)
