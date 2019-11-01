import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from utils.config import Config, DRIVER_PATH, DATA_PATH
from utils.log import logger
from utils.file_reader import ExcelReader


class TestBaiDu(unittest.TestCase):
    URL = Config().get("URL")
    excel = DATA_PATH + "/baidu.xlsx"

    locator_kw = (By.ID, "kw")
    locator_su = (By.ID, "su")
    locator_result = (By.XPATH, '//*[@id="content_left"]')

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + "\chromedriver.exe")
        self.driver.get(self.URL)

    def tearDown(self):
        self.driver.quit()

    def test_search(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.driver.find_element(*self.locator_kw).send_keys(d["search"])
                self.driver.find_element(*self.locator_su).click()
                time.sleep(3)
                links = self.driver.find_elements(*self.locator_result)
                for link in links:
                    logger.info(link.text)


if __name__ == '__main__':
    unittest.main(verbosity=2)
