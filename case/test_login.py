from commonfunction.driver import Driver
import time
import unittest
from PageElements.pageLogin import Login
from PageElements.pageMain import Main
from commonfunction.excel_data import Excel
from commonfunction.function_mysql import Function_Mysql
from commonfunction.phone_no import PhoneNo
from commonfunction.common_re import Common_re

from PageElements.pageIncall import incall

class Login_case(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        Driver().open_browser() #打开浏览器
        Driver().end_browser()    #清缓存
        time.sleep(3)
    @classmethod
    def tearDownClass(cls): #结束case，输出123
        # Driver().end_browser()
        # Driver().quit_browser()
            pass
    def test_001(self):    #定位用户名输入框
        # print(Excel().excel("b2"),Excel().excel("c2"))
        Login().username().send_keys(Excel().excel_read("b2"))
        Login().password().send_keys(Excel().excel_read("c2"))
        Login().login_key().click()
        self.assertEqual("开始工作",Main().gotowork_button().text)

    def test_002(self):
        Main().passdoor().click()
        Main().incall_passdoor().click()
        Main().input_passdoor().send_keys(PhoneNo().getno(2))
        Main().c2incall().click()
        incall().input_name().send_keys(Excel().excel_read("b2"))
        incall().fenqi_button().click()
        incall().endcode_jthgd().click()
        incall().souce_58().click()
        incall().save_data().click()
        mysql_info="select task_priority from used_car_task WHERE biz_no IN (SELECT biz_no from c2_biz_info WHERE customer_phone=%s)"%PhoneNo().getno(2)
        tempInfo=Function_Mysql().Function_mysql_select(mysql_info)
        real_task_priority=Common_re().number_re(tempInfo)
        self.assertEqual(str(400),real_task_priority)


# if __name__ == '__main__':
#     unittest.main(Login_case)






