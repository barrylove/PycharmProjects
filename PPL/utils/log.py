import os
import logging
from logging.handlers import TimedRotatingFileHandler

class Logger(object):
    def __init__(self, logger_name="PPL网页版测试"):
        self.BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
        self.LOG_PATH = os.path.join(self.BASE_PATH, 'log')
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
        self.log_file_name = "CRM_test.log"
        self.backup_count = 5
        #日志输出级别
        self.console_output_level = "DEBUG"
        self.file_output_level = "DEBUG"
        #日志输出格式
        pattern = "%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s"
        self.formatter = logging.Formatter(pattern)

    def get_logger(self):
        """在日志中添加日志句柄并返回，如果logger已有句柄，则直接返回"""
        if not self.logger.handlers:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)

            # 每天重新创建一个日志文件，最多保留backup_count份
            file_handler=TimedRotatingFileHandler(
                filename=os.path.join(self.LOG_PATH, self.log_file_name),
                when="D",
                interval=1,
                backupCount=self.backup_count,
                delay=True,
                encoding="utf-8"
            )
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
        return self.logger

logger = Logger().get_logger()
