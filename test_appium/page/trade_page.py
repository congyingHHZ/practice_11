from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.base_page import BasePage
from test_appium.page.search_page import Search


class Trade(BasePage):
    def goto_search(self):
        self.find(MobileBy.ID, 'action_search').click()
        return Search(self._driver)

    def optional_share(self):
        self.find(MobileBy.XPATH, '//*[contains(@resource-id, "title_text") and @text="自选股"]').click()
        # sleep(5)
        # for i in range(5):
        #     print(self._driver.contexts)
        #     sleep(0.5)
        # print(self._driver.page_source)
        #
        # print(self._driver.page_source)
        # # print(self._driver.window_handles)

        self.find(MobileBy.XPATH, '//*[@text="自选股"]').click()
        stocks = self.find_elements(MobileBy.ID, 'portfolio_stockName')
        stocks_name = []
        for i in stocks:
            stocks_name.append(i.text)

        return stocks_name
