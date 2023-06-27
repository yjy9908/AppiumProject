import os
import time

import pytest
import allure
from appium import webdriver
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from MainProject.common.DataTurn_excel import DataTurn_excel
from MainProject.common.data_util import readYaml

from MainProject.pageobject.LoginPage import LoginPage
from appium.webdriver.common.appiumby import By


nowtime=time.strftime('%Y-%m-%d-%H_%M_%S',time.localtime(time.time()))
# 日志配置
logging.basicConfig(
    level=logging.INFO,
    filename="../result/log/appium-%s.log" % nowtime,
    format="[%(asctime)s %(levelname)s] %(filename)s : %(message)s",
)


@allure.feature("登录")
class TestLogin:

    def setup(self):
        rootPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        # 路径拼接
        path = os.path.join(rootPath, "config\config.yaml")
        data = readYaml(path)
        logging.info("测试开始")
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", data["desired_caps"])

    @allure.story("用户登录")
    @pytest.mark.parametrize('phone,pswd', DataTurn_excel.read_data_from_excel("../data/account.xlsx", 'account'))
    def testlogin(self, phone, pswd):
        logging.info("用户登录用例执行")
        login_page = LoginPage(driver=self.driver)
        self.driver.implicitly_wait(20)
        login_page.login(phone, pswd)
        driver = self.driver
        btn = "//*[@resource-id='showSignInPop']/android.view.View[2]/android.view.View[12]"
        x1 = WebDriverWait(driver, 5 * 60, 1000).until(EC.visibility_of_element_located((By.XPATH, btn)))
        x1.click()
        assert EC.visibility_of_element_located((By.ID, "com.km.karaoke:id/tab_layout_text_id"))

    def teardown(self):
        """ tearDown  """
        logging.info('测试用例执行完毕，测试环境正在还原！')
        time.sleep(15)
        print("teardown")
        self.driver.quit()


if __name__ == '__main__':
    pytest.main(['-s', 'TestLogin.py', '--alluredir', '../result/temp_jsonreport'])
    os.system('allure generate ../result/temp_jsonreport -o ../result/report/html --clean')
