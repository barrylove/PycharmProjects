import sys
sys.path.append('utils')
import paramunittest
import json
import unittest
import urllib.parse
import utils.Log
from utils.geturlParams import GeturlParams
from utils.readExcel import ReadExcel
from utils.configHttp import RunMain

geturlparams = GeturlParams()
url = geturlparams.get_Url()
readexcel = ReadExcel()
test_xls = readexcel.get_xls('TestCase_MerchantCancel.xlsx', 'Sheet1')
logs = utils.Log.logger

@paramunittest.parametrized(*test_xls)
class testmerchantcancel(unittest.TestCase):
    def setParameters(self, case_name, path, query, method, expect_result):
        """
        set params
        :param case_name:
        :param path
        :param query
        :param method
        :param expect_result
        :return:
        """
        self.case_name = str(case_name)
        self.path = str(path)
        print(self.path)
        self.query = str(query)
        self.method = str(method)
        self.expect_result = str(expect_result)

    def description(self):
        """
        test report description
        :return:
        """
        self.case_name

    def setUp(self):
        """
        :return:
        """
        print(self.case_name + "测试开始前准备")

    def test01case(self):
        self.checkResult()

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def checkResult(self):  # 断言
        """
        check test result
        :return:
        """
        url1 = "http://192.168.14.249:8089/mbp-cs/api/"
        data = {"header": {"appId": "bill99","bizCode": "accountOpen","requestId": "2017032516260005354535000","requestTime": "2017-03-25 16:26:00.011","version": "1.0"},"user":{"memberCode":"27000037700","phone":"15411111000","name":"段杰","identityCardId":"650103198911201316","realName":"true"},"data": {"bankName":"招商银行","cityCode":"420300","merchantName":"拉拉","provinceCode":"420000","settleCardNo":"4367480050497844","address":"湖北省十堰市"}}
        info = RunMain().run_main(self.method, url1, data)  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        if self.case_name == 'existmerchant':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(info['header']['rspCode'], self.expect_result)
            logs.info(r'返回结果 %s', info['header']['rspCode'])
            logs.info(r'期望结果 %s', self.expect_result)
            logs.info(r'期望结果 %s', self.expect_result)
        if self.case_name == 'error_settlmentcard':  # 同上
            self.assertEqual(info['rspCode'], -1)
        if self.case_name == 'login_null':  # 同上
            self.assertEqual(info['rspCode'], 10001)
