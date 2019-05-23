from commonfunction.driver import Driver
import time
class Login():

    def username(self):     #定位用户名输入框
        username=Driver.driver.find_element_by_id("username")
        return username

    def password(self):  #定位密码输入框
        password=Driver.driver.find_element_by_id("password")
        return password

    def login_key(self):
        login_key=Driver.driver.find_element_by_class_name("btn-submit")
        return login_key


