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
        
        self.client = AsyncOpenAI(
            base_url=OPENROUTER_BASE_URL,
            api_key=config.api_key
        )
        
        self.history: List[Message] = []
        self.max_tokens = model_info.max_completion_tokens or DEFAULT_MAX_TOKENS
    
    # REFACTORED: Simplified to focus only on API interaction
    async def get_response(
        self,
        content: Any,
        use_reasoning: bool = False
    ) -> APIResponse:
        """Get response from AI model / AI 모델로부터 응답 받기"""
        try:
            messages = self._prepare_messages(content)
            extra_body = {"plugins": [{"id": "web"}]}
            if use_reasoning:
                extra_body['reasoning'] = {}
            
            stream = await self._get_ai_response_stream(messages, extra_body)
            full_response = await self._collect_stream_response(stream)
            
            self._update_history(content, full_response)
            
            return APIResponse(
                model_nickname=self.model_info.nickname,
                response_text=full_response,
                user_content=content
            )
            
        except (APIStatusError, APIConnectionError, APITimeoutError) as e:
            self.logger.error(f"API Error: {e}")
            return APIResponse(
                model_nickname=self.model_info.nickname,
                response_text=None,
                user_content=content,
                error=e
            )
        except Exception as e:
            self.logger.exception(f"Unexpected error: {e}")
            return APIResponse(
                model_nickname=self.model_info.nickname,
                response_text=None,
                user_content=content,
                error=e
            )
    
    def _prepare_messages(self, content: Any) -> List[Dict[str, Any]]:
        """Prepare messages for API call / API 호출을 위한 메시지 준비"""
        messages = [{"role": "system", "content": self.config.system_prompt}]
        
        history_messages = []
        for msg in self.history[-(TRIMMED_HISTORY_COUNT * 2):]:
            history_messages.append({
                "role": msg.role,
                "content": msg.content
            })
        messages.extend(history_messages)
        
        messages.append({"role": "user", "content": content})
        return messages
    
    @retry(
        wait=wait_fixed(RETRY_WAIT_SECONDS),
        stop=stop_after_attempt(RETRY_ATTEMPTS),
        retry=retry_if_exception_type((APITimeoutError, APIConnectionError)),
        reraise=True
    )
    async def _get_ai_response_stream(self, messages: List[Dict[str, Any]], extra_body: Dict[str, Any]):
        """Get streaming response with retry / 재시도와 함께 스트리밍 응답 받기"""
        return await self.client.chat.completions.create(
            model=self.model_info.model_id,
            messages=messages,
            stream=True,
            timeout=API_TIMEOUT,
            max_tokens=self.max_tokens,
            extra_body=extra_body
        )
    
    # REFACTORED: Separated from logging concerns
    async def _collect_stream_response(self, stream: Any) -> str:
        """Collect full response from stream / 스트림에서 전체 응답 수집"""
        full_response = ""
        reasoning_text = ""
        
        async for chunk in stream:
            delta = chunk.choices[0].delta
            
            if hasattr(delta, 'reasoning') and delta.reasoning:
                reasoning_text += delta.reasoning
                
            if delta.content:
                full_response += delta.content
        
        self._last_reasoning = reasoning_text
        return full_response
    
    def _update_history(self, user_content: Any, assistant_response: str) -> None:
        """Update conversation history / 대화 히스토리 업데이트"""
        self.history.append(Message(role="user", content=user_content))
        self.history.append(Message(role="assistant", content=assistant_response))
    
    def get_last_reasoning(self) -> str:
        """Get last reasoning text / 마지막 추론 텍스트 가져오기"""
        return getattr(self, '_last_reasoning', '')