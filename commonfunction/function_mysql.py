import pymysql
from commonfunction.phone_no import PhoneNo
class Function_Mysql():
    db=pymysql.connect(host="opm01.taoche.cn",user="temp_admin",password="temp_admin@2018",db="ucarcrm",port=20051)
    cur=db.cursor()

    def Function_mysql_select(self,str):  #数据库查询
        Function_Mysql.cur.execute(str)
        results=Function_Mysql.cur.fetchall()
        Function_Mysql.db.close()
        return results

    def Function_mysql_delete(self,str):  #删除数据
        Function_Mysql.cur.execute(str)
        Function_Mysql.db.commit()
        Function_Mysql.db.close()

if __name__ == '__main__':
    str=Function_Mysql().Function_mysql_select("select task_priority from used_car_task WHERE biz_no IN (SELECT biz_no from c2_biz_info WHERE customer_phone=%s)"%PhoneNo().getno(2))
    print(str)