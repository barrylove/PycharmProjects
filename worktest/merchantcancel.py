import unittest
import requests
import re


#商户进件

#json主体
H5gatewayUrl = 'http://192.168.14.249:8089/mbp-cs/api/'
AccountOpenData = {
    'header':{
    "appId": "bill99",
    "bizCode": "accountOpen",
    "requestId": "2017032516260005354535000",
    "requestTime": "2017-03-25 16:26:00.011",
    "version": "1.0"
    },
    "data": {
    "bankName":"招商银行",
    "cityCode":"420300",
    "merchantName":"拉拉",
    "provinceCode":"420000",
    "settleCardNo":"6226090217889456",
 	"address":"湖北省十堰市"
    },
    'user':{
     "memberCode":"27000037700",
	  "phone":"15411111000",
	  "name":"段杰",
 	  "identityCardId":"650103198911201316",
	  "realName":"true"
    }

}

re = requests.post(H5gatewayUrl, None, AccountOpenData)
print(re.text)

#if __name__ == '__main__':
