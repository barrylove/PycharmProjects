import requests
import json
from bs4 import BeautifulSoup

url1 = "https://query.99bill.com/report/login.do"
url2 = "https://query.99bill.com/report/query/doQuery.do"
data = {"username":"rui.zhang.wb", "password":"Barry250"}
sql = "select sum(amt) from t_amon_order_" + tablenumber + "where status ='1'"
sentence = {"ds":"ate0102", "sql": "select sum(amt) from t_amon_order_001 where status ='1'"}
session=requests.session()
session.post(url1, data=data, verify=False)
result = session.post(url2, data=sentence, verify=False)
print(result.text)
soup = BeautifulSoup(result.text, "lxml")
number = soup.find("td",class_="resultCell")
print(number)
