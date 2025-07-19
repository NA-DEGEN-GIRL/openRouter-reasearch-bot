"""
Data models using dataclasses.
데이터클래스를 사용한 데이터 모델.
"""
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from pathlib import Path
import json
import re


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
    content: Any


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


# REFACTORED: Added PromptResult for structured data pipeline
@dataclass
class PromptResult:
    """
    Result from a prompt execution with structured data support.
    구조화된 데이터를 지원하는 프롬프트 실행 결과.
    """
    model_nickname: str
    raw_text: str
    structured_data: Optional[Dict[str, Any]] = None
    error: Optional[Exception] = None
    
    @staticmethod
    def from_response(response: APIResponse) -> 'PromptResult':
        """Create PromptResult from APIResponse / APIResponse에서 PromptResult 생성"""
        if response.error or not response.response_text:
            return PromptResult(
                model_nickname=response.model_nickname,
                raw_text="",
                error=response.error
            )
        
        # REFACTORED: Enhanced JSON extraction from gemini-2.5-pro
        structured_data = None
        text = response.response_text
        
        json_match = re.search(r'```json\s*\n(.*?)\n```', text, re.DOTALL)
        if json_match:
            try:
                structured_data = json.loads(json_match.group(1))
            except json.JSONDecodeError:
                pass
        
        return PromptResult(
            model_nickname=response.model_nickname,
            raw_text=text,
            structured_data=structured_data
        )


# REFACTORED: Added ProjectContext for immutable configuration
@dataclass
class ProjectContext:
    """
    Immutable project execution context.
    불변 프로젝트 실행 컨텍스트.
    """
    project_name: str
    system_prompt: str
    output_dir: Path
    live_log_dir: Path
    context_optional: str = ''