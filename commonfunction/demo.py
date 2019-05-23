# # 1、 题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
# info_list=[1,2,3,4] #初始数字的列表
# for i in range(1,5):
#     for k in range(1,5):
#         for j in range(1,5):
#             if (i != k) and (j != k) and ( i != j):
#                 print(i,j,k)


#题目：输入三个整数x,y,z，请把这三个数由小到大输出。
# a,b,c=input().split()
# #冒泡排序
# list=[1,3,45,2,45,343,11,2,0]
# for temp1 in range(len(list)-1):
#     for temp2 in range(len(list)-1-temp1):
#         if list[temp2]>list[temp2+1]:
#             list[temp2],list[temp2+1]=list[temp2+1],list[temp2]
# print(list)
# list=[]
# for i in range(3):
#     info=input("please:")
#     list.append(info)
# list.sort()
# print(list)
# a = 176
# b = 219
# print(chr(b),chr(a),chr(a),chr(a),chr(b) )
# print (chr(a),chr(b),chr(a),chr(b),chr(a))
# print (chr(a),chr(a),chr(b),chr(a),chr(a) )
# print (chr(a),chr(b),chr(a),chr(b),chr(a) )
# print (chr(b),chr(a),chr(a),chr(a),chr(b))
# #99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d * %d =%d "%(i,j,i*j),end=" ")
#     print(" ")]
#输出100-200之间素数
# list=[]
# temp_list=[]
# for i in range(100,201):
#     for j in  range(2,i):
#         if i%j == 0:
#             if i not in list:
#                 list.append(i)
# for i in range(100,201):
#     if i not  in list:
#         temp_list.append(i)
# print(temp_list)
# # print(list)
"""
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
1.程序分析：利用while语句,条件为输入的字符不为’\n’.
"""
# str_info=input("请输入一行字符")
#统计一篇文章出现最多次数的字符。
# temp_str="一天两天三天四天"
# max_info=1
# for i in temp_str:
#     info=temp_str.count(i)
#     if info >= max_info:
#         max_info=info
#         max_i=i
# print(str(max_i)+str(max_info))
#字符压缩

#1、遍历字符串
#2、获取下一个字符，判断是否和第一个字符是一致的。
#3、如果是一致的，count+1
#4、拼接起来，填到列表里。
#5、输出列表
# class Zipper:
#     def zipstring(self,string):
#         str_info=string[0]
#         count=0
#         result=""
#         for temp in string:
#             if temp==str_info:
#                 count+=1
#
#             else:
#                 result+=str_info+str(count)
#                 str_info=temp
#                 count=1
#         result+=str_info+str(count)
#         return  result
# if __name__ == '__main__':
#     str1 = "aaabbbbbccdfffffffff"
#     exp=Zipper()
#     print(exp.zipstring(str1))
#     print(str1)
#统计每个字符的出现次数
#统计一个字符串中的每一个字符出现了多少次 #定义一个字符串 str = 'abbcccdddd' #在字符串的每一个字符之间插入一个空格组成一个新的字符串 str = ' '.join(str) #打印新的字符串看看 print('str = ',str) #将新字符串按空格分割成一个列表 li = str.split(' ') #打印新的列表 print('li = ',li) #统计每一个字符出现的次数: #方式一 for i in set(li): if li.count(i) >= 1: print('%s 出现了%d 次!'%(i, li.count(i))) print('*'*50)
#
#unnitest
import unittest
def add(a,b):
    return a+b
def mins(a,b):
    return a-b
def multi(a,b):
    return a*b
def chu(a,b):
    return a/b

class testmath(unittest.TestCase):
    @classmethod
    def tearDown(self):
        print("所有用例执行前的清理工作")
    @classmethod
    def setUp(self):
        print("所有用例执行后的开始工作")
    #@unittest.skip

    def test00ces(self):
        print("测试加法")
        self.assertEqual(4,add(1,2))

    def test001(self):
        print("测试减法")
        self.assertEqual(1,mins(2,1))

    def test003(self):
        print("测试乘法")
        self.assertEqual(6,multi(2,3))

if __name__ == '__main__':
    suitInfo=unittest.TestSuite()
    test_case=[testmath("test00ces"),testmath("test001")]
    suitInfo.addTests(test_case)
    runner=unittest.TextTestRunner(verbosity=2)
    runner.run(suitInfo)













