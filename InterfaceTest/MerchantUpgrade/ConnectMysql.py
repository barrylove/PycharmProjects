import pymysql

def connectmysql(DBConfig): #返回传入数据库的游标

#建立数据库链接
    mysqldb = pymysql.connect(
        host= DBConfig["host"],
        port= DBConfig["port"],
        user= DBConfig["user"],
        passwd= DBConfig["password"],
        db= DBConfig["db"],
        charset= DBConfig["charset"]
    )
    cursor = mysqldb.cursor()
    return cursor
"""
    cursor = mysqldb.cursor()
    cursor.execute("select id, device_type, brand, org_id, source_org from t_coral_device where sn = 'Q0NL15143721'")
    cursor.close()
    mysqldb.close()"""