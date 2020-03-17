import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from test_selenium_po.page.base_page import BasePage


class Contacts(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#contacts"

    def add_member(self, member_name, icon, member_account, member_mail, member_sex):
        self.wait(3, EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.js_has_member .js_add_member')))
        self.find(By.CSS_SELECTOR, '.js_has_member .js_add_member').click()
        self.wait_page_jump(5, (By.CSS_SELECTOR, '.js_has_member .js_add_member'),
                            (By.CSS_SELECTOR, '.js_btn_continue'))

        self.find(By.CSS_SELECTOR, '.member_edit_formWrap [placeholder="姓名"]').send_keys(member_name)  # 输入姓名

        self.find(By.CSS_SELECTOR, '.ww_icon_CameraWhiteSmall').click()
        self.wait(3, EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.js_no_img')))
        self.find(By.CSS_SELECTOR, '.js_no_img a .js_file').send_keys(icon)  # 上传头像
        self.find(By.CSS_SELECTOR, '.js_save').click()
        # self.wait(5, lambda x: 'display: block' in self.find(By.CSS_SELECTOR, '.success').get_attribute('style'))

        self.find(By.CSS_SELECTOR, '.member_edit_formWrap #memberAdd_acctid').send_keys(member_account)  # 输入账号

        self.find(By.CSS_SELECTOR, '.member_edit_formWrap #memberAdd_mail').send_keys(member_mail)  # 输入邮箱

        if member_sex == 'girl':
            value = "2"
            self.find(By.CSS_SELECTOR, '.member_edit_sec:nth-child(1) .member_edit_item_Radios [value="{value}"]'.
                      format(value=value)).click()  # 点击“女”

        self.find(By.CSS_SELECTOR, '.js_btn_save').click()

    def add_member_success(self):
        # 通讯录成员存在
        self.find(By.ID, 'menu_index').click()
        self.find(By.ID, 'menu_contacts').click()
        result = list()
        for element in self.find_elements(By.CSS_SELECTOR, '[data-type=member] td:nth-child(2)'):
            result.append(element.get_attribute('title'))

        return result

    def edit_member(self, member_name, member_information):
        mail_selector = (By.ID, 'memberEdit_mail')
        name_selector = (By.CSS_SELECTOR, '[name=username]')
        sex_selector_ = '.member_edit_sec:nth-child(1) .member_edit_item_Radios [value="%s"]'
        phone_country_code_selector = (By.CSS_SELECTOR, '[name=country_code]')
        phone_selector = (By.CSS_SELECTOR, '[name=mobile]')
        save_selector =(By.CSS_SELECTOR, '.js_save')
        self.find(By.CSS_SELECTOR, f'[title={member_name}]').click()
        self.find(By.LINK_TEXT, '编辑').click()

        if member_information['member_name']:
            self.find(name_selector).clear()
            self.find(name_selector).send_keys(member_information['member_name'])

        if member_information['member_sex']:
            if member_information['member_sex'] == 'girl':
                value = "2"
            else:
                value = "1"
            self.find(By.CSS_SELECTOR, sex_selector_ % value).click()

        if member_information['member_phone']:
            phone_area = member_information['member_phone'].split(' ')[0]
            phone_number = member_information['member_phone'].split(' ')[1]
            self.find(phone_country_code_selector).click()
            self.find(By.PARTIAL_LINK_TEXT, phone_area).click()
            self.find(phone_selector).clear()
            self.find(phone_selector).send_keys(phone_number)

        if member_information['member_mail']:
            self.find(mail_selector).clear()
            self.find(mail_selector).send_keys(member_information['member_mail'])

        self.find(save_selector).click()

    def edit_member_success(self):
        name_selector = (By.CSS_SELECTOR, '.member_display_cover_detail_name')
        phone_selector = (By.CSS_SELECTOR,
                          '.member_display_item_Phone .member_display_item_right')
        email_selector = (By.CSS_SELECTOR,
                          '.member_display_item_Email .member_display_item_right')

        result = dict()
        result['member_name'] = self.find(name_selector).text
        result['member_phone'] = self.find(phone_selector).text
        result['member_mail'] = self.find(email_selector).text
        return result


