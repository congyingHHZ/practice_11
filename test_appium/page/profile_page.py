from selenium.webdriver.common.by import By

from test_appium.page.base_page import BasePage


class Profile(BasePage):

    def login_password(self, account, password):
        self.find(By.ID,'login_account').send_keys(account)
        self.find(By.ID,'login_password').send_keys(password)
        self.find(By.ID,'button_next').click()
        tip = self.find(By.ID,'md_content').text
        self.find(By.ID,'md_buttonDefaultPositive').click()

        return tip
