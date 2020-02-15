# coding=utf-8
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestHomeWork_7:
    def setup_method(self):
        chrome_options = webdriver.ChromeOptions()
        # chrome.exe --remote-debugging-port=9222
        chrome_options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_options)
        # self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        time.sleep(10)
        # self.driver.close()

    def wait(self, time_out, method):
        WebDriverWait(self.driver, time_out).until(method)

    @pytest.mark.parametrize('member_information', [
        {
            'member_name': 'new_guy_00',
            'icon':'E:\\picture\\xiugai1.jpg',
            'member_mail': 'new_guy_00@qq.com',
            'member_phone': '',
            'member_account': 'new_guy_00',
            'member_sex': 'girl',
            'department': 'department_01'}
    ])
    def test_wexin(self, member_information):
        """
        企业微信添加 成员信息（包括头像、姓名、邮箱、账号、性别、部门） 其他信息大同小异，不做添加
        :param member_information:
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR,
                                 '.index_service_cnt_itemWrap:nth-child(1) .index_service_cnt_item_title').click()

        #  选择部门
        if member_information['department']:
            # 部门信息判断是否不为空，有则添加到对应部门下
            # 对于选择部门 还有一种情况没有做判断处理，不做过多扩展,主要是懒LOL
            department = member_information['department']
            self.wait(5, EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.js_btn_continue')))
            self.driver.find_element(By.ID, 'memberSearchInput').send_keys(department)

            self.driver.find_element(By.CSS_SELECTOR, '#search_party_list a').click()  # 这里必须点击，否则style为空
            if 'display: none' not in self.driver.find_element(By.CSS_SELECTOR, '.js_no_member').get_attribute('style'):
                # 该部门下没有成员
                self.driver.find_element(By.CSS_SELECTOR, '.js_no_member .js_add_member').click()
                self.wait_element(5, (By.CSS_SELECTOR, '.js_no_member .js_add_member'))
            else:
                # 该部门下已有成员
                self.driver.find_element(By.CSS_SELECTOR, '.js_has_member .js_add_member').click()
                self.wait_element(5, (By.CSS_SELECTOR, '.js_has_member .js_add_member'))

        self.wait(5,
                  EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.member_edit_formWrap [placeholder="姓名"]')))
        self.driver.find_element(By.CSS_SELECTOR, '.member_edit_formWrap [placeholder="姓名"]'). \
            send_keys(member_information['member_name'])  # 输入姓名

        if member_information['icon']:
            # 上传头像 (发现头像上传也挺有意思的，添加这部分的信息）
            # 判断头像信息是否为空，是就添加，不是就不添加
            self.driver.find_element(By.CSS_SELECTOR, '.ww_icon_CameraWhiteSmall').click()
            self.wait(3, EC.visibility_of_all_elements_located((By.CSS_SELECTOR,'.js_no_img')))
            # self.driver.find_element(By.CSS_SELECTOR, '.js_no_img a').click()
            self.driver.find_element(By.CSS_SELECTOR, '.js_no_img a .js_file').send_keys(member_information['icon'])
            self.driver.find_element(By.CSS_SELECTOR, '.js_save').click()
            self.wait(5, lambda x: 'display: block' in self.driver.find_element(By.CSS_SELECTOR, '.success').
                      get_attribute('style'))

        self.driver.find_element(By.CSS_SELECTOR, '.member_edit_formWrap #memberAdd_acctid'). \
            send_keys(member_information['member_account'])  # 输入账号

        self.driver.find_element(By.CSS_SELECTOR, '.member_edit_formWrap #memberAdd_mail'). \
            send_keys(member_information['member_mail'])  # 输入邮箱

        if member_information['member_sex'] == 'girl':
            value = "2"
            self.driver.find_element(
                By.CSS_SELECTOR,
                '.member_edit_sec:nth-child(1) .member_edit_item_Radios [value="{value}"]'.format(value=value)).click()
            # 点击“女”
        else:
            value = "1"

        self.driver.find_element(By.CSS_SELECTOR, '.js_btn_save').click()

    def wait_element(self, time_out, selector):
        """
        判断是否跳转，没有跳转重复点击（目前只有两个地方会调用这个函数，就不做过多兼容了）
        :param time_out: 超时时间
        :param selector: 元素选择器
        :return:
        """
        # selector = (By.CSS_SELECTOR, '.js_no_member .js_add_member')
        time_deadline = time.time() + time_out
        while True:
            elements = self.driver.find_elements(By.CSS_SELECTOR, '.js_btn_continue')
            if len(elements) < 1:
                self.driver.find_element(*selector).click()

            elif len(elements) >= 1:
                break
            if time.time() == time_deadline:
                break