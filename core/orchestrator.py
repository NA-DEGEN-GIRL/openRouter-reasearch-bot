"""
Main project orchestrator that controls the execution flow.
실행 흐름을 제어하는 메인 프로젝트 오케스트레이터.
"""
import os
import re
import json
import shutil
import asyncio
from typing import List, Dict, Optional
from pathlib import Path

from config.config import Config
from config.constants import *
from core.models import Prompt, APIResponse, ModelInfo, ProjectContext, PromptResult
from core.exceptions import ProjectError
from services.ai_client import AIModelClient
from services.file_handler import FileHandler
from services.prompt_parser import PromptParser
from services.model_provider import ModelDataProvider
from services.result_handler import ResultHandler
from utils.logger import get_logger
from utils.error_handler import log_error


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
        
        self.file_handler = FileHandler()
        self.prompt_parser = PromptParser()
        self.model_provider = ModelDataProvider()
        self.result_handler = ResultHandler()
        
        self.ai_clients: Dict[str, AIModelClient] = {}
        self.prompts: List[Prompt] = []
        self.last_turn_responses: Dict[str, PromptResult] = {}
        self.context: Optional[ProjectContext] = None
    
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
    
    @log_error
    async def _initialize_project(self) -> None:
        """Initialize project from prompt file / 프롬프트 파일에서 프로젝트 초기화"""
        self.logger.info("Initializing project from prompt file")

        project_name, context_optional, system_prompt, prompts = self.prompt_parser.parse(
            self.config.prompt_filepath,
            self.loc_strings
        )
        
        # REFACTORED: Create immutable ProjectContext
        folder_name = re.sub(r'[^\w-]', '_', project_name).lower()
        output_dir = Path(OUTPUT_DIR_PREFIX) / folder_name
        live_log_dir = output_dir / LIVE_LOG_DIR_NAME
        
        self.context = ProjectContext(
            project_name=project_name,
            system_prompt=system_prompt,
            output_dir=output_dir,
            live_log_dir=live_log_dir,
            context_optional=context_optional
        )
        
        self.prompts = prompts
    
    def _setup_output_directories(self) -> None:
        """Setup output directories / 출력 디렉토리 설정"""
        self.logger.info(f"Setting up output directories at {self.context.output_dir}")
        
        if self.context.live_log_dir.exists():
            shutil.rmtree(self.context.live_log_dir)
        self.context.live_log_dir.mkdir(parents=True, exist_ok=True)
        self.context.output_dir.mkdir(parents=True, exist_ok=True)
    
    async def _initialize_ai_clients(self) -> None:
        """Initialize AI model clients / AI 모델 클라이언트 초기화"""
        self.logger.info("Initializing AI model clients")
        
        model_data = await self.model_provider.get_model_data(self.loc_strings)
        
        for model_id in self.config.ai_models:
            model_info = ModelInfo(
                model_id=model_id,
                nickname=model_id.split('/')[-1],
                max_completion_tokens=model_data.get(model_id, {}).get('max_completion_tokens')
            )
            
            # REFACTORED: Pass system_prompt through modified Config
            modified_config = Config(
                language=self.config.language,
                prompt_filepath=self.config.prompt_filepath,
                enable_collaboration=self.config.enable_collaboration,
                pdf_engine=self.config.pdf_engine
            )
            modified_config.api_key = self.config.api_key
            modified_config.ai_models = self.config.ai_models
            modified_config.system_prompt = self.context.system_prompt
            
            client = AIModelClient(
                config=modified_config,
                model_info=model_info
            )
            self.ai_clients[model_info.nickname] = client
    
    def _print_startup_info(self) -> None:
        """Print startup information / 시작 정보 출력"""
        print(self._divider())
        print(self.loc_strings["research_start"].format(project_name=self.context.project_name))
        print(self.loc_strings["output_folder_info"].format(output_dir=self.context.output_dir))
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
    
    # REFACTORED: Simplified by delegating file I/O
    async def _execute_single_prompt(self, prompt: Prompt, index: int) -> None:
        """Execute a single prompt / 단일 프롬프트 실행"""
        is_last_prompt = (index == len(self.prompts) - 1)
        
        print(f"\n\n")
        print(self._divider(char=PROMPT_DIVIDER_CHAR))
        print(self.loc_strings["prompt_execution"].format(
            prompt_id=prompt.id,
            total_prompts=len(self.prompts),
            prompt_name=prompt.name
        ))
        
        if prompt.use_reasoning:
            print(self.loc_strings["reasoning_activated"])
        
        print(self.loc_strings["request_start"].format(num_models=len(self.ai_clients)))
        
        current_responses = await self._execute_prompt_parallel(prompt, index, is_last_prompt)
        
        if current_responses:
            self.last_turn_responses = current_responses
        
        print(self.loc_strings["prompt_finished"].format(prompt_id=prompt.id))
    
    # REFACTORED: Reduced complexity and separated concerns
    async def _execute_prompt_parallel(self, prompt: Prompt, index: int, is_last: bool) -> Dict[str, PromptResult]:
        """Execute prompt for all models in parallel / 모든 모델에 대해 병렬로 프롬프트 실행"""
        current_responses = {}
        
        tasks = []
        for nickname, client in self.ai_clients.items():
            task = self._create_model_task(nickname, client, prompt, index, is_last)
            tasks.append(task)
        
        responses = await asyncio.gather(*tasks, return_exceptions=True)
        
        for (nickname, client), response in zip(self.ai_clients.items(), responses):
            if isinstance(response, PromptResult):
                if response.raw_text:
                    print(self.loc_strings["task_completed"].format(nick=nickname))
                    current_responses[nickname] = response
                else:
                    print(self.loc_strings["task_failed"].format(nick=nickname))
            elif isinstance(response, Exception):
                self.logger.error(f"Task error for {nickname}: {response}")
                print(self.loc_strings["task_error"].format(
                    model_nickname=nickname,
                    e=response
                ))
        
        return current_responses
    
    async def _create_model_task(self, nickname: str, client: AIModelClient, prompt: Prompt, index: int, is_last: bool) -> PromptResult:
        """Create task for single model / 단일 모델을 위한 작업 생성"""
        try:
            user_content = self._prepare_user_content(prompt, index, nickname)
            
            content = self.file_handler.make_message_content(
                prompt_text=user_content,
                img_files=prompt.img_files,
                pdf_files=prompt.pdf_files,
                code_files=prompt.code_files,
                doc_files=prompt.doc_files
            )
            
            live_log_path = self.context.live_log_dir / f"{nickname}.log"
            self.result_handler.write_log_header(
                live_log_path, prompt.id, prompt.name, self.loc_strings
            )
            
            if prompt.use_reasoning:
                self.result_handler.write_reasoning_header(live_log_path, self.loc_strings)
            
            response = await client.get_response(content, prompt.use_reasoning)
            
            if response.error:
                self.result_handler.write_error_to_log(
                    live_log_path, str(response.error), self.loc_strings
                )
                return PromptResult(
                    model_nickname=nickname,
                    raw_text="",
                    error=response.error
                )
            
            if prompt.use_reasoning:
                reasoning = client.get_last_reasoning()
                if reasoning:
                    self.result_handler.append_to_log(live_log_path, reasoning)
            
            self.result_handler.append_to_log(live_log_path, response.response_text)
            
            if is_last:
                self.result_handler.save_final_result(
                    self.context.output_dir, nickname, response.response_text
                )
            else:
                self.result_handler.save_interim_result(
                    self.context.output_dir, prompt.id, nickname, response.response_text
                )
            
            return PromptResult.from_response(response)
            
        except Exception as e:
            self.logger.error(f"Error in task for {nickname}: {e}")
            return PromptResult(
                model_nickname=nickname,
                raw_text="",
                error=e
            )
    
    # REFACTORED: Support structured data in collaboration
    def _prepare_user_content(self, prompt: Prompt, index: int, model_nickname: str) -> str:
        """Prepare user content / 사용자 콘텐츠 준비"""
        if index == 0:
            if self.context.context_optional:
                return f"## context ##\n{self.context.context_optional}\n## end of context ##{prompt.text}"
            else:
                return prompt.text
        
        if not self.config.enable_collaboration or not prompt.has_other_ai_info:
            return prompt.text
        
        other_responses = []
        for nick, result in self.last_turn_responses.items():
            if nick != model_nickname:
                if result.structured_data:
                    response_text = f"--- RESPONSE FROM {nick} (STRUCTURED) ---\n"
                    response_text += json.dumps(result.structured_data, ensure_ascii=False, indent=2)
                    response_text += "\n"
                else:
                    response_text = f"--- RESPONSE FROM {nick} ---\n{result.raw_text}\n"
                other_responses.append(response_text)
        
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
    
    def _divider(self, char: str = DIVIDER_CHAR, length: int = DIVIDER_LENGTH) -> str:
        """Create a divider line / 구분선 생성"""
        return char * length