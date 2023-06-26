# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os

import pytest




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pytest.main(['-s','./MainProject/testcases/TestLogin.py','--alluredir','./MainProject/result/temp_jsonreport'])
    os.system("allure generate ./result/temp_jsonreport -o ./report/html --clean")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
