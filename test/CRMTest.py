#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import datetime
from selenium.common.exceptions import NoSuchElementException
import unittest

class MainCase(unittest.TestCase):
    #打开浏览器，登录PC版crm

    def setUp(self):
        # 打开浏览器，登录PC版crm
        driver = webdriver.Chrome("D:\Python\chromedriver.exe")
        driver.get("https://oms-cloud.99bill.com/stage2/html/pc-crm/index.html#/login/")
        #扫码登录
        while True:
            if driver.current_url == "https://oms-cloud.99bill.com/stage2/html/pc-crm/index.html#/login/":
                print ("请扫码登录...")
                time.sleep(5)
            else:
                print ("成功登录...")
                print (driver.current_url)
                break

    def createnewmemo(self):
        #新建纪要
        self.driver.find_element_by_class_name("index__action-PWJfP").click()
        time.sleep(3)

        #点击选择选择日程
        self.driver.find_element_by_class_name("ant-btn-primary").click()
        time.sleep(3)

        #选择第一个日程
        self.driver.find_elements_by_link_text("选择")[0].click()
        time.sleep(3)

        #添加客户联系人
        self.driver.find_element_by_class_name("ant-btn-sm").click()
        time.sleep(3)

        #选择第一页所有客户联系人,点击确定
        self.driver.find_element_by_class_name("ant-checkbox-input").click()
        time.sleep(3)
        self.driver.find_elements_by_tag_name("button")[-1].click()

    def teardown(self):
        self.driver.close()