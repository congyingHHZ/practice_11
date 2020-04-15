from test_wework.api.wework import WeWork


class TestWework:
    token = ""
    secret =""
    @classmethod
    def setup_class(cls):

        cls.token = WeWork.get_token(cls.secret)
    def test_get_token(self):
        r = WeWork.get_access_token(self.secret)
    def test_get_token_exist(self):
        assert self.token is not None
