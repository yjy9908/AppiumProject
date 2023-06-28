# coding=utf-8
import os
import time

import pytest
import logging

nowtime=time.strftime('%Y-%m-%d-%H_%M_%S',time.localtime(time.time()))
# 日志配置
logging.basicConfig(
    level=logging.INFO,
    filename="./result/log/appium-%s.log" % nowtime,
    format="[%(asctime)s %(levelname)s] %(filename)s : %(message)s",
)



if __name__ == '__main__':
    pytest.main(['-s', './testcases/TestLogin.py', '--alluredir', './result/temp_jsonreport'])
    os.system('allure generate ./result/temp_jsonreport -o ./result/report/html --clean')