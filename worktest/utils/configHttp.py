import requests
import json


class RunMain():
    def send_post(self, url, data):
        result = requests.post(url=url, json=data).json()  # 因为这里要封装post方法，所以这里的url和data值不能写死
        #res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return result

    def send_get(self, url, data):
        result = requests.get(url=url, params=data).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def run_main(self, method, url=None, data=None):  # 定义一个run_main函数，通过传过来的method来进行不同的get或post请求
        result = None
        if method == 'post':
            result = self.send_post(url, data)
        elif method == 'get':
            result = self.send_get(url, data)
        else:
            print("method值错误！！！")
        return result


if __name__ == '__main__':  # 通过写死参数，来验证我们写的请求是否正确
    jsondata = '"header": {"appId": "bill99","bizCode": "accountOpen","requestId": "2017032516260005354535000","requestTime": "2017-03-25 16:26:00.011","version": "1.0"}"user:{"memberCode":"27000037700","phone":"15411111000","name":"段杰","identityCardId":"650103198911201316","realName":"true"},"data": {"bankName":"招商银行","cityCode":"420300","merchantName":"拉拉","provinceCode":"420000","settleCardNo":"4367480050497844","address":"湖北省十堰市"}'
    result1 = RunMain().run_main('po1st', 'http://127.0.0.1:8888/login', {'name': 'xiaoming', 'pwd': '111'})
    result2 = RunMain().run_main('post', 'http://192.168.14.249:8089/mbp-cs/api/', jsondata.encode())
    print(result1)
    print(result2)
