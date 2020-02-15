from selenium.webdriver.common.by import By

from test_selenium_po.page.base_page import BasePage


class ManageTool(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#manageTools"

    def add_material_pic(self, pic_path):
        # self.find(By.LINK_TEXT, '素材库').wait()
        self.find((By.PARTIAL_LINK_TEXT, "素材库")).click()
        self.find(By.LINK_TEXT, "图片").click()
        self.find(By.LINK_TEXT, "添加图片").click()
        self.find(By.CSS_SELECTOR,'[name=uploadImageFile]').send_keys(pic_path)
        self.find(By.CSS_SELECTOR, ".qui_btn").click()
        return self
