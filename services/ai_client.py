"""
AI model client for interacting with OpenRouter API.
OpenRouter API와 상호작용하는 AI 모델 클라이언트.
"""
from typing import List, Dict, Any, Optional
from pathlib import Path
from openai import AsyncOpenAI, APITimeoutError, APIConnectionError, APIStatusError
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type

from config.config import Config
from config.constants import *
from core.models import ModelInfo, Message, APIResponse
from core.exceptions import APIError
from utils.logger import get_logger


class AIModelClient:
    """
    Manages interaction with a specific AI model.
    특정 AI 모델과의 상호작용을 관리.
    """
    
    def __init__(self, config: Config, model_info: ModelInfo):
        """Initialize AI model client / AI 모델 클라이언트 초기화"""
        self.config = config
        self.model_info = model_info
        self.logger = get_logger(f"{self.__class__.__name__}.{model_info.nickname}")
        
        # Initialize Async OpenAI client / 비동기 OpenAI 클라이언트 초기화
        self.client = AsyncOpenAI(
            base_url=OPENROUTER_BASE_URL,
            api_key=config.api_key
        )
        
        # Conversation history / 대화 히스토리
        self.history: List[Message] = []
        
        # Determine max tokens / 최대 토큰 결정
        self.max_tokens = model_info.max_completion_tokens or DEFAULT_MAX_TOKENS
    
    async def get_response(
        self,
        content: Any,
        output_path: Path,
        live_log_path: Path,
        use_reasoning: bool = False
    ) -> APIResponse:
        """
        Get response from AI model and save to files.
        AI 모델로부터 응답을 받고 파일에 저장.
        """
        try:
            # Prepare messages / 메시지 준비
            messages = self._prepare_messages(content)
            
            # Prepare API parameters / API 파라미터 준비
            extra_body = {"plugins": [{"id": "web"}]}
            if use_reasoning:
                extra_body['reasoning'] = {}
            
            # Get streaming response / 스트리밍 응답 받기
            stream = await self._get_ai_response_stream(messages, extra_body)
            
            # Process and log response / 응답 처리 및 로깅
            full_response = await self._process_stream_response(
                stream, live_log_path, use_reasoning
            )
            
            # Save full response / 전체 응답 저장
            output_path.write_text(full_response, encoding='utf-8')
            
            # Update history / 히스토리 업데이트
            self._update_history(content, full_response)
            
            return APIResponse(
                model_nickname=self.model_info.nickname,
                response_text=full_response,
                user_content=content
            )
            
        except (APIStatusError, APIConnectionError, APITimeoutError) as e:
            self.logger.error(f"API Error getting response: {e}")
            
            # Log error to file / 파일에 오류 로깅
            with open(live_log_path, 'a', encoding='utf-8') as f:
                error_message = str(e)
                f.write(self.config.get_strings()["log_error_header"].format(
                    error_message=error_message
                ))
            
            return APIResponse(
                model_nickname=self.model_info.nickname,
                response_text=None,
                user_content=content,
                error=e
            )
        except Exception as e:
            self.logger.exception(f"Unexpected error getting response: {e}")
            
            # Log error to file / 파일에 오류 로깅
            with open(live_log_path, 'a', encoding='utf-8') as f:
                error_message = str(e)
                f.write(self.config.get_strings()["log_error_header"].format(
                    error_message=error_message
                ))
            
            return APIResponse(
                model_nickname=self.model_info.nickname,
                response_text=None,
                user_content=content,
                error=e
            )
    
    def _prepare_messages(self, content: Any) -> List[Dict[str, Any]]:
        """Prepare messages for API call / API 호출을 위한 메시지 준비"""
        messages = [{"role": "system", "content": self.config.system_prompt}]
        
        # Add trimmed history / 잘린 히스토리 추가
        history_messages = []
        for msg in self.history[-(TRIMMED_HISTORY_COUNT * 2):]:
            history_messages.append({
                "role": msg.role,
                "content": msg.content
            })
        messages.extend(history_messages)
        
        # Add current user message / 현재 사용자 메시지 추가
        messages.append({"role": "user", "content": content})
        
        return messages
    
    @retry(
        wait=wait_fixed(RETRY_WAIT_SECONDS),
        stop=stop_after_attempt(RETRY_ATTEMPTS),
        retry=retry_if_exception_type((APITimeoutError, APIConnectionError)),
        reraise=True
    )
    async def _get_ai_response_stream(self, messages: List[Dict[str, Any]], extra_body: Dict[str, Any]):
        """Get streaming response from API with retry / 재시도와 함께 API에서 스트리밍 응답 받기"""
        return await self.client.chat.completions.create(
            model=self.model_info.model_id,
            messages=messages,
            stream=True,
            timeout=API_TIMEOUT,
            max_tokens=self.max_tokens,
            extra_body=extra_body
        )
    
    async def _process_stream_response(self, stream: Any, live_log_path: Path, use_reasoning: bool) -> str:
        """Process streaming response and write to log / 스트리밍 응답 처리 및 로그 작성"""
        full_response = ""
        
        with open(live_log_path, 'a', encoding='utf-8') as log_file:
            # Write reasoning header if needed / 필요시 추론 헤더 작성
            if use_reasoning:
                log_file.write(self.config.get_strings()["log_reasoning_header"])
                log_file.flush()
            
            # Process stream chunks / 스트림 청크 처리
            async for chunk in stream:
                delta = chunk.choices[0].delta
                
                # Log reasoning content / 추론 콘텐츠 로깅
                if hasattr(delta, 'reasoning') and delta.reasoning:
                    log_file.write(delta.reasoning)
                    log_file.flush()
                
                # Log and collect content / 콘텐츠 로깅 및 수집
                if delta.content:
                    full_response += delta.content
                    log_file.write(delta.content)
                    log_file.flush()
        
        return full_response
    
    def _update_history(self, user_content: Any, assistant_response: str) -> None:
        """Update conversation history / 대화 히스토리 업데이트"""
        self.history.append(Message(role="user", content=user_content))
        self.history.append(Message(role="assistant", content=assistant_response))