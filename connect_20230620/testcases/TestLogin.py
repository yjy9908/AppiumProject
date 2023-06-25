import os
#from ddt import ddt,file_data

import pytest
from appium import webdriver

from connect_20230620.common.DataTurn_excel import read_data_from_excel
from connect_20230620.common.data_util import readYaml

from connect_20230620.pageobject.LoginPage import LoginPage


class TestLogin:

    def setup(self):
        rootPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        # 路径拼接
        path = os.path.join(rootPath, "config\config.yaml")
        data=readYaml(path)
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",data["desired_caps"])


    @pytest.mark.parametrize('phone,pswd',read_data_from_excel("../data/account.xlsx",'account'))
    def test_login(self,phone,pswd):
        login_page=LoginPage(driver=self.driver)
        self.driver.implicitly_wait(15)
        login_page.login(phone,pswd)

if __name__ == '__main__':
    pytest.main()