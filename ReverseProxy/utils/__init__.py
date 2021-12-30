import logging
from env.proxy_config import LOGFILE_CONFIG

from .logger import BlasterLogger

# loggers initialisation
info_logger = BlasterLogger("info_logger", LOGFILE_CONFIG["info_logfilepath"])
warning_logger = BlasterLogger("warning_logger", LOGFILE_CONFIG["warning_logfilepath"] ,log_level=logging.ERROR)
error_logger = BlasterLogger("error_logger", LOGFILE_CONFIG["error_logfilepath"] ,log_level=logging.ERROR)
critical_logger = BlasterLogger("error_logger", LOGFILE_CONFIG["critical_logfilepath"] ,log_level=logging.ERROR)

def loginfo(msg : str)-> None:
    info_logger.logger.log(logging.INFO,msg)

def logerror(msg : str)-> None:
    error_logger.logger.log(logging.ERROR,msg,exc_info=True)

def logwarning(msg : str)-> None:
    warning_logger.logger.log(logging.WARNING,msg)

def logcritical(msg : str)-> None:
    critical_logger.logger.log(logging.CRITICAL,msg)
