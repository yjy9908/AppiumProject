import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy,By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions



#1、设置终端参数项
desired_caps={
    "platformName":"Android",
    "platformVersion":"7.1.2",
    "deviceName":"yjy",
    "appPackage":"com.km.karaoke",
    "appActivity":"com.utalk.hsing.activity.StartActivity",
    "noReset":True

}

#2、appium server进行启动


#3、发送指令给到appium server
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

#driver.implicitly_wait(30)
# psd=driver.find_element(By.XPATH, "//*[@resource-id='com.km.karaoke:id/activity_account_login_password']").send_keys("123456")
#
# btn=driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Đăng nhập").resourceId("com.km.karaoke:id/activity_account_login_btn_login")')
# btn.click()
#btn=driver.find_element(By.ID,"com.km.karaoke:id/activity_account_login_btn_login").click()


window_size=driver.get_window_size()
print("手机屏幕尺寸：",window_size)
x=window_size['width']
y=window_size['height']
print(x)
time.sleep(20)

for i in range(0,2):
    driver.swipe(start_x=x*0.9,  start_y=y*0.5,end_x=x*0.1,end_y=y*0.5,duration=1000)