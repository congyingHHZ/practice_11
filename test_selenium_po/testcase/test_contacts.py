import os
import time

import pytest
from selenium.webdriver.common.by import By

from test_selenium_po.page.contacts import Contacts


class TestContact:
    def setup(self):
        self.contact = Contacts(reuse=True)

    @pytest.mark.parametrize('member_information', [
        {
            'member_name': 'zxcvbnm',
            'icon': 'icon.jpg',
            'member_mail': '12345@qq.com',
            'member_phone': '',
            'member_account': '123445',
            'member_sex': 'girl',
            'department': 'department_01'}
    ])
    def test_add_member(self, member_information):
        current_path = os.path.dirname(os.getcwd())
        icon_path = os.path.join(current_path, 'picture', member_information['icon'])

        self.contact.add_member(member_information['member_name'],
                                icon_path,
                                member_information['member_account'],
                                member_information['member_mail'],
                                member_information['member_sex'])
        time.sleep(0.5)
        assert member_information['member_name'] in self.contact.add_member_success()

    @pytest.mark.parametrize('member_name, member_information', [
        ('zxcvbnm', {
            'member_name': 'zxcvbnm11',
            'icon': 'icon.jpg',
            'member_mail': 'abcdf@qq.com',
            'member_phone': '+852 888888888',
            'member_sex': 'boy',
            'department': 'department_01'})
    ])
    def test_change_member(self, member_name, member_information):
        self.contact.edit_member(member_name, member_information)

        assert member_information['member_name'] == self.contact.edit_member_success()['member_name']
        assert member_information['member_phone'].replace(' ', '') == self.contact.edit_member_success()['member_phone']
        assert member_information['member_mail'] == self.contact.edit_member_success()['member_mail']




