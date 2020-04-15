import requests

from test_wework.api.base_api import BaseApi


class WeWork(BaseApi):
    token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    corpid = "ww404377c9bbb17e4f"
    token = {}

    @classmethod
    def get_token(cls, secret=None):
        # 第一次调用get_token，取到的token会存入token字典中，下一次调用的时候会先查询字典
        if secret not in cls.token:
            r = cls.get_access_token(secret)
            cls.token[secret] = r["access_token"]
            return cls.token[secret]
        return cls.token[secret]

    @classmethod
    def get_access_token(cls, secret):
        r = requests.get(cls.token_url, params={"corpid": cls.corpid, "corpsecret": secret})
        assert r.json()["errcode"] == 0
        cls.token[secret] = r.json()["access_token"]
        return r.json()
