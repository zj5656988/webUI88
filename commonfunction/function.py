from selenium import webdriver
from  commonfunction.driver import Driver
class Function():    #selenium方法
    def prtsc(self):
        Driver.driver.get_screenshot_as_file("C:\\Users\Administrator\Desktop\webUI\\demo.png")
    #截图




