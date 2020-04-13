from pprint import pprint

import requests

proxies = {"http": "http://127.0.0.1:8888",
           "https": "https://127.0.0.1:8888"}


def test_requests():
    r = requests.get("https://home.testing-studio.com/t/topic/1450.json")
    pprint(r)

    print(r.status_code)
    print(r.json())
    assert r.status_code == 200


def test_get():
    r = requests.get("https://httpbin.testing-studio.com/get",
                     params={"a": 2,
                             "b": 3,
                             "c": 'sdaqw'},
                     proxies=proxies["http"],
                     verify=False  # 关闭证书验证
                     )
    print(r.json())
    assert r.status_code == 200


def test_post():
    r = requests.post("https://httpbin.testing-studio.com/post",
                      params={"d": 32342},
                      data={"a": 2,
                            "b": 3,
                            "c": 'sdaqw'})
    print(r.json())
    assert r.status_code == 200


def test_upload():
    r = requests.post("https://httpbin.testing-studio.com/post",
                      files={"file": open("__init__.py", "rb")},
                      headers={"Content-Type": "aa",
                               "User-Agent": "cy",
                               "hh": "new"},
                      cookies={"name": "seveniruby"})
    print(r.json())
    print(r.text)
    print(r.raw.read(10))  # 解析数据的前10个字节
    print(r.request)  # 请求的内容
    assert r.status_code == 200
    assert r.json()["headers"]["User-Agent"] == "cy"
    assert r.json()["headers"]["Hh"] == "new"  # 头信息 大写
