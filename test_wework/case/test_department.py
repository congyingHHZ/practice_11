import json

import pytest

from test_wework.api.department import Department
from test_wework.api.wework import WeWork


class TestDepartment:
    secret = "hFSgf7rHTuT9qmA8VIViem9T1RY1aMsppdpYdofjX54"

    @classmethod
    def setup_class(cls):
        cls.department_api = Department()
        # cls.token = WeWork.get_token(cls.secret)

    def test_department_list(self):

        department_list = self.department_api.get_list()["department"]

        assert "department_02" in "|".join([i["name"] for i in department_list])
        return department_list

    @pytest.mark.parametrize("department_name, parentid",[("department_04", 2)])
    def test_create_department(self,department_name, parentid):
        # 创建部门
        self.department_api.create_department(department_name, parentid)

        assert department_name in "|".join([i["name"] for i in self.department_api.get_list()["department"]])

    @pytest.mark.parametrize("department_id, department_name", [(7, "new")])
    def test_upgrade_department(self,department_id,department_name):
        self.department_api.upgrade_department(7, name=department_name)
        assert department_name in "|".join([i["name"] for i in self.department_api.get_list()["department"]])

    @pytest.mark.parametrize("department_id", [7])
    def test_delete_department(self, department_id):
        self.department_api.upgrade_department(department_id)
        assert str(department_id) in "|".join([str(i["id"]) for i in self.department_api.get_list()["department"]])
