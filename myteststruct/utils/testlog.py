import logging

logging.warning("warning:user/passwd is invalid")
logging.critical("critical: server is down")

logging.basicConfig(filename="acc.log", level=logging.INFO,
                    format="%(asctime)s %(message)s", datefmt="%m/%d/%Y %I:%M:%S %P")
logging.debug("This message should go to the log file?")
logging.info("So should this")
logging.warning("And this,too")

def logger(log_obj):
    logger = logging.getLogger(log_obj)
    logger.setLevel(logging.INFO)
    console_handle = logging.StreamHandler()
    log_file = "access.log"
    file_handle = logging.FileHandler(log_file)
    file_handle.setLevel(logging.WARNING)