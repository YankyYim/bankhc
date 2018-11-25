#coding=utf-8
import pymysql  # 导入 pymysql



class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, data, url):
        #print(data)
        if data is None:
            return
        self.datas.append(data)
        #print(data)

        try:
            db = pymysql.connect(host="localhost", user="root",
                             password="yankeyun", db="imooc", port=3306)

            cur = db.cursor()
        except Exception as e1:
            print(e1)

        str_tittle=data['tittle']
        #print(str_tittle)

        str_time=data['time']
        #print(str_time)

        str_bank= data['bank']

        str_url = "http://m.yinhangzhaopin.com/m/" + str(url) + ".htm"


        sql_insert = "insert into url_tittle_time_bank values('%s','%s','%s','%s')" %(str_url,str_tittle,str_time,str_bank)
        print(sql_insert)

        try:
            cur.execute(sql_insert)
            # 提交
            db.commit()
            print(sql_insert)
        except Exception as e:
            # 错误回滚
            print(e)
            db.rollback()
        finally:
            cur.close()
            db.close()

    def output_html(self,new_detail):
        fout = open('output.html','a+')
        try:
            # print(str(new_detail))
            fout.write(str(new_detail))
        except Exception as e1:
            print(e1)
        finally:
            fout.close()



