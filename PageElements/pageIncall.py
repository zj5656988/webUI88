from commonfunction.driver import Driver
class incall():
    def input_name(self):  #输入姓名
        input_name=Driver.driver.find_element_by_xpath("//*[@id='name']")
        return input_name
    def fenqi_button(self):  #选择是否分期
        fenqi_button=Driver.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[2]/form/div[3]/div[1]/div/div[2]/div/span/div/label[3]/span[1]/input")
        return fenqi_button

    def endcode_jthgd(self): #约定日联系结束码
         ydrlx=Driver.driver.find_element_by_xpath("//*[text()='接通后挂断']")
         return ydrlx

    def souce_58(self):   #渠道来源
        Driver.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[3]/div[1]/div[2]/div/div/div/form/div[1]/div[2]/div/span/div/span/input").click()
        Driver.driver.find_element_by_xpath("//*[text()='58同城']").click()
        souce_58=Driver.driver.find_element_by_xpath("//*[text()='B2C 58同城']")
        return souce_58

    def save_data(self):
        save_data=Driver.driver.find_element_by_xpath("//*[text()='保存工单']")
        return save_data



