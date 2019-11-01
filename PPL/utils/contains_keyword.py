from utils.log import logger


class Contains:
    def contains(self, str, driver):
        if str in driver.page_source:
            print("页面存在元素 %r" % str)
            logger.info("页面存在元素 %r" % str)
        else:
            print("页面元素丢失 %r" % str)
            raise Exception("没有找到%" % str)
            logger.info("页面元素丢失 %r" % str)