#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import xlwt

#打开浏览器，登录PC版crm
driver = webdriver.Firefox()
driver.get("https://oms-cloud.99bill.com/stage2/html/pc-crm/index.html#/login/")

#提示扫码登录
while True:
        try:
            if driver.find_element_by_link_text("请使用快Go App扫码登录"):
                print "请扫码登录..."
                time.sleep(1)

        except NoSuchElementException:
            print "成功登录..."
            print driver.current_url
            break
