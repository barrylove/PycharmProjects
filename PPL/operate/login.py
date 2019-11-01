from selenium import webdriver
import time
from utils.log import logger

class Login():
    def login(self, driver, URL):
        #判断扫码登录成功
        while True:
            if driver.current_url == URL:
                logger.info(u"登录成功...")

                break
            else:
                logger.info(u"请扫码登录...")
                time.sleep(5)

