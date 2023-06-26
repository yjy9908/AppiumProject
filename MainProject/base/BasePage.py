

class BasePage:

    def __init__(self,driver):
        self.driver = driver


    #元素定位
    def locator(self,loc):

        return self.driver.find_element(*loc)


    #输入
    def input(self,loc,value):
        self.locator(loc).send_keys(value)

    #点击
    def click(self,loc):
        self.locator(loc).click()