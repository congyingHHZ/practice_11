import pytest

from test_appium.page.app import App


class TestSearch:
    def setup(self):
        self.main = App().start().main()

    @pytest.mark.parametrize("key,stock_type,price", [
        ("ALIBABA", "BABA", 200)])
    def test_search(self, key, stock_type, price):
        # 搜索，并判断股价是否大于给定价格值
        assert self.main.goto_search().search(key).get_price(stock_type) > price
