import pymysql.cursors

#连接数据库
connection = pymysql.connect(host='192.168.64.6',
                             port=3350,
                             user='dcmall',
                             password='5sn8hbgxyvccpwlj',
                             db='dcmall',
                             charset='utf8'
                             )

# 使用cursor()方法获取操作游标
cursor = connection.cursor()

#查询语句
sql = ""

# 执行SQL语句
cursor.execute(sql)

# 获取所有记录列表
results = cursor.fetchall()


# 关闭数据库连接
connection.close()