import re

class Common_re():
    def number_re(self,str1):
        patten=re.compile(r"\d+")
        result=patten.findall(str(str1))
        return result[0]
# if __name__ == '__main__':
#     str="()(400)"
#     x=Common_re().number_re(str)
#     print(x[0])

