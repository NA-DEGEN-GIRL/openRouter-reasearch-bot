"""
Configuration management class.
설정 관리 클래스.
"""
import os
from pathlib import Path
from typing import List, Optional
from dataclasses import dataclass, field
from dotenv import load_dotenv

from config.constants import *
from core.exceptions import ConfigurationError
from localization import STRINGS


@dataclass
class Config:
    """
    Central configuration management.
    중앙 설정 관리.
    """
    language: str
    prompt_filepath: Path
    enable_collaboration: bool = True
    pdf_engine: str = 'pdf-text'
    
    api_key: Optional[str] = field(default=None, init=False)
    ai_models: List[str] = field(default_factory=list, init=False)
    
    def __post_init__(self) -> None:
        """Initialize configuration / 데이터클래스 생성 후 설정 초기화"""
        self.load_environment()
        self.load_ai_models()
        self.validate()
    
    def load_environment(self) -> None:
        """Load environment variables / 환경 변수 로드"""
        load_dotenv()
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        
        if not self.api_key:
            raise ConfigurationError(
                self.get_strings()["error_no_api_key"]
            )
    
    def load_ai_models(self, filepath: str = AI_MODELS_FILE) -> None:
        """Load AI models from file / 파일에서 AI 모델 로드"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                models = [line.strip() 
                          for line in f 
                          if line.strip() and not line.strip().startswith('#')]
            
            if not models:
                raise ConfigurationError(
                    f"No models specified in '{filepath}'."
                )
            
            self.ai_models = models
            
        except FileNotFoundError:
            raise ConfigurationError(
                f"File not found at '{filepath}'."
            )
    
    def validate(self) -> None:
        """Validate configuration / 설정 검증"""
        if not self.prompt_filepath.exists():
            raise ConfigurationError(
                self.get_strings()["error_file_not_found"].format(
                    filepath=self.prompt_filepath
                )
            )
    
    def get_strings(self) -> dict:
        """Get localized strings / 지역화된 문자열 가져오기"""
        return STRINGS[self.language]