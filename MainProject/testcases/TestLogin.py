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

    def setup_class(self):
        rootPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        # 路径拼接
        path = os.path.join(rootPath, "config\config.yaml")
        data = readYaml(path)
        logging.info("测试开始")
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", data["desired_caps"])

    @allure.story("用户登录")
    #@pytest.mark.parametrize('phone,pswd', DataTurn_excel.read_data_from_excel("./data/account.xlsx", 'account'))
    def testlogin(self):
        logging.info("用户登录用例执行")
        login_page = LoginPage(driver=self.driver)
        self.driver.implicitly_wait(20)
        login_page.login("1234567807","123456")
        time.sleep(6)
        try:
            #用绝对路径，路径前面加r，表示不转义
            self.driver.get_screenshot_as_file(r'E:\python_workspace\AppiumProject\MainProject\result\screenshot' +'\\'+nowtime+ "screenshot.png")
            logging.info("截图成功")
        except:
            logging.info("截图失败")
        btn = "//*[@resource-id='showSignInPop']/android.view.View[2]/android.view.View[12]"
        x1 = WebDriverWait(self.driver, 5 * 60, 1000).until(EC.visibility_of_element_located((By.XPATH, btn)))
        x1.click()
        assert EC.visibility_of_element_located((By.ID, "com.km.karaoke:id/tab_layout_text_id"))

    @allure.story("首页滑动")
    def testslip(self):
        window_size = self.driver.get_window_size()
        print("手机屏幕尺寸：", window_size)
        x = window_size['width']
        y = window_size['height']
        print(x)
        time.sleep(6)
        logging.info("首页滑动用例执行")
        for i in range(0, 2):
            self.driver.swipe(start_x=x * 0.9, start_y=y * 0.5, end_x=x * 0.1, end_y=y * 0.5, duration=1000)
        assert self.driver.find_element(By.XPATH,"//android.widget.HorizontalScrollView/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]").is_selected()==True


    def teardown_class(self):
        """ tearDown  """
        logging.info('测试用例执行完毕，测试环境正在还原！')
        time.sleep(15)
        print("teardown")
        self.driver.quit()
        # try:
        #     self.driver.refresh()
        # except ConnectionAbortedError as e:
        #     logging.info(e)

if __name__ == '__main__':
    pytest.main(['-s', 'TestLogin.py', '--alluredir', '../result/temp_jsonreport'])
    os.system('allure generate ../result/temp_jsonreport -o ../result/report/html --clean')
