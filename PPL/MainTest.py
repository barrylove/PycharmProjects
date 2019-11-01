#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver.
import time
from selenium.common.exceptions import NoSuchElementException
import unittest
from operate.login import Login
from utils.contains_keyword import Contains
from utils.databasereader import databaseReader


class MainCase(unittest.TestCase):
    prodmemourl = "https://oms-cloud.99bill.com/prod/html/pc-crm/index.html#/memo/memo-manage/memo-list"
    st2memourl = "https://oms-cloud.99bill.com/stage2/html/pc-crm/index.html#/memo/memo-manage/memo-list"
    loginurl = "https://oms-cloud.99bill.com/stage2/html/pc-crm/index.html#/login/"

    #setUpClass所有case的前置条件
    @classmethod
    def setUpClass(cls):
        # 打开浏览器，到达主页面
       # cls.maindriver = webdriver.Chrome("D:\Python\chromedriver.exe")
        cls.logindriver = webdriver.Chrome("D:\Python\chromedriver.exe")
        cls.containswords = Contains()
        cls.dbreader = databaseReader()
        cls.logindriver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.logindriver.close()

    def testLogin(self):
        self.logindriver.get(self.loginurl)
        loginer = Login()
        loginer.login(self.logindriver, self.st2memourl)

    def testWordsInPage(self):
        self.logindriver.get(self.prodmemourl)

        # 验证主页元素
        keywords = ["客户名称", "发布人", "模糊搜索", "请输入全名", "拜访日期", "发布日期", "开始日期", "结束日期", "今日", "近一周", "近一个月"]
        for word in keywords:
            self.containswords.contains(word, self.logindriver)
            time.sleep(1)
"""
    def testCreateMemo(self):
        self.maindriver.get(self.prodmemourl)

        #点击新建纪要
        self.maindriver.find_element_by_class_name("index__action-PWJfP").click()
        time.sleep(3)

        #点击选择选择日程
        self.maindriver.find_element_by_class_name("ant-btn-primary").click()
        time.sleep(3)

        #选择第一个日程
        self.customer = self.maindriver.find_element_by_class_name("indent-level-0")[0].text
        self.maindriver.find_elements_by_link_text("选择")[0].click()
        time.sleep(3)

        #验证客户名称
        self.cn = self.maindriver.find_elements_by_class_name("NewMemo__ipt-3K7rm")[0].get_attribute("value")
        self.assertEqual(self.customer, self.cn, msg="客户名称校验未通过")


        #验证商机阶段
        self.phase_act = self.maindriver.find_elements_by_class_name("NewMemo__ipt-3K7rm")[1].get_attribute("value")
        self.phase_exp = self.dbreader_phase(self.phase)
        self.assertEqual(self.phase_act, self.phase_exp, msg="客户名称校验未通过")

        #验证拜访时间
        #验证会议位置
        #验证拜访目的

        #添加客户联系人
        self.maindriver.find_elements_by_class_name("ant-btn-sm")[0].click()
        time.sleep(3)

        #选择第一页所有客户联系人,点击确定
        self.maindriver.find_element_by_class_name("ant-checkbox-input").click()
        time.sleep(3)
        self.maindriver.find_elements_by_tag_name("button")[-1].click()

        #添加快钱参会人
        self.maindriver.find_elements_by_class_name("ant-btn-sm")[1].click()
        self.maindriver.find_elements_by_class_name("kqJoiners__search-2pBgl").find_element_by_tag_name("input").sendkeys("张芮")
        self.maindriver.find_elements_by_class_name("kqJoiners__search-2pBgl").find_element_by_class_name("searchBtn-2GFOR").click()

        #填写沟通内容
        self.maindriver.find_elements_by_class_name("NewMemo__text-26UQy")[1].clear()
        self.maindriver.find_elements_by_class_name("NewMemo__text-26UQy")[1].sendkeys("CRM-PC版自动化测试-沟通内容")

        # 填写后续工作
        self.maindriver.find_elements_by_class_name("NewMemo__text-26UQy")[2].clear()
        self.maindriver.find_elements_by_class_name("NewMemo__text-26UQy")[2].sendkeys("CRM-PC版自动化测试-后续工作")

        # 填写其他补充
        self.maindriver.find_elements_by_class_name("NewMemo__text-26UQy")[3].clear()
        self.maindriver.find_elements_by_class_name("NewMemo__text-26UQy")[3].sendkeys("CRM-PC版自动化测试-其他补充")

        #点击提交
        self.maindriver.find_elements_by_class_name("NewMemo__fabu-wh0PY").click()
"""

if __name__ == "__main__":
    unittest.main(verbosity=2)
