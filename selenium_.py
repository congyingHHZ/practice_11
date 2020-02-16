import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC

class TestHogwarts:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)

    def teardown_method(self):
        time.sleep(5)
        self.driver.quit()

    def test_click(self):
        self.driver.get("https://testerhome.com/")
        # self.driver.set_window_size(1295, 695)
        # self.driver.find_element(By.LINK_TEXT, "社团").click()
        # time.sleep(1)
        # self.driver.find_element(By.CSS_SELECTOR, "霍格沃兹测试学院").click()
        # WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".MTSC2020* ")))
        self.driver.find_element(By.CSS_SELECTOR, ".MTSC2020* ").click()
