import requests
from flask import Flask
import urllib3
from Login import login
from Search import searchamt
from GetResult import getresult
import SpellSql
def calamt(tradedate):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#登录链接
    loginurl = "https://query.99bill.com/report/login.do"
#登录信息
    login_data = {"username":"rui.zhang.wb", "password":"Barry250"}
#搜索链接
    searchurl = "https://query.99bill.com/report/query/doQuery.do"
#头文件
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"}
#日期
    tradedata = "2019-10-15"
#初始表名
    tablestart = 0
    totalamt = 0
#初始数据库名
    dbs = {
        "db1":"ate0101",
        "db2":"ate0102",
        "db3":"ate0201",
        "db4":"ate0202",
        "db5":"ate0301",
        "db6":"ate0302"
    }

#打开会话
    ss = requests.session()
    login(ss, loginurl, login_data, header)

#循环主体
    tablenum = 20
    start = 0
    for db in dbs:
        for j in range(tablenum):
            index = "{:0>3d}".format(start + j)
            sql_data = {
                "ds": dbs[db],
                "sql": SpellSql.sumtotalamt(index, tradedate)
            }
            res = searchamt(ss, searchurl, sql_data, header)
            amt = getresult(res)
            totalamt = float(totalamt) + float(amt)
            #print("表" + str(index) + "中是：" + str(amt) + "总数是:" + str(totalamt))
        start = start + tablenum

    ss.close()
    return totalamt
