"""
Logging configuration and utilities.
로깅 설정 및 유틸리티.
"""
import logging
import sys
from typing import Optional

from config.constants import LOG_FORMAT, LOG_DATE_FORMAT


def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Setup and return a logger instance.
    로거 인스턴스를 설정하고 반환.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    logger.handlers = []
    
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    
    formatter = logging.Formatter(LOG_FORMAT, LOG_DATE_FORMAT)
    console_handler.setFormatter(formatter)
    
    logger.addHandler(console_handler)
    
    return logger


def get_logger(name: str) -> logging.Logger:
    """
    Get a logger instance for the given name.
    주어진 이름의 로거 인스턴스 가져오기.
    """
    return logging.getLogger(name)


class CustomFormatter(logging.Formatter):
    """
    Custom formatter for different log levels.
    다른 로그 레벨을 위한 커스텀 포맷터.
    """
    
    grey = "\x1b[38;21m"
    green = "\x1b[32;21m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    
    FORMATS = {
        logging.DEBUG: grey + LOG_FORMAT + reset,
        logging.INFO: green + LOG_FORMAT + reset,
        logging.WARNING: yellow + LOG_FORMAT + reset,
        logging.ERROR: red + LOG_FORMAT + reset,
        logging.CRITICAL: bold_red + LOG_FORMAT + reset
    }
    
    def format(self, record: logging.LogRecord) -> str:
        """Format the log record / 로그 레코드 포맷"""
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, LOG_DATE_FORMAT)
        return formatter.format(record)