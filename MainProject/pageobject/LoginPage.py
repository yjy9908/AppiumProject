import time

from appium.webdriver.common.mobileby import MobileBy

from MainProject.base.BasePage import BasePage


class LoginPage(BasePage):

    #特有的属性
    el_agreemedia=(MobileBy.ID,"com.android.packageinstaller:id/permission_allow_button")
    el_agreetrem=(MobileBy.ID,"com.km.karaoke:id/check_iv")
    el_phoneicon = (MobileBy.ID, "com.km.karaoke:id/login_by_phone")
    el_phone=(MobileBy.ID,"com.km.karaoke:id/activity_account_login_phone_number")
    el_checkphonebtn=(MobileBy.ID,"com.km.karaoke:id/activity_account_login_btn_login")
    el_password=(MobileBy.ID,"com.km.karaoke:id/activity_account_login_password")
    el_login=(MobileBy.ID,"com.km.karaoke:id/activity_account_login_btn_login")


    #特有的行为
    def login(self,phone,password):
        self.click(self.el_agreemedia)
        self.click(self.el_agreetrem)
        self.click(self.el_phoneicon)
        self.input(self.el_phone,phone)
        self.click(self.el_checkphonebtn)
        self.input(self.el_password,password)
        self.click(self.el_login)
