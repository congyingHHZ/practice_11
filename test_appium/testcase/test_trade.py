from time import sleep

from test_appium.page.app import App


class TestTrade:
    def setup(self):
        self.main = App().start().main()

    def test_trade_add_stock(self):
        # todo:数据驱动未做
        self.main.goto_stocks().goto_search().search('jingdong').add_stock()

        assert '京东' in self.main.goto_stocks().optional_share()

    def test_xx(self):
        self.main.goto_stocks().goto_search().search('jingdong').add_stock()

        assert "已添加" in self.main.goto_stocks().goto_search().search('jingdong').get_stock_state("JD")


