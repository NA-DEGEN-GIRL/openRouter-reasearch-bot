2025-07-18 10:15:02
알겠습니다. 전문 개발자로서 수립된 마스터 플랜에 따라 AI-Forge 프로젝트의 리팩토링을 시작하겠습니다. 모든 변경 사항은 추적이 가능하도록 독립적으로 구현하고, 계획에 명시된 대로 안정성과 가독성을 최우선으로 고려하겠습니다.

---

### 1. 최종 파일 구조 (tree 형식)

마스터 플랜에 따라 클래스를 재분배하고 책임을 명확히 한 최종 파일 구조입니다.

```
.
├── config
│   ├── config.py
│   └── constants.py
├── core
│   ├── context.py
│   ├── engine.py
│   ├── exceptions.py
│   └── models.py
├── projects/
├── prompts
│   └── research.md
├── services
│   ├── ai_client.py
│   ├── file_handler.py
│   ├── model_provider.py
│   ├── prompt_parser.py
│   └── result_handler.py
├── utils
│   └── logger.py
├── .env.example
├── ai_models.txt
├── localization.py
├── main.py
├── README.md
└── requirements.txt
```

---

### 2. 전체 리팩토링된 코드

[File: ./main.py]
```python
#!/usr/bin/env python3
"""
Main entry point for the AI-Forge.
AI-Forge의 메인 진입점.
"""
import sys
import asyncio
import argparse
from pathlib import Path

from config.config import Config
from core.engine import WorkflowEngine
from core.exceptions import ProjectError
from utils.logger import setup_logger
from localization import STRINGS

# REFACTORED: Argument parsing logic is self-contained. / 인자 파싱 로직을 자체 포함하도록 변경.
def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments / 명령줄 인자를 파싱"""
    parser = argparse.ArgumentParser(
        description="AI-Forge: An automated project research bot using AI models."
    )
    parser.add_argument(
        '--lang', '-l',
        type=str,
        choices=['ko', 'en'],
        help="Select language (ko/en). If not specified, an interactive prompt will be shown."
    )
    parser.add_argument(
        '--prompt', '-p',
        type=str,
        help="Specify a custom prompt file inside the 'prompts/' directory."
    )
    return parser.parse_args()

# REFACTORED: User interaction logic is grouped together. / 사용자 상호작용 로직을 그룹화.
def select_language() -> str:
    """Interactive language selection / 대화형 언어 선택"""
    while True:
        choice = input(STRINGS['en']["select_language"])
        if choice == '1': return 'ko'
        if choice == '2': return 'en'
        print(STRINGS['en']["invalid_input"])

def select_prompt_file(lang: str) -> Path:
    """Interactive prompt file selection / 대화형 프롬프트 파일 선택"""
    loc_strings = STRINGS[lang]
    print(loc_strings["select_bot"])
    print(f"  {loc_strings['bot_option_research']}")
    print(f"  {loc_strings['bot_option_custom']}")
    
    while True:
        choice = input(f"\n번호를 입력하세요 (1-2): ")
        if choice == '1':
            filename = 'research_en.md' if lang == 'en' else 'research.md'
            return Path('prompts') / filename
        if choice == '2':
            filename = input(loc_strings['enter_prompt_filename'])
            return Path('prompts') / filename
        print(loc_strings["invalid_input"])

async def main() -> None:
    """Main execution function / 메인 실행 함수"""
    args = parse_arguments()
    logger = setup_logger('ai_forge')
    
    try:
        lang = args.lang or select_language()
        prompt_filepath = Path('prompts') / args.prompt if args.prompt else select_prompt_file(lang)
        
        print(f"Language: {lang.upper()} | Prompt: {prompt_filepath}")
        
        # REFACTORED: Decoupled Config and Engine. Main is now a simple launcher.
        # Config와 Engine을 분리. Main은 이제 간단한 실행기 역할.
        config = Config(language=lang, prompt_filepath=prompt_filepath)
        engine = WorkflowEngine(config)
        await engine.run()
        
    except ProjectError as e:
        logger.error(f"A known error occurred: {e}")
        print(f"Error: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        logger.info("Execution interrupted by user.")
        print("\n실행이 중단되었습니다.")
        sys.exit(0)
    except Exception as e:
        logger.exception("An unexpected error occurred.")
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
```
[File: ./localization.py]
```python
# No changes. The file adheres to SRP.
# 변경 없음. 파일이 단일 책임 원칙을 잘 준수하고 있음.
STRINGS = {
    'en': {
        "select_language": "Select language (1: Korean, 2: English): ",
        "invalid_input": "Invalid input. Please try again.",
        "select_bot": "# Select bot mode #",
        "bot_option_research": "1) Standard research bot",
        "bot_option_custom": "2) Custom prompt",
        "enter_prompt_filename": "Enter prompt filename (under ./prompts): ",
        "mode_selected": "Language: {lang_upper} | Prompt: {prompt_filepath}",
        "error_no_api_key": "[Error] OPENROUTER_API_KEY not found in environment variables.",
        "fetching_models": "Fetching model metadata from OpenRouter...",
        "fetching_models_failed": "Failed to fetch model list",
        "error_file_not_found": "[Error] File not found: {filepath}",
        "error_no_headers": "[Error] No headers found in: {filepath}",
        "error_no_project_name": "[Error] No 'project name' section in prompt file.",
        "error_no_system_prompt": "[Error] No 'system prompt' section.",
        "research_start": "### Research started for: {project_name} ###",
        "output_folder_info": "Outputs will be saved in: {output_dir}",
        "live_log_info": "Live logs will be recorded.",
        "models_in_use": "Models: {models_list}",
        "collaboration_disabled": "[COLLABORATION DISABLED]",
        "prompt_execution": "[Prompt {prompt_id}/{total_prompts}] Executing: {prompt_name}",
        "reasoning_activated": "(Reasoning mode ON)",
        "request_start": "{num_models} models: Running requests...",
        "task_completed": "Response complete for: {nick}",
        "task_failed": "FAILED: No response: {nick}",
        "task_error": "[ERROR] {model_nickname}: {e}",
        "prompt_finished": "-- Prompt {prompt_id} finished. --",
        "all_finished": "# All prompts processed. #",
        "log_reasoning_header": "\n## REASONING MODE LOG ##\n",
        "log_prompt_header": "\n{divider} Prompt {prompt_id}: {prompt_name} {divider}\n",
        "log_error_message": ">>> Error occurred: {e}\n",
        "log_error_header": "\n## ERROR OCCURRED ##\n{error_message}\n",
    },
    'ko': {
        "select_language": "언어를 선택하세요 (1: 한글, 2: 영어): ",
        "invalid_input": "잘못된 입력입니다. 다시 시도해주세요.",
        "select_bot": "# 봇 모드 선택 #",
        "bot_option_research": "1) 표준 리서치 봇",
        "bot_option_custom": "2) 커스텀 프롬프트",
        "enter_prompt_filename": "프롬프트 파일명을 입력하세요 (./prompts 하위): ",
        "mode_selected": "언어: {lang_upper} | 프롬프트: {prompt_filepath}",
        "error_no_api_key": "[오류] 환경 변수에서 OPENROUTER_API_KEY를 찾을 수 없습니다.",
        "fetching_models": "OpenRouter로부터 모델 메타데이터를 불러오는 중...",
        "fetching_models_failed": "모델 목록 불러오기 실패",
        "error_file_not_found": "[오류] 파일 없음: {filepath}",
        "error_no_headers": "[오류] 헤더가 없는 프롬프트 파일: {filepath}",
        "error_no_project_name": "[오류] 프롬프트 파일에 'project name' 섹션이 없습니다.",
        "error_no_system_prompt": "[오류] 'system prompt' 섹션이 없습니다.",
        "research_start": "### 프로젝트 리서치 시작: {project_name} ###",
        "output_folder_info": "출력물 폴더: {output_dir}",
        "live_log_info": "실시간 로그가 기록됩니다.",
        "models_in_use": "사용 모델: {models_list}",
        "collaboration_disabled": "[협업 비활성화]",
        "prompt_execution": "[프롬프트 {prompt_id}/{total_prompts}] 실행 중: {prompt_name}",
        "reasoning_activated": "(추론 모드 활성화)",
        "request_start": "{num_models}개 모델: 요청 실행 중...",
        "task_completed": "응답 완료: {nick}",
        "task_failed": "실패: 응답 없음: {nick}",
        "task_error": "[오류] {model_nickname}: {e}",
        "prompt_finished": "-- 프롬프트 {prompt_id} 완료 --",
        "all_finished": "# 모든 프롬프트 처리 완료 #",
        "log_reasoning_header": "\n## 추론 모드 로그 ##\n",
        "log_prompt_header": "\n{divider} 프롬프트 {prompt_id}: {prompt_name} {divider}\n",
        "log_error_message": ">>> 오류 발생: {e}\n",
        "log_error_header": "\n## 오류 발생 ##\n{error_message}\n",
    }
}
```
[File: ./config/config.py]
```python
"""
Configuration management class.
설정 관리 클래스.
"""
import os
from pathlib import Path
from typing import List, Optional
from dataclasses import dataclass, field
from dotenv import load_dotenv

from core.exceptions import ConfigurationError
from localization import STRINGS
from .constants import AI_MODELS_FILE

@dataclass(frozen=True)
class Config:
    """
    Central, immutable configuration management.
    중앙의, 불변하는 설정 관리 클래스.
    """
    language: str
    prompt_filepath: Path
    enable_collaboration: bool = True
    
    # REFACTORED: Made Config immutable (frozen=True) and removed runtime state.
    # Config를 불변 객체로 만들고 런타임 상태 변수를 제거.
    api_key: str = field(init=False)
    ai_models: List[str] = field(init=False)
    
    def __post_init__(self):
        # Using object.__setattr__ to set fields in a frozen dataclass
        # frozen 데이터클래스의 필드 설정을 위해 object.__setattr__ 사용
        api_key = self._load_api_key()
        models = self._load_ai_models()
        object.__setattr__(self, 'api_key', api_key)
        object.__setattr__(self, 'ai_models', models)
        self._validate()

    def _load_api_key(self) -> str:
        """Load API key from environment / 환경에서 API 키 로드"""
        load_dotenv()
        api_key = os.getenv("OPENROUTER_API_KEY")
        if not api_key:
            raise ConfigurationError(self.get_strings()["error_no_api_key"])
        return api_key
    
    def _load_ai_models(self) -> List[str]:
        """Load AI models from file / 파일에서 AI 모델 로드"""
        try:
            with open(AI_MODELS_FILE, 'r', encoding='utf-8') as f:
                models = [line.strip() for line in f if line.strip() and not line.strip().startswith('#')]
            if not models:
                raise ConfigurationError(f"No models specified in '{AI_MODELS_FILE}'.")
            return models
        except FileNotFoundError:
            raise ConfigurationError(f"File not found at '{AI_MODELS_FILE}'.")
    
    def _validate(self) -> None:
        """Validate configuration / 설정 검증"""
        if not self.prompt_filepath.exists():
            raise ConfigurationError(
                self.get_strings()["error_file_not_found"].format(filepath=self.prompt_filepath)
            )

    def get_strings(self) -> dict:
        """Get localized strings / 지역화된 문자열 가져오기"""
        return STRINGS[self.language]

```
[File: ./config/constants.py]
```python
"""
Application constants and magic strings.
애플리케이션 상수와 매직 문자열.
"""
# REFACTORED: Centralized all configurable constants. / 모든 설정 가능 상수를 중앙화.
# File Names
AI_MODELS_FILE = "ai_models.txt"
MODEL_CACHE_FILE = "model_cache.json"

# API Configuration
DEFAULT_MAX_TOKENS = 65536
API_TIMEOUT = 1200  # 20 minutes
RETRY_ATTEMPTS = 2
RETRY_WAIT_SECONDS = 5
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
OPENROUTER_MODELS_ENDPOINT = f"{OPENROUTER_BASE_URL}/models"

# History Management
TRIMMED_HISTORY_COUNT = 25

# Prompt Parsing
SECTION_HEADERS = {
    'PROJECT_NAME': 'project name',
    'SYSTEM_PROMPT': 'system prompt',
    'PROMPT_PREFIX': 'prompt',
    'DEACTIVE_PREFIX': 'deactive',
}
FILE_COMMANDS = {
    'IMAGE': r"#\s*img\s*:\s*(.+)",
    'PDF': r"#\s*pdf\s*:\s*(.+)",
    'CODE': r"#\s*code\s*:\s*(.+)",
    'DOC': r"#\s*doc\s*:\s*(.+)",
}
REASONING_FLAG = '# reasoning'
OTHER_AI_INFO_FLAG = '# other_ai_info'

# Output Paths
OUTPUT_DIR_PREFIX = "projects"
LIVE_LOG_DIR_NAME = "live_logs"

# Model Data Cache
MODEL_CACHE_TTL = 86400  # 24 hours

# Logging
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
DIVIDER_CHAR = "="
DIVIDER_LENGTH = 80
```
[File: ./core/context.py]
```python
"""
Defines ProjectContext, which holds runtime state for a workflow.
워크플로의 런타임 상태를 보유하는 ProjectContext를 정의.
"""
import re
from pathlib import Path
from dataclasses import dataclass

from config.constants import OUTPUT_DIR_PREFIX, LIVE_LOG_DIR_NAME

# REFACTORED: New class to manage runtime state, separating it from immutable Config.
# 런타임 상태를 관리하는 새 클래스. 불변하는 Config 객체와 책임을 분리.
@dataclass
class ProjectContext:
    """
    Holds all runtime information for a single project workflow.
    단일 프로젝트 워크플로의 모든 런타임 정보를 보유.
    """
    project_name: str
    system_prompt: str
    output_dir: Path
    live_log_dir: Path

    @classmethod
    def from_project_name(cls, project_name: str, system_prompt: str) -> 'ProjectContext':
        """Creates a context instance from a project name. / 프로젝트 이름으로 컨텍스트 인스턴스 생성."""
        folder_name = re.sub(r'[^\w-]', '_', project_name).lower()
        output_dir = Path(OUTPUT_DIR_PREFIX) / folder_name
        live_log_dir = output_dir / LIVE_LOG_DIR_NAME
        return cls(project_name, system_prompt, output_dir, live_log_dir)

```
[File: ./core/engine.py]
```python
"""
Main project workflow engine that controls the execution flow.
실행 흐름을 제어하는 메인 프로젝트 워크플로 엔진.
"""
import asyncio
from typing import List, Dict

from config.config import Config
from config.constants import DIVIDER_CHAR, DIVIDER_LENGTH
from core.context import ProjectContext
from core.models import Prompt, ModelResponse, ModelInfo, PromptResult
from core.exceptions import ProjectError
from services.ai_client import AIModelClient
from services.file_handler import FileHandler
from services.prompt_parser import PromptParser
from services.model_provider import ModelDataProvider
from services.result_handler import ResultHandler
from utils.logger import get_logger

# REFACTORED: Renamed from Orchestrator to WorkflowEngine, focusing solely on orchestration.
# Orchestrator에서 WorkflowEngine으로 이름 변경, 오케스트레이션에만 집중.
class WorkflowEngine:
    """Orchestrates the entire project workflow. / 전체 프로젝트 워크플로를 지휘."""
    
    def __init__(self, config: Config):
        self.config = config
        self.logger = get_logger(self.__class__.__name__)
        self.loc_strings = config.get_strings()
        
        self.file_handler = FileHandler()
        self.prompt_parser = PromptParser()
        self.model_provider = ModelDataProvider()
        
        self.ai_clients: Dict[str, AIModelClient] = {}
        self.prompts: List[Prompt] = []
        self.last_turn_results: Dict[str, PromptResult] = {}
        self.context: ProjectContext
        self.result_handler: ResultHandler

    async def run(self) -> None:
        """Main execution method / 메인 실행 메서드"""
        try:
            await self._initialize_project()
            self._print_startup_info()
            await self._execute_workflow()
            self._print_completion_info()
        except Exception as e:
            self.logger.error(f"Workflow execution failed: {e}")
            raise ProjectError(f"Workflow execution failed: {e}") from e

    async def _initialize_project(self) -> None:
        """Initializes the project context, services, and AI clients."""
        project_name, system_prompt, prompts = self.prompt_parser.parse(
            self.config.prompt_filepath, self.loc_strings
        )
        self.prompts = prompts

        # REFACTORED: Context and ResultHandler manage all output/state, not the engine.
        # 엔진이 아닌 Context와 ResultHandler가 모든 출력/상태를 관리.
        self.context = ProjectContext.from_project_name(project_name, system_prompt)
        self.result_handler = ResultHandler(self.context, self.loc_strings)
        self.result_handler.setup_directories()
        
        await self._initialize_ai_clients()

    async def _initialize_ai_clients(self) -> None:
        """Initializes AI model clients based on config."""
        model_data = await self.model_provider.get_model_data(self.loc_strings)
        for model_id in self.config.ai_models:
            model_info = ModelInfo(
                model_id=model_id,
                max_completion_tokens=model_data.get(model_id, {}).get('max_completion_tokens')
            )
            client = AIModelClient(config=self.config, model_info=model_info, system_prompt=self.context.system_prompt)
            self.ai_clients[model_info.nickname] = client

    def _print_startup_info(self) -> None:
        """Prints startup information to the console."""
        print(self._divider())
        print(self.loc_strings["research_start"].format(project_name=self.context.project_name))
        print(self.loc_strings["output_folder_info"].format(output_dir=self.context.output_dir))
        print(self.loc_strings["models_in_use"].format(models_list=', '.join(self.ai_clients.keys())))
        if not self.config.enable_collaboration:
            print(self.loc_strings["collaboration_disabled"])
        print(self._divider())

    async def _execute_workflow(self) -> None:
        """Executes all prompts in the workflow sequentially."""
        for i, prompt in enumerate(self.prompts):
            is_last_prompt = (i == len(self.prompts) - 1)
            await self._execute_single_prompt(prompt, is_last_prompt)

    async def _execute_single_prompt(self, prompt: Prompt, is_last: bool) -> None:
        """Executes one prompt across all AI models in parallel."""
        print(f"\n\n{self._divider('*')}")
        print(self.loc_strings["prompt_execution"].format(
            prompt_id=prompt.id, total_prompts=len(self.prompts), prompt_name=prompt.name
        ))
        if prompt.use_reasoning: print(self.loc_strings["reasoning_activated"])
        print(self.loc_strings["request_start"].format(num_models=len(self.ai_clients)))

        tasks = [
            self._process_model_task(client, prompt, is_last)
            for client in self.ai_clients.values()
        ]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        current_results: Dict[str, PromptResult] = {}
        for res in results:
            if isinstance(res, PromptResult):
                current_results[res.model_nickname] = res
            elif isinstance(res, Exception):
                self.logger.error(f"A model task failed: {res}")
        
        self.last_turn_results = current_results
        print(self.loc_strings["prompt_finished"].format(prompt_id=prompt.id))
    
    async def _process_model_task(self, client: AIModelClient, prompt: Prompt, is_last: bool) -> PromptResult:
        """Handles the complete lifecycle of a single model's task for a prompt."""
        self.result_handler.log_prompt_header(client.model_info.nickname, prompt)
        
        user_content_str = self._prepare_user_content(prompt, client.model_info.nickname)
        content_payload = self.file_handler.make_message_content(
            user_content_str, prompt.img_files, prompt.pdf_files, prompt.code_files, prompt.doc_files
        )
        
        full_response_text = ""
        try:
            # REFACTORED: Streaming response is now handled here, not in AIClient.
            # 스트리밍 응답을 AIClient가 아닌 여기서 처리.
            async for chunk in client.get_response_stream(content_payload, prompt.use_reasoning):
                full_response_text += chunk
                self.result_handler.log_stream_chunk(client.model_info.nickname, chunk)
            
            print(self.loc_strings["task_completed"].format(nick=client.model_info.nickname))
            
            response = ModelResponse(
                model_nickname=client.model_info.nickname, 
                response_text=full_response_text,
                user_content=content_payload
            )
            self.result_handler.save_result(prompt.id, response, is_last)
            
            # REFACTORED: Now returns a structured PromptResult for the data pipeline.
            # 데이터 파이프라인을 위해 구조화된 PromptResult를 반환.
            return PromptResult.from_response(response)

        except Exception as e:
            self.logger.error(f"Task failed for {client.model_info.nickname}: {e}")
            print(self.loc_strings["task_error"].format(model_nickname=client.model_info.nickname, e=e))
            self.result_handler.log_error(client.model_info.nickname, e)
            raise

    def _prepare_user_content(self, prompt: Prompt, model_nickname: str) -> str:
        """Prepares user content with other AIs' responses if collaboration is on."""
        if not self.config.enable_collaboration or not prompt.has_other_ai_info:
            return prompt.text

        other_ai_responses = []
        for nick, result in self.last_turn_results.items():
            if nick != model_nickname:
                 # REFACTORED: Uses structured data (JSON) if available, otherwise raw text.
                 # 구조화된 데이터(JSON)가 있으면 사용하고, 없으면 원본 텍스트 사용.
                content_to_add = result.structured_data if result.structured_data else result.raw_text
                other_ai_responses.append(f"--- RESPONSE FROM {nick} ---\n{content_to_add}\n")
        
        return f"## PREVIOUS RESPONSES FROM OTHER AIs ##\n{''.join(other_ai_responses)}\n\n## CURRENT REQUEST ##\n{prompt.text}"

    def _print_completion_info(self) -> None:
        """Prints completion information."""
        print(self._divider())
        print(self.loc_strings["all_finished"])
        print(self._divider())

    def _divider(self, char: str = DIVIDER_CHAR, length: int = DIVIDER_LENGTH) -> str:
        return char * length
```
[File: ./core/exceptions.py]
```python
"""
Custom exception definitions.
커스텀 예외 정의.
"""
# No changes needed. This file is well-designed.
# 변경 필요 없음. 파일이 잘 설계됨.

class ProjectError(Exception):
    """Base exception for project-related errors / 프로젝트 관련 오류의 기본 예외"""
    pass


class ConfigurationError(ProjectError):
    """Configuration-related errors / 설정 관련 오류"""
    pass


class FileProcessingError(ProjectError):
    """File processing errors / 파일 처리 오류"""
    pass


class APIError(ProjectError):
    """API interaction errors / API 상호작용 오류"""
    pass


class PromptParsingError(ProjectError):
    """Prompt file parsing errors / 프롬프트 파일 파싱 오류"""
    pass
```
[File: ./core/models.py]
```python
"""
Data models using dataclasses.
데이터클래스를 사용한 데이터 모델.
"""
import json
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any

@dataclass(frozen=True)
class Prompt:
    id: int
    name: str
    text: str
    use_reasoning: bool = False
    has_other_ai_info: bool = False
    img_files: List[str] = field(default_factory=list)
    pdf_files: List[str] = field(default_factory=list)
    code_files: List[str] = field(default_factory=list)
    doc_files: List[str] = field(default_factory=list)

@dataclass(frozen=True)
class ModelInfo:
    model_id: str
    max_completion_tokens: Optional[int] = None
    nickname: str = field(init=False)
    
    def __post_init__(self):
        object.__setattr__(self, 'nickname', self.model_id.split('/')[-1])

@dataclass(frozen=True)
class Message:
    role: str
    content: Any

@dataclass(frozen=True)
class ModelResponse:
    # REFACTORED: Renamed from APIResponse for clarity. / 명확성을 위해 APIResponse에서 이름 변경.
    model_nickname: str
    response_text: Optional[str]
    user_content: Any
    error: Optional[Exception] = None

# REFACTORED: New class to support the structured data pipeline.
# 구조화된 데이터 파이프라인을 지원하기 위한 새 클래스.
@dataclass(frozen=True)
class PromptResult:
    """Represents the processed result from a model for one prompt."""
    model_nickname: str
    raw_text: str
    structured_data: Optional[Dict[str, Any]] = None

    @classmethod
    def from_response(cls, response: ModelResponse) -> 'PromptResult':
        if not response.response_text:
            return cls(response.model_nickname, "")
            
        raw_text = response.response_text
        structured_data = None
        try:
            # Attempt to find and parse a JSON block
            json_match = json.loads(raw_text)
            if isinstance(json_match, dict):
                structured_data = json_match
        except (json.JSONDecodeError, TypeError):
            # Not a valid JSON response, treat as raw text
            pass
        return cls(response.model_nickname, raw_text, structured_data)
```
[File: ./services/ai_client.py]
```python
"""
AI model client for interacting with OpenRouter API.
OpenRouter API와 상호작용하는 AI 모델 클라이언트.
"""
from typing import List, Dict, Any, AsyncGenerator
from openai import AsyncOpenAI, APITimeoutError, APIConnectionError, APIStatusError
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type

from config.config import Config
from config.constants import *
from core.models import ModelInfo, Message
from utils.logger import get_logger

class AIModelClient:
    """Manages interaction with a specific AI model. / 특정 AI 모델과의 상호작용을 관리."""
    
    def __init__(self, config: Config, model_info: ModelInfo, system_prompt: str):
        self.config = config
        self.model_info = model_info
        self.system_prompt = system_prompt
        self.logger = get_logger(f"{self.__class__.__name__}.{model_info.nickname}")
        
        self.client = AsyncOpenAI(base_url=OPENROUTER_BASE_URL, api_key=config.api_key)
        self.history: List[Message] = []
        self.max_tokens = model_info.max_completion_tokens or DEFAULT_MAX_TOKENS

    # REFACTORED: Changed to an async generator (`get_response_stream`) to decouple streaming from file I/O.
    # 스트리밍과 파일 I/O를 분리하기 위해 비동기 제너레이터(`get_response_stream`)로 변경.
    async def get_response_stream(self, content: Any, use_reasoning: bool) -> AsyncGenerator[str, None]:
        """Gets a streaming response from the AI model, yielding content chunks."""
        messages = self._prepare_messages(content)
        extra_body = {"plugins": [{"id": "web"}]}
        if use_reasoning:
            extra_body['reasoning'] = {}
        
        try:
            stream = await self._get_ai_response_stream(messages, extra_body)
            full_response = ""
            async for chunk in stream:
                delta = chunk.choices[0].delta
                if hasattr(delta, 'reasoning') and delta.reasoning:
                    yield delta.reasoning
                if delta.content:
                    full_response += delta.content
                    yield delta.content
            
            self._update_history(content, full_response)
        
        except (APIStatusError, APIConnectionError, APITimeoutError) as e:
            self.logger.error(f"API Error getting response: {e}")
            raise
        except Exception as e:
            self.logger.exception(f"Unexpected error getting response: {e}")
            raise

    def _prepare_messages(self, content: Any) -> List[Dict[str, Any]]:
        """Prepares messages for API call, including history. / 히스토리를 포함하여 API 호출 메시지를 준비."""
        messages = [{"role": "system", "content": self.system_prompt}]
        history_messages = [
            {"role": msg.role, "content": msg.content} 
            for msg in self.history[-(TRIMMED_HISTORY_COUNT * 2):]
        ]
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
        """Gets streaming response from API with retry. / 재시도와 함께 API에서 스트리밍 응답 받기."""
        return await self.client.chat.completions.create(
            model=self.model_info.model_id,
            messages=messages,
            stream=True,
            timeout=API_TIMEOUT,
            max_tokens=self.max_tokens,
            extra_body=extra_body
        )

    def _update_history(self, user_content: Any, assistant_response: str) -> None:
        """Updates conversation history. / 대화 히스토리를 업데이트."""
        self.history.append(Message(role="user", content=user_content))
        self.history.append(Message(role="assistant", content=assistant_response))
```
[File: ./services/file_handler.py]
```python
# No significant changes needed, but added comments for clarity as per plan.
# 큰 변경은 필요 없지만, 계획에 따라 명확성을 위해 주석 추가.
import base64
import mimetypes
from typing import List, Dict, Any, Optional
from pathlib import Path

from core.exceptions import FileProcessingError
from utils.logger import get_logger

class FileHandler:
    """Handles file processing for attachments. / 첨부 파일 처리를 담당."""
    
    def __init__(self):
        self.logger = get_logger(self.__class__.__name__)
    
    def make_message_content(
        self,
        prompt_text: str,
        img_files: Optional[List[str]] = None,
        pdf_files: Optional[List[str]] = None,
        code_files: Optional[List[str]] = None,
        doc_files: Optional[List[str]] = None
    ) -> Any:
        """Creates message content with file attachments. / 파일 첨부가 있는 메시지 콘텐츠 생성."""
        content = []
        
        # Helper methods could be used here, but current structure is clear enough.
        # 헬퍼 메서드를 사용할 수도 있지만, 현재 구조도 충분히 명확함.
        if doc_files:
            for path in doc_files: content.extend(self._handle_text_file(path, "markdown"))
        if code_files:
            for path in code_files: content.extend(self._handle_text_file(path, "python")) # Simple default
        
        content.append({"type": "text", "text": prompt_text})
        
        if img_files:
            for path in img_files: content.extend(self._handle_image_file(path))
        if pdf_files:
            for path in pdf_files: content.extend(self._handle_pdf_file(path))
        
        return content[0]["text"] if len(content) == 1 and content[0]["type"] == "text" else content

    def _handle_text_file(self, file_path: str, lang: str) -> List[Dict[str, Any]]:
        """Handles any text-based file (docs, code). / 텍스트 기반 파일(문서, 코드) 처리."""
        path = Path(file_path)
        if not path.exists(): raise FileProcessingError(f"File not found: {file_path}")
        try:
            content = path.read_text(encoding='utf-8')
            return [{"type": "text", "text": f"[File: {file_path}]\n```{lang}\n{content}\n```"}]
        except Exception as e:
            raise FileProcessingError(f"Error reading file {file_path}: {e}") from e

    def _handle_image_file(self, img_path: str) -> List[Dict[str, Any]]:
        """Handles local or URL image files. / 로컬 또는 URL 이미지 파일 처리."""
        if img_path.startswith("http"):
            return [{"type": "image_url", "image_url": {"url": img_path}}]
        
        path = Path(img_path)
        if not path.exists(): raise FileProcessingError(f"Image not found: {img_path}")
        
        try:
            mime_type, _ = mimetypes.guess_type(img_path)
            with open(path, 'rb') as f:
                b64_data = base64.b64encode(f.read()).decode('utf-8')
            return [{"type": "image_url", "image_url": {"url": f"data:{mime_type or 'image/jpeg'};base64,{b64_data}"}}]
        except Exception as e:
            raise FileProcessingError(f"Error processing image {img_path}: {e}") from e
    
    def _handle_pdf_file(self, pdf_path: str) -> List[Dict[str, Any]]:
        """Handles PDF files by encoding them. / PDF 파일을 인코딩하여 처리."""
        path = Path(pdf_path)
        if not path.exists(): raise FileProcessingError(f"PDF not found: {pdf_path}")
        try:
            with open(path, 'rb') as f:
                b64_data = base64.b64encode(f.read()).decode('utf-8')
            return [{"type": "tool_use", "tool_use": {"file": {"data": b64_data, "mime_type": "application/pdf"}}}]
        except Exception as e:
            raise FileProcessingError(f"Error processing PDF {pdf_path}: {e}") from e

```
[File: ./services/model_provider.py]
```python
"""
Model data provider service with caching.
캐싱이 있는 모델 데이터 제공 서비스.
"""
import os
import json
import time
from typing import Dict
from pathlib import Path
import aiohttp

from config.constants import MODEL_CACHE_FILE, MODEL_CACHE_TTL, OPENROUTER_MODELS_ENDPOINT
from utils.logger import get_logger

# This class was already well-structured. No changes required.
# 이 클래스는 이미 구조가 좋아서 변경이 필요 없음.
class ModelDataProvider:
    """Fetches and caches model data from OpenRouter. / OpenRouter에서 모델 데이터를 가져오고 캐싱."""
    
    def __init__(self):
        self.logger = get_logger(self.__class__.__name__)
        self.cache_file = Path(MODEL_CACHE_FILE)
    
    async def get_model_data(self, loc_strings: Dict[str, str]) -> Dict[str, Dict]:
        """Get model data, using cache if valid. / 유효한 경우 캐시를 사용하여 모델 데이터 가져오기."""
        if self._is_cache_valid():
            try:
                with open(self.cache_file, 'r', encoding='utf-8') as f:
                    self.logger.info("Loaded model data from cache")
                    return json.load(f)
            except Exception as e:
                self.logger.warning(f"Failed to load cache: {e}")
        
        print(loc_strings["fetching_models"])
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(OPENROUTER_MODELS_ENDPOINT) as response:
                    response.raise_for_status()
                    data = await response.json()
            
            model_data = {
                model['id']: {'max_completion_tokens': model.get('top_provider', {}).get('max_completion_tokens')}
                for model in data.get('data', [])
            }
            self._save_cache(model_data)
            return model_data
            
        except aiohttp.ClientError as e:
            print(f"{loc_strings['fetching_models_failed']} ({e})")
            self.logger.error(f"Failed to fetch model data: {e}")
            return {}
    
    def _is_cache_valid(self) -> bool:
        """Check if cache file exists and is fresh. / 캐시 파일이 존재하고 유효한지 확인."""
        return self.cache_file.exists() and (time.time() - os.path.getmtime(self.cache_file)) < MODEL_CACHE_TTL
    
    def _save_cache(self, data: Dict[str, Dict]) -> None:
        """Save data to cache file. / 캐시 파일에 데이터 저장."""
        try:
            with open(self.cache_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
            self.logger.info("Model data cached successfully")
        except Exception as e:
            self.logger.error(f"Failed to save cache: {e}")
```
[File: ./services/prompt_parser.py]
```python
"""
Prompt file parsing service.
프롬프트 파일 파싱 서비스.
"""
import re
from typing import List, Tuple, Dict
from pathlib import Path

from core.models import Prompt
from core.exceptions import PromptParsingError
from config.constants import *
from utils.logger import get_logger

class PromptParser:
    """Parses prompt files and extracts structured data. / 프롬프트 파일을 파싱하고 구조화된 데이터를 추출."""
    
    def __init__(self):
        self.logger = get_logger(self.__class__.__name__)
    
    def parse(self, filepath: Path, loc_strings: Dict[str, str]) -> Tuple[str, str, List[Prompt]]:
        """Parses a prompt file into project info and a list of Prompts."""
        try:
            content = filepath.read_text(encoding='utf-8')
        except FileNotFoundError:
            raise PromptParsingError(loc_strings["error_file_not_found"].format(filepath=filepath))
        
        headers, sections = self._extract_sections(content)
        if not headers: raise PromptParsingError(loc_strings["error_no_headers"].format(filepath=filepath))
        
        project_name, system_prompt = None, None
        prompts = []
        
        for header, text in zip(headers, sections):
            clean_text, header_lower = text.strip(), header.lower()
            
            if header_lower.startswith(SECTION_HEADERS['DEACTIVE_PREFIX']): continue
            if header_lower == SECTION_HEADERS['PROJECT_NAME']: project_name = clean_text
            elif header_lower == SECTION_HEADERS['SYSTEM_PROMPT']: system_prompt = clean_text
            elif header_lower.startswith(SECTION_HEADERS['PROMPT_PREFIX']):
                prompts.append(self._parse_prompt_section(header, clean_text))
        
        if not project_name: raise PromptParsingError(loc_strings["error_no_project_name"])
        if not system_prompt: raise PromptParsingError(loc_strings["error_no_system_prompt"])
        
        return project_name, system_prompt, sorted(prompts, key=lambda p: p.id)
    
    def _extract_sections(self, content: str) -> Tuple[List[str], List[str]]:
        """Extracts headers and their content sections. / 헤더와 콘텐츠 섹션 추출."""
        headers = re.findall(r"##\s*(.*?)\s*##", content)
        sections = re.split(r"##\s*.*?\s*##", content)[1:]
        return headers, sections
    
    def _parse_prompt_section(self, header: str, content: str) -> Prompt:
        """Parses a single prompt section into a Prompt object."""
        id_match = re.search(r'\d+', header)
        if not id_match: raise PromptParsingError(f"No ID in prompt header: {header}")
        
        prompt_text, attachments = self._extract_attachments(content)
        
        use_reasoning = REASONING_FLAG in prompt_text.lower()
        has_other_ai_info = OTHER_AI_INFO_FLAG in prompt_text.lower()
        
        clean_text = re.sub(rf'({REASONING_FLAG}|{OTHER_AI_INFO_FLAG})', '', prompt_text, flags=re.IGNORECASE).strip()
        
        return Prompt(
            id=int(id_match.group()), name=header, text=clean_text,
            use_reasoning=use_reasoning, has_other_ai_info=has_other_ai_info, **attachments
        )
    
    # REFACTORED: Extracted attachment parsing into its own method to simplify parent.
    # 부모 메서드를 단순화하기 위해 첨부 파일 파싱 로직을 별도 메서드로 추출.
    def _extract_attachments(self, content: str) -> Tuple[str, Dict[str, List[str]]]:
        """Extracts file attachments and flags from prompt content."""
        attachments = {'img_files': [], 'pdf_files': [], 'code_files': [], 'doc_files': []}
        lines = content.splitlines()
        text_lines = []
        
        for line in lines:
            matched = False
            for key, pattern in FILE_COMMANDS.items():
                match = re.match(pattern, line, re.IGNORECASE)
                if match:
                    attachments[f"{key.lower()}_files"].append(match.group(1).strip())
                    matched = True
                    break
            if not matched: text_lines.append(line)
        
        return '\n'.join(text_lines), attachments
```
[File: ./services/result_handler.py]
```python
"""
Handles all file I/O operations for results and logs.
결과 및 로그에 대한 모든 파일 I/O 작업을 처리.
"""
import shutil
from datetime import datetime
from pathlib import Path

from core.context import ProjectContext
from core.models import Prompt, ModelResponse
from config.constants import DIVIDER_CHAR, DIVIDER_LENGTH

# REFACTORED: New class to handle all file I/O, adhering to SRP.
# 모든 파일 I/O를 처리하는 새 클래스. 단일 책임 원칙 준수.
class ResultHandler:
    """Manages writing all outputs to the file system. / 모든 출력물을 파일 시스템에 쓰는 것을 관리."""
    
    def __init__(self, context: ProjectContext, loc_strings: dict):
        self.context = context
        self.loc_strings = loc_strings

    def setup_directories(self) -> None:
        """Cleans and creates the necessary output directories."""
        if self.context.live_log_dir.exists():
            shutil.rmtree(self.context.live_log_dir)
        self.context.live_log_dir.mkdir(parents=True, exist_ok=True)
        self.context.output_dir.mkdir(parents=True, exist_ok=True)

    def save_result(self, prompt_id: int, response: ModelResponse, is_final: bool) -> None:
        """Saves the response from a model to a file."""
        filename_prefix = "final" if is_final else f"p{prompt_id}"
        output_path = self.context.output_dir / f"{filename_prefix}_{response.model_nickname}.md"
        content = response.response_text or f"[ERROR: {response.error}]"
        header = f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        output_path.write_text(header + content, encoding='utf-8')

    def log_prompt_header(self, model_nickname: str, prompt: Prompt) -> None:
        """Writes a prompt header to the live log file."""
        log_path = self._get_log_path(model_nickname)
        divider = DIVIDER_CHAR * 20
        header = self.loc_strings["log_prompt_header"].format(
            divider=divider, prompt_id=prompt.id, prompt_name=prompt.name
        )
        with log_path.open('a', encoding='utf-8') as f:
            f.write(header)
            if prompt.use_reasoning:
                f.write(self.loc_strings["log_reasoning_header"])

    def log_stream_chunk(self, model_nickname: str, chunk: str) -> None:
        """Appends a chunk of streaming text to the live log."""
        log_path = self._get_log_path(model_nickname)
        with log_path.open('a', encoding='utf-8') as f:
            f.write(chunk)
            f.flush()

    def log_error(self, model_nickname: str, error: Exception) -> None:
        """Logs an error message to the live log."""
        log_path = self._get_log_path(model_nickname)
        error_message = self.loc_strings["log_error_header"].format(error_message=str(error))
        with log_path.open('a', encoding='utf-8') as f:
            f.write(error_message)

    def _get_log_path(self, model_nickname: str) -> Path:
        """Constructs the path for a model's live log file."""
        return self.context.live_log_dir / f"{model_nickname}.log"

```
[File: ./utils/logger.py]
```python
"""
Logging configuration and utilities.
로깅 설정 및 유틸리티.
"""
import logging
import sys

from config.constants import LOG_FORMAT, LOG_DATE_FORMAT

# This module is already well-designed. No changes required.
# 이 모듈은 이미 잘 설계되어 변경이 필요 없음.
def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Setup and return a logger instance. / 로거 인스턴스를 설정하고 반환."""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    if not logger.handlers:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(level)
        formatter = logging.Formatter(LOG_FORMAT, LOG_DATE_FORMAT)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
    
    return logger

def get_logger(name: str) -> logging.Logger:
    """Get a logger instance for the given name. / 주어진 이름의 로거 인스턴스 가져오기."""
    return logging.getLogger(name)

```
---

### 3. 변경사항 요약표

| 항목 | 변경 전 | 변경 후 | 개선 효과 |
| :--- | :--- |:--- | :--- |
| **핵심 제어 클래스** | `ProjectOrchestrator` (1개 클래스) | `WorkflowEngine`, `ProjectContext`, `ResultHandler` (3개 클래스) | **SRP 준수**, 테스트 용이성 |
| **설정 관리** | `Config` (가변 객체) | `Config` (불변 객체), `ProjectContext` (런타임 상태) | **안정성**, 상태 추적 용이 |
| **AI 클라이언트** | API 호출 + 파일 쓰기 + 히스토리 관리 | API 호출 + 히스토리 관리 (파일 쓰기 책임 제거) | **SRP 준수**, 의존성 감소 |
| **데이터 파이프라인** | `Dict[str, str]` (순수 텍스트) | `Dict[str, PromptResult]` (구조화된 객체) | **안정성**, 기능 확장성 |
| **파일 입출력(I/O)** | `Orchestrator`, `AIClient`에 분산 | `ResultHandler`에 중앙 집중 | **SRP 준수**, 유지보수성 |
| **파싱 로직** | `_parse_prompt_section` 내 복합 로직 | `_extract_attachments` 헬퍼 함수로 분리 | **가독성**, 유지보수성 |