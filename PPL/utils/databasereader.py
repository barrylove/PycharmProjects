import pymysql

class databaseReader:
    def __init__(self):
        self.datas = pymysql.connect(
            host="192.168.63.164",
            user="qamodify",
            password="0n1kcfrm",
            db="org",
            port=3306)

    def datareader_phase(self, parm):
        cursor = self.datas.cursor()
        query = "select b.phase_code from t_opp_customer as a left join t_opp_cust_business_phase as b on a.id = b.cust_id where a.cust_name = \"%s\"" % parm
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()
        return result

    def datareader_visttime(self, parm):
        cursor = self.datas.cursor()
        query = "select b.phase_code from t_opp_customer as a left join t_opp_cust_business_phase as b on a.id = b.cust_id where a.cust_name = \"%s\"" % parm
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()
        return result