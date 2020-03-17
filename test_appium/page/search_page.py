import string

from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.base_page import BasePage


class Search(BasePage):
    # def __int__():
    #     pass
    # self._driver = driver
    # 子类不重写__init__，实例化时会自动调用父类的__init__
    # 实例化Search传入_driver，BasePage中定义的那个self._driver值就会被改写

    _name_locator = (MobileBy.ID, "name")  # 常用定位符，类变量，便于多个方法调用，可根据不同版本、平台进行改造
    def search(self, key: string):
        self.find(MobileBy.ID, 'search_input_text').send_keys(key)
        self.find(MobileBy.ID, 'search_input_text').click()
        self.find(self._name_locator).click()
        # self.find(MobileBy.XPATH, '//*[@text="搜索"]').click()
        # //*[@content-desc="搜索"]
        return self

    def get_price(self, key: string) -> float:
        self.find(MobileBy.XPATH, '//*[@text="股票"]').click()
        reslut = self._driver.find_element_by_xpath(
            f'//*[@text="{key}"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]').text

        return float(reslut)

    def add_stock(self):
        # 加自选
        self.find(MobileBy.ID, 'add_attention').click()
        self.find(MobileBy.ID, 'action_close').click()
        return self

    def get_stock_state(self, key: string):
        # stock_state_locator = (MobileBy.XPATH,
        #                        f'//*[@text="{key}"]/../../..//*[contains(@resource-id, "add_attention")]/*')
        #
        # result = self.find(stock_state_locator).get_attribute('resource-id')
        # if 'followed_btn' in result:
        #     return '已添加'
        # else:
        #     return '加自选'

        # 根据大佬的思路做了更改
        stock_state_locator = (MobileBy.XPATH,
                               f'//*[@text="{key}"]/../../..//*[contains(@resource-id, "add_attention")]//*'
                               f'[contains(@resource-id, "followed")]')

        result = self.find(stock_state_locator).get_attribute('text')

        return result
