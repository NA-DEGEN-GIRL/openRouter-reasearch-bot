"""
Data models using dataclasses.
데이터클래스를 사용한 데이터 모델.
"""
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from pathlib import Path


@dataclass
class Prompt:
    """
    Represents a single prompt from the prompt file.
    프롬프트 파일의 단일 프롬프트를 나타냄.
    """
    id: int
    name: str
    text: str
    use_reasoning: bool = False
    has_other_ai_info: bool = False
    img_files: List[str] = field(default_factory=list)
    pdf_files: List[str] = field(default_factory=list)
    code_files: List[str] = field(default_factory=list)
    doc_files: List[str] = field(default_factory=list)


@dataclass
class ModelInfo:
    """
    Information about an AI model.
    AI 모델에 대한 정보.
    """
    model_id: str
    nickname: str
    max_completion_tokens: Optional[int] = None
    
    def __post_init__(self) -> None:
        """Extract nickname from model_id / model_id에서 nickname 추출"""
        if not self.nickname:
            self.nickname = self.model_id.split('/')[-1]


@dataclass
class Message:
    """
    Represents a chat message.
    채팅 메시지를 나타냄.
    """
    role: str
    content: Any  # Can be string or list of content parts / 문자열 또는 콘텐츠 부분 리스트


@dataclass
class APIResponse:
    """
    Response from AI model API.
    AI 모델 API의 응답.
    """
    model_nickname: str
    response_text: Optional[str]
    user_content: Any
    error: Optional[Exception] = None