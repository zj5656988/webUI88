from commonfunction.driver import Driver
class Main():
    def gotowork_button(self):  #开始工作按钮
        gotowork_button=Driver.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div/div[3]/button")
        return gotowork_button
    def passdoor(self):         #传送门
        passdoor=Driver.driver.find_element_by_xpath("//*[text()='传送门']")
        return passdoor
    def incall_passdoor(self):  #内呼传送门
        incall_passdoor=Driver.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div/ul/li[5]/ul/li[7]/a")
        return incall_passdoor
    def input_passdoor(self):  #传送门输入页
        input_passdoor=Driver.driver.find_element_by_id("name")
        return input_passdoor
    def c2incall(self):       #C2内呼按钮
        c2incall_button=Driver.driver.find_element_by_xpath("//*[text()='C2内呼']")
        return c2incall_button
