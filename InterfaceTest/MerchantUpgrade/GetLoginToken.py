import requests
import re
def getlogintoken():
    loginurl = "https://ebd.99bill.com/coc-bill-api/1.0/members/password/login"
    login_data ={
        "idContent": "Ho6SJpWP9yG3jny6UT3n6A%253D%253D",
        "password": "kqVfRSs%252BQ52844PzHnVqmQ%253D%253D"
    }
    header = {
        "Content-Type": "application/json"
    }
    #获取到logintoken
    login_token = requests.post(loginurl, data=None, json=login_data, headers=header)
    token = re.search(r'\w+-\w+-\w+-\w+-\w+', login_token.text).group()
    return token
