import datetime
import time
class PhoneNo():
    #手机号码类
    def __init__(self):
        pass
    def getno(self,info):
        phone_list=[]
        time_info=time.localtime(time.time())
       #print(time_info.tm_year,time_info.tm_mon,time_info.tm_mday)
        for i in range(10):
    #手机号码的规则是 17+ 年+月+日 + 1-10 之间的数
            if time_info.tm_mon < 10:
                tempMon_str="0"+str(time_info.tm_mon)  #1-9 月变为01、02、、、、
            phone_no="17"+str(time_info.tm_year)+tempMon_str+str(time_info.tm_mday)+str(i)
            phone_list.append(phone_no)
        return phone_list[info]
# if __name__ == '__main__':
#     info=PhoneNo()
#     print(info.getno())




