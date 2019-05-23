from  selenium import webdriver
import time
class Driver():
    driver = webdriver.Firefox()
    def __init__(self):
        self.driver.get("http://uat.crm.yxqiche.com")
        time.sleep(2)
        self.driver.get_screenshot_as_file("C:\\Users\Administrator\Desktop\\demo.png")
        time.sleep(3)
        self.driver.find_element_by_id("chromeClose").click()   #点击关闭浏览器切换提示
        self.driver.delete_all_cookies() #清除数据
        print("输出")
    def test(self):
        print("test")

# if __name__ == '__main__':
#     demo=Driver()
#     demo.test()


