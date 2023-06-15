
from appium import webdriver


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
