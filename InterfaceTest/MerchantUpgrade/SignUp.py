import requests
from GetLoginToken import getlogintoken

def signup():
    signurl = "https://ebd.99bill.com/cp-gateway/task/signIn"
    signdata = {}
    header = {
        "Content-Type": "application/json",
        "Authorization": str(getlogintoken())
    }
    print(header["Authorization"])
    re = requests.post(signurl, data=None, json=signdata, headers=header)
    print(re.text)

signup()