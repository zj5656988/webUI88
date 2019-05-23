
from  selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from   commonfunction import phone_no
driver=webdriver.Firefox()
driver.delete_all_cookies()
driver.get("http://uat.crm.yxqiche.com")
time.sleep(2)
driver.get_screenshot_as_file("C:\\Users\Administrator\Desktop\\demo.png")
time.sleep(3)
driver.find_element_by_id("chromeClose").click()   #点击关闭浏览器切换提示
driver.find_element_by_id("username").send_keys("chejing")
driver.find_element_by_id("password").send_keys("uat.portal")
time.sleep(2)
driver.find_element_by_class_name("btn-submit").click()
time.sleep(5)
# driver.delete_all_cookies()
# phone_info=phone_no.PhoneNo(1)
# #driver.find_element_by_xpath("//*span[text()='传送门']").click()
# driver.find_element_by_xpath("//*[text()='传送门']").click()
# time.sleep(2)
# driver.find_element_by_css_selector('li.ant-menu-item:nth-child(2) > a:nth-child(1)').click()
# #点击内呼传送门
# driver.find_element_by_id("name").send_keys("123")
# driver.find_element_by_css_selector("button.ant-btn:nth-child(2)").click()
time.sleep(5)
# info=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div/div[3]/button").text
# print(info)
#driver.find_element_by_css_selector("li.ant-menu-submenu:nth-child(4) > div:nth-child(1)").click()
# driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div/ul/li[4]/div[1]").click()
driver.find_element_by_xpath("//*[text()='传送门']").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div/ul/li[5]/ul/li[7]/a").click()
driver.find_element_by_id("name").send_keys(17201901225 )
driver.find_element_by_xpath("//*[text()='C2内呼']").click()
driver.find_element_by_xpath("//*[@id='name']").send_keys("自动化测试")
driver.find_element_by_xpath("//*[text()='接通后挂断']").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[2]/form/div[3]/div[1]/div/div[2]/div/span/div/label[3]/span[1]/input").click()
#分期按钮
driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[3]/div[1]/div[2]/div/div/div/form/div[1]/div[2]/div/span/div/span/input").click()
#driver.find_element_by_xpath("")
driver.find_element_by_xpath("//*[text()='58同城']").click()
driver.find_element_by_xpath("//*[text()='B2C 58同城']").click()



# info=Select(driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[3]/div[1]/div[2]/div/div/div/form/div[1]/div[2]/div/span/div/span/input"))
# info2=Select(info.select_by_visible_text("淘车无忧"))
# info3=info2.select_by_visible_text("淘车无忧")
driver.find_element_by_xpath("//*[text()='保存工单']").click()


