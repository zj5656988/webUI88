from  selenium import webdriver
import time
class Driver():
    driver = webdriver.Firefox()
    def open_browser(self):
        self.driver.get("http://uat.crm.yxqiche.com")
        #self.driver.get_screenshot_as_file("C:\\Users\Administrator\Desktop\\demo.png")
        time.sleep(3)
        self.driver.find_element_by_id("chromeClose").click()   #点击关闭浏览器切换提示
        self.driver.delete_all_cookies() #清除数据
        print("浏览器打开，关闭了谷歌提示")
    def end_browser(self):
        self.driver.delete_all_cookies()  #删除所有cookies

    def quit_browser(self):
        self.driver.quit()

# if __name__ == '__main__':
#     demo=Driver()


