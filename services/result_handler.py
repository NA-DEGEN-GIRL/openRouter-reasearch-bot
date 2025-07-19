"""
Result handling service for file I/O operations.
파일 I/O 작업을 위한 결과 처리 서비스.
"""
from typing import Optional
from pathlib import Path
from datetime import datetime

from utils.logger import get_logger
from utils.error_handler import log_error


class ResultHandler:
    """
    REFACTORED: Handles all result saving operations
    모든 결과 저장 작업을 처리
    """
    
    def __init__(self):
        self.logger = get_logger(self.__class__.__name__)
    
    @log_error
    def save_final_result(self, project_dir: Path, model_nickname: str, content: str) -> None:
        """Save final result / 최종 결과 저장"""
        output_path = project_dir / f"final_{model_nickname}.md"
        self._write_file(output_path, content)
    
    @log_error
    def save_interim_result(self, project_dir: Path, prompt_id: int, model_nickname: str, content: str) -> None:
        """Save interim result / 중간 결과 저장"""
        output_path = project_dir / f"p{prompt_id}_{model_nickname}.md"
        self._write_file(output_path, content)
    
    @log_error
    def write_log_header(self, log_path: Path, prompt_id: int, prompt_name: str, loc_strings: dict) -> None:
        """Write prompt header to log / 로그에 프롬프트 헤더 작성"""
        divider = '=' * 20
        header = loc_strings["log_prompt_header"].format(
            divider=divider,
            prompt_id=prompt_id,
            prompt_name=prompt_name
        )
        self._append_file(log_path, header)
    
    @log_error
    def write_reasoning_header(self, log_path: Path, loc_strings: dict) -> None:
        """Write reasoning header to log / 로그에 추론 헤더 작성"""
        header = loc_strings["log_reasoning_header"]
        self._append_file(log_path, header)
    
    @log_error
    def append_to_log(self, log_path: Path, content: str) -> None:
        """Append content to log / 로그에 내용 추가"""
        self._append_file(log_path, content)
    
    @log_error
    def write_error_to_log(self, log_path: Path, error_message: str, loc_strings: dict) -> None:
        """Write error to log / 로그에 오류 작성"""
        error_header = loc_strings["log_error_header"].format(
            error_message=error_message
        )
        self._append_file(log_path, error_header)
    
    def _write_file(self, path: Path, content: str) -> None:
        """Write content to file with timestamp / 타임스탬프와 함께 파일에 내용 작성"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        path.write_text(f"{timestamp}\n{content}", encoding='utf-8')
        self.logger.debug(f"Saved result to {path}")
    
    def _append_file(self, path: Path, content: str) -> None:
        """Append content to file / 파일에 내용 추가"""
        with open(path, 'a', encoding='utf-8') as f:
            f.write(content)
            f.flush()