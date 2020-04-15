import json

import requests

from test_wework.api.wework import WeWork


class Department(WeWork):
    secret = "hFSgf7rHTuT9qmA8VIViem9T1RY1aMsppdpYdofjX54"

    def get_list(self):
        department_list_url = "https://qyapi.weixin.qq.com/cgi-bin/department/list"
        r = requests.get(department_list_url,
                         params={"access_token": self.get_token(self.secret)})
        # todo:get_token是否可以再封装一层
        self.format(r.json())
        assert r.json()["errcode"] == 0
        return r.json()

    def create_department(self, department_name, parentid):
        create_department_url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        data = {"name": department_name,"parentid": parentid}

        r = requests.post(create_department_url,
                          params={"access_token": self.get_token(self.secret)},
                          json=data)
        self.format(r.json())
        assert r.json()["errcode"] == 0
        return r.json()

    def upgrade_department(self, id,**kwargs):
        upgrade_department_url = "https://qyapi.weixin.qq.com/cgi-bin/department/update"

        data = {"id": id}
        data.update(kwargs)
        r = requests.post(upgrade_department_url,
                          params={"access_token": self.get_token(self.secret)},
                          json=data)
        self.format(r.json())
        assert r.json()["errcode"] == 0
        return r.json()

    def delete_department(self,department_id):
        department_list_url = "https://qyapi.weixin.qq.com/cgi-bin/department/delete"
        r = requests.get(department_list_url,
                         params={"access_token": self.get_token(self.secret),"id":department_id})

        self.format(r.json())
        assert r.json()["errcode"] == 0
        return r.json()
