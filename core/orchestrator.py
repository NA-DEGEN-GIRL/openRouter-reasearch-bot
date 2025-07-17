"""
Main project orchestrator that controls the execution flow.
실행 흐름을 제어하는 메인 프로젝트 오케스트레이터.
"""
import os
import shutil
import asyncio
from typing import List, Dict, Optional
from pathlib import Path

from config.config import Config
from config.constants import *
from core.models import Prompt, APIResponse, ModelInfo
from core.exceptions import ProjectError
from services.ai_client import AIModelClient
from services.file_handler import FileHandler
from services.prompt_parser import PromptParser
from services.model_provider import ModelDataProvider
from utils.logger import get_logger


class ProjectOrchestrator:
    """
    Orchestrates the entire project execution.
    전체 프로젝트 실행을 오케스트레이션.
    """
    
    def __init__(self, config: Config):
        """Initialize orchestrator / 오케스트레이터 초기화"""
        self.config = config
        self.logger = get_logger(self.__class__.__name__)
        self.loc_strings = config.get_strings()
        
        # Initialize services / 서비스 초기화
        self.file_handler = FileHandler()
        self.prompt_parser = PromptParser()
        self.model_provider = ModelDataProvider()
        
        # Initialize state / 상태 초기화
        self.ai_clients: Dict[str, AIModelClient] = {}
        self.prompts: List[Prompt] = []
        self.last_turn_responses: Dict[str, str] = {}
        self.context_optional: str = ''
    
    async def run(self) -> None:
        """Main execution method / 메인 실행 메서드"""
        try:
            await self._initialize_project()
            self._setup_output_directories()
            await self._initialize_ai_clients()
            self._print_startup_info()
            await self._execute_prompts()
            self._print_completion_info()
            
        except Exception as e:
            self.logger.error(f"Project execution failed: {e}")
            raise ProjectError(f"Project execution failed: {e}")
    
    async def _initialize_project(self) -> None:
        """Initialize project from prompt file / 프롬프트 파일에서 프로젝트 초기화"""
        self.logger.info("Initializing project from prompt file")
        
        project_name, context_optional, system_prompt, prompts = self.prompt_parser.parse(
            self.config.prompt_filepath,
            self.loc_strings
        )
        
        self.config.set_project_info(project_name, system_prompt)
        self.prompts = prompts
        self.context_optional = context_optional
    
    def _setup_output_directories(self) -> None:
        """Setup output directories / 출력 디렉토리 설정"""
        self.logger.info(f"Setting up output directories at {self.config.output_dir}")
        
        # Clean and create live log directory / 라이브 로그 디렉토리 정리 및 생성
        if self.config.live_log_dir.exists():
            shutil.rmtree(self.config.live_log_dir)
        self.config.live_log_dir.mkdir(parents=True, exist_ok=True)
        self.config.output_dir.mkdir(parents=True, exist_ok=True)
    
    async def _initialize_ai_clients(self) -> None:
        """Initialize AI model clients / AI 모델 클라이언트 초기화"""
        self.logger.info("Initializing AI model clients")
        
        # Fetch model data / 모델 데이터 가져오기
        model_data = await self.model_provider.get_model_data(self.loc_strings)
        
        # Create clients for each model / 각 모델에 대한 클라이언트 생성
        for model_id in self.config.ai_models:
            model_info = ModelInfo(
                model_id=model_id,
                nickname=model_id.split('/')[-1],
                max_completion_tokens=model_data.get(model_id, {}).get('max_completion_tokens')
            )
            
            client = AIModelClient(
                config=self.config,
                model_info=model_info
            )
            self.ai_clients[model_info.nickname] = client
    
    def _print_startup_info(self) -> None:
        """Print startup information / 시작 정보 출력"""
        print(self._divider())
        print(self.loc_strings["research_start"].format(project_name=self.config.project_name))
        print(self.loc_strings["output_folder_info"].format(output_dir=self.config.output_dir))
        print(self.loc_strings["live_log_info"])
        print(self.loc_strings["models_in_use"].format(
            models_list=', '.join(self.ai_clients.keys())
        ))
        if not self.config.enable_collaboration:
            print(self.loc_strings["collaboration_disabled"])
        print(self._divider())
    
    async def _execute_prompts(self) -> None:
        """Execute all prompts / 모든 프롬프트 실행"""
        for i, prompt in enumerate(self.prompts):
            await self._execute_single_prompt(prompt, i)
    
    async def _execute_single_prompt(self, prompt: Prompt, index: int) -> None:
        """Execute a single prompt / 단일 프롬프트 실행"""
        is_last_prompt = (index == len(self.prompts) - 1)
        
        # Print prompt header / 프롬프트 헤더 출력
        print(f"\n\n")
        print(self._divider(char="*"))
        print(self.loc_strings["prompt_execution"].format(
            prompt_id=prompt.id,
            total_prompts=len(self.prompts),
            prompt_name=prompt.name
        ))
        
        if prompt.use_reasoning:
            print(self.loc_strings["reasoning_activated"])
        
        print(self.loc_strings["request_start"].format(num_models=len(self.ai_clients)))
        
        # Execute prompt for all models / 모든 모델에 대해 프롬프트 실행
        current_responses = await self._execute_prompt_parallel(prompt, index, is_last_prompt)
        
        # Update last turn responses / 마지막 턴 응답 업데이트
        if current_responses:
            self.last_turn_responses = current_responses
        
        print(self.loc_strings["prompt_finished"].format(prompt_id=prompt.id))
    
    async def _execute_prompt_parallel(self, prompt: Prompt, index: int, is_last: bool) -> Dict[str, str]:
        """Execute prompt for all models in parallel / 모든 모델에 대해 병렬로 프롬프트 실행"""
        current_responses = {}
        
        # Prepare tasks / 작업 준비
        tasks = []
        for nickname, client in self.ai_clients.items():
            # Prepare user content / 사용자 콘텐츠 준비
            user_content = self._prepare_user_content(prompt, index, nickname)
            
            # Prepare file attachments / 파일 첨부 준비
            content = self.file_handler.make_message_content(
                prompt_text=user_content,
                img_files=prompt.img_files,
                pdf_files=prompt.pdf_files,
                code_files=prompt.code_files,
                doc_files=prompt.doc_files
            )
            
            # Prepare output paths / 출력 경로 준비
            filename_prefix = "final" if is_last else f"p{prompt.id}"
            output_path = self.config.output_dir / f"{filename_prefix}_{nickname}.md"
            live_log_path = self.config.live_log_dir / f"{nickname}.log"
            
            # Write prompt header to log / 로그에 프롬프트 헤더 작성
            with open(live_log_path, 'a', encoding='utf-8') as f:
                divider = '=' * 20
                f.write(self.loc_strings["log_prompt_header"].format(
                    divider=divider,
                    prompt_id=prompt.id,
                    prompt_name=prompt.name
                ))
            
            # Create task / 작업 생성
            task = client.get_response(
                content=content,
                output_path=output_path,
                live_log_path=live_log_path,
                use_reasoning=prompt.use_reasoning
            )
            tasks.append(task)
        
        # Execute all tasks concurrently / 모든 작업 동시 실행
        responses = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Process responses / 응답 처리
        for (nickname, client), response in zip(self.ai_clients.items(), responses):
            if isinstance(response, Exception):
                self.logger.error(f"Task error for {nickname}: {response}")
                print(self.loc_strings["task_error"].format(
                    model_nickname=nickname,
                    e=response
                ))
            elif isinstance(response, APIResponse):
                if response.response_text:
                    print(self.loc_strings["task_completed"].format(nick=nickname))
                    current_responses[nickname] = response.response_text
                else:
                    print(self.loc_strings["task_failed"].format(nick=nickname))
        
        return current_responses
    
    def _prepare_user_content(self, prompt: Prompt, index: int, model_nickname: str) -> str:
        """Prepare user content based on collaboration settings / 협업 설정에 따라 사용자 콘텐츠 준비"""
        if index == 0:
            if self.context_optional != '':
                return f"## context ##\n{self.context_optional}\n## end of context ##{prompt.text}"
            else:
                return prompt.text
        
        if not self.config.enable_collaboration or not prompt.has_other_ai_info:
            return prompt.text
        
        # Include other AI responses / 다른 AI 응답 포함
        other_responses = [
            f"--- RESPONSE FROM {nick} ---\n{resp}\n"
            for nick, resp in self.last_turn_responses.items()
            if nick != model_nickname
        ]
        
        return (
            f"## PREVIOUS RESPONSES FROM OTHER AIs ##\n"
            f"{''.join(other_responses)}\n\n"
            f"## CURRENT REQUEST ##\n"
            f"{prompt.text}"
        )
    
    def _print_completion_info(self) -> None:
        """Print completion information / 완료 정보 출력"""
        print(self._divider())
        print(self.loc_strings["all_finished"])
        print(self._divider())
    
    def _divider(self, char: str = "=", length: int = 80) -> str:
        """Create a divider line / 구분선 생성"""
        return char * length