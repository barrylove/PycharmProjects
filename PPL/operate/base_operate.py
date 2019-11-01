# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from config.sysconfig import *
from utils.log import logger
import sys
import time

class BaseOperate():
    operate_driver = webdriver.Chrome()

    def __init__(self,driver):
        self.operate_driver = driver

    def find_element(self, *loc):
        try:
            self.operate_driver.find_element(By.ID)
        except Exception as e:
            logger.info(e)
