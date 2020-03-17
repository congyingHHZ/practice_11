import pytest

from test_appium.page.app import App


class TestProfile:
    def setup(self):
        self.profile = App().main().goto_profile()

    @pytest.mark.parametrize("account,password,result", [('12334', '122332', '错误')])
    def test_login(self, account, password, result):
        assert result in self.profile.login_password(account, password)
