from commonfunction.driver import Driver
from commonfunction.phone_no import PhoneNo
from commonfunction.excel_data import Excel
from commonfunction.function_mysql import Function_Mysql
from PageElements.pageMain import Main
from PageElements.pageIncall import incall
import unittest

class test_Task(unittest.TestCase):
    def test_task_follow(self):
        Main().passdoor().click()
        Main().incall_passdoor().click()
        Main().input_passdoor().send_keys(PhoneNo().getno(2))
        Main().c2incall().click()
        incall().input_name().send_keys(Excel().excel_read("b2"))
        incall().fenqi_button().click()
        incall().endcode_ydrlx().click()
        incall().souce_58().click()
        incall().save_data().click()
        mysql_info="select task_priority from used_car_task WHERE biz_no IN (SELECT biz_no from c2_biz_info WHERE customer_phone=%s)"%PhoneNo().getno(2)
        self.assertEqual(400,Function_Mysql.Function_mysql_select(mysql_info))

