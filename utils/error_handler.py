"""
Error handling utilities.
오류 처리 유틸리티.
"""
import functools
from typing import Callable, Any

from utils.logger import get_logger


def log_error(func: Callable) -> Callable:
    """
    REFACTORED: Decorator for consistent error logging
    일관된 오류 로깅을 위한 데코레이터
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        logger = get_logger(func.__module__)
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {e}")
            raise
    return wrapper