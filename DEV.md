# AI-Forge 개발자 문서

## 아키텍처 개요

AI-Forge는 계층화된 아키텍처를 채택하여 각 컴포넌트의 책임을 명확히 분리했습니다:

```
┌─────────────────┐
│     main.py     │  진입점 및 CLI
└────────┬────────┘
         │
┌────────▼────────┐
│  Orchestrator   │  워크플로우 제어
└────────┬────────┘
         │
┌────────▼────────────────────────┐
│  Services Layer                 │
│  ├─ AIClient     (API 통신)     │
│  ├─ PromptParser (파싱)         │
│  ├─ FileHandler  (파일 처리)    │
│  └─ ResultHandler(결과 저장)    │
└─────────────────────────────────┘
```

## 디렉토리 구조 설명

```
.
├── config/
│   ├── config.py      # 설정 관리 (불변 객체)
│   └── constants.py   # 모든 상수 중앙화
├── core/
│   ├── orchestrator.py # 메인 워크플로우 엔진
│   ├── models.py      # 데이터 모델 정의
│   └── exceptions.py  # 커스텀 예외 클래스
├── services/
│   ├── ai_client.py   # AI API 통신 전담
│   ├── file_handler.py # 멀티모달 파일 처리
│   ├── prompt_parser.py # 프롬프트 파일 파싱
│   └── result_handler.py # 파일 I/O 전담
└── utils/
    ├── logger.py      # 로깅 설정
    └── error_handler.py # 에러 처리 데코레이터
```

## 핵심 컴포넌트 상세

### 1. ProjectOrchestrator

**역할**: 전체 워크플로우를 제어하는 중앙 컨트롤러

**주요 메서드**:
```python
async def run(self) -> None:
    """메인 실행 - 프로젝트 초기화부터 완료까지"""
    await self._initialize_project()
    self._setup_output_directories()
    await self._initialize_ai_clients()
    await self._execute_prompts()

async def _execute_prompt_parallel(self, prompt: Prompt, index: int, is_last: bool):
    """모든 AI 모델에 대해 병렬로 프롬프트 실행"""
    tasks = [self._create_model_task(nick, client, prompt, index, is_last) 
             for nick, client in self.ai_clients.items()]
    responses = await asyncio.gather(*tasks, return_exceptions=True)
```

### 2. AIModelClient

**역할**: OpenRouter API와의 통신만 담당 (단일 책임 원칙)

**주요 메서드**:
```python
async def get_response(self, content: Any, use_reasoning: bool) -> APIResponse:
    """AI 모델로부터 응답을 받아 반환"""
    messages = self._prepare_messages(content)
    stream = await self._get_ai_response_stream(messages, extra_body)
    full_response = await self._collect_stream_response(stream)
    return APIResponse(...)
```

### 3. PromptResult (데이터 파이프라인)

**역할**: AI 간 협업 시 구조화된 데이터 전달

```python
@dataclass
class PromptResult:
    model_nickname: str
    raw_text: str
    structured_data: Optional[Dict[str, Any]] = None
    
    @staticmethod
    def from_response(response: APIResponse) -> 'PromptResult':
        """JSON 블록을 자동으로 추출하여 구조화"""
```

### 4. ResultHandler

**역할**: 모든 파일 I/O 작업을 중앙에서 관리

```python
class ResultHandler:
    def save_final_result(self, project_dir: Path, model_nickname: str, content: str):
    def write_log_header(self, log_path: Path, prompt_id: int, prompt_name: str):
    def append_to_log(self, log_path: Path, content: str):
```

## 설계 결정 및 트레이드오프

### 1. 불변 설정 vs 런타임 컨텍스트

**결정**: `Config`는 불변, `ProjectContext`는 런타임 상태 관리

**이유**:
- 설정의 예측 가능성 향상
- 디버깅 시 상태 추적 용이
- 멀티스레드 환경에서의 안전성

**대안**: 모든 것을 Config에 통합
- 장점: 단순함
- 단점: 런타임 상태와 설정의 경계 모호

### 2. 구조화된 데이터 파이프라인

**결정**: `PromptResult`를 통한 JSON 지원

**이유**:
- AI 간 정보 전달의 정확성 향상
- 복잡한 워크플로우에서의 데이터 무결성
- 향후 고급 분석 기능 추가 용이

### 3. 서비스 레이어 분리

**결정**: 파일 I/O를 `ResultHandler`로 완전 분리

**이유**:
- 테스트 용이성 (모킹 간편)
- 단일 책임 원칙 준수
- 파일 시스템 변경 시 영향 최소화

## 리팩토링 히스토리

### Phase 1: Critical Issues (Week 1)
- **구조적 데이터 파이프라인 도입**: `Dict[str, str]` → `Dict[str, PromptResult]`
  - 정보 손실 방지, JSON 자동 파싱
- **SRP 리팩토링**: `AIModelClient`에서 파일 I/O 분리
  - 순환 복잡도 12 → 7로 감소

### Phase 2: Major Improvements (Week 2)
- **ProjectContext 도입**: 런타임 상태 분리
- **에러 처리 데코레이터**: 중복 코드 70% 제거

### Phase 3: Minor Optimizations (Week 3)
- **상수 중앙화**: 모든 매직 넘버를 `constants.py`로 이동
- **타입 힌트 100% 적용**

## 외부 라이브러리 설명

### 1. OpenAI (openai)
- **용도**: OpenRouter API 클라이언트
- **선택 이유**: OpenRouter가 OpenAI 호환 API 제공
- **대안**: `httpx` 직접 사용 (더 낮은 수준의 제어)

### 2. Tenacity
- **용도**: API 재시도 로직
- **선택 이유**: 데코레이터 기반의 깔끔한 구현
- **대안**: `backoff`, 수동 구현

### 3. aiohttp
- **용도**: 비동기 HTTP 요청 (모델 메타데이터)
- **선택 이유**: asyncio와의 완벽한 통합
- **대안**: `httpx` (동기/비동기 모두 지원)

### 4. python-dotenv
- **용도**: 환경 변수 관리
- **선택 이유**: 표준적인 `.env` 파일 형식
- **대안**: `python-decouple`, OS 환경 변수 직접 사용

## 향후 확장 가이드

### 1. 새로운 파일 타입 지원 추가
```python
# file_handler.py에 메서드 추가
def _handle_video_file(self, video_path: str) -> List[Dict[str, Any]]:
    # 비디오 처리 로직
    pass

# constants.py에 패턴 추가
FILE_COMMANDS['VIDEO'] = r"#\s*video\s+(.+)"
```

### 2. 커스텀 AI 제공자 추가
```python
# 새 클라이언트 클래스 생성
class CustomAIClient(AIModelClient):
    async def _get_ai_response_stream(self, messages, extra_body):
        # 커스텀 API 호출 로직
        pass
```

### 3. 새로운 워크플로우 타입 추가
```python
# 새 파서 생성 또는 기존 파서 확장
class WorkflowParser(PromptParser):
    def parse_workflow_specific_tags(self, content: str):
        # 워크플로우별 특수 태그 처리
        pass
```

### 4. 플러그인 시스템 구현
```python
# 플러그인 인터페이스 정의
class AIForgePlugin:
    def pre_prompt_execution(self, prompt: Prompt): pass
    def post_response_processing(self, response: PromptResult): pass
```

---

# AI-Forge Developer Documentation

## Architecture Overview

AI-Forge adopts a layered architecture with clear separation of responsibilities:

```
┌─────────────────┐
│     main.py     │  Entry point & CLI
└────────┬────────┘
         │
┌────────▼────────┐
│  Orchestrator   │  Workflow control
└────────┬────────┘
         │
┌────────▼────────────────────────┐
│  Services Layer                 │
│  ├─ AIClient     (API comm)     │
│  ├─ PromptParser (Parsing)      │
│  ├─ FileHandler  (File proc)    │
│  └─ ResultHandler(Result save)  │
└─────────────────────────────────┘
```

## Directory Structure

```
.
├── config/
│   ├── config.py      # Configuration management (immutable)
│   └── constants.py   # All constants centralized
├── core/
│   ├── orchestrator.py # Main workflow engine
│   ├── models.py      # Data model definitions
│   └── exceptions.py  # Custom exception classes
├── services/
│   ├── ai_client.py   # AI API communication
│   ├── file_handler.py # Multimodal file processing
│   ├── prompt_parser.py # Prompt file parsing
│   └── result_handler.py # File I/O operations
└── utils/
    ├── logger.py      # Logging configuration
    └── error_handler.py # Error handling decorator
```

## Core Components

### 1. ProjectOrchestrator

**Role**: Central controller managing the entire workflow

**Key Methods**:
```python
async def run(self) -> None:
    """Main execution - from project initialization to completion"""
    await self._initialize_project()
    self._setup_output_directories()
    await self._initialize_ai_clients()
    await self._execute_prompts()

async def _execute_prompt_parallel(self, prompt: Prompt, index: int, is_last: bool):
    """Execute prompt for all AI models in parallel"""
    tasks = [self._create_model_task(nick, client, prompt, index, is_last) 
             for nick, client in self.ai_clients.items()]
    responses = await asyncio.gather(*tasks, return_exceptions=True)
```

### 2. AIModelClient

**Role**: Handles only OpenRouter API communication (Single Responsibility Principle)

**Key Methods**:
```python
async def get_response(self, content: Any, use_reasoning: bool) -> APIResponse:
    """Get response from AI model"""
    messages = self._prepare_messages(content)
    stream = await self._get_ai_response_stream(messages, extra_body)
    full_response = await self._collect_stream_response(stream)
    return APIResponse(...)
```

### 3. PromptResult (Data Pipeline)

**Role**: Structured data transfer for AI collaboration

```python
@dataclass
class PromptResult:
    model_nickname: str
    raw_text: str
    structured_data: Optional[Dict[str, Any]] = None
    
    @staticmethod
    def from_response(response: APIResponse) -> 'PromptResult':
        """Automatically extract and structure JSON blocks"""
```

### 4. ResultHandler

**Role**: Centralized management of all file I/O operations

```python
class ResultHandler:
    def save_final_result(self, project_dir: Path, model_nickname: str, content: str):
    def write_log_header(self, log_path: Path, prompt_id: int, prompt_name: str):
    def append_to_log(self, log_path: Path, content: str):
```

## Design Decisions and Trade-offs

### 1. Immutable Config vs Runtime Context

**Decision**: `Config` is immutable, `ProjectContext` manages runtime state

**Rationale**:
- Improved predictability of configuration
- Easier state tracking during debugging
- Thread safety in multi-threaded environments

**Alternative**: Integrate everything into Config
- Pros: Simplicity
- Cons: Blurred boundaries between runtime state and configuration

### 2. Structured Data Pipeline

**Decision**: JSON support through `PromptResult`

**Rationale**:
- Improved accuracy of information transfer between AIs
- Data integrity in complex workflows
- Easy addition of advanced analysis features

### 3. Service Layer Separation

**Decision**: Complete separation of file I/O into `ResultHandler`

**Rationale**:
- Testability (easy mocking)
- Single Responsibility Principle compliance
- Minimize impact of file system changes

## Refactoring History

### Phase 1: Critical Issues (Week 1)
- **Structured Data Pipeline**: `Dict[str, str]` → `Dict[str, PromptResult]`
  - Prevent information loss, automatic JSON parsing
- **SRP Refactoring**: Separated file I/O from `AIModelClient`
  - Reduced cyclomatic complexity from 12 to 7

### Phase 2: Major Improvements (Week 2)
- **ProjectContext Introduction**: Separated runtime state
- **Error Handling Decorator**: 70% duplicate code removal

### Phase 3: Minor Optimizations (Week 3)
- **Constant Centralization**: Moved all magic numbers to `constants.py`
- **100% Type Hint Coverage**

## External Libraries

### 1. OpenAI (openai)
- **Purpose**: OpenRouter API client
- **Why chosen**: OpenRouter provides OpenAI-compatible API
- **Alternative**: Direct `httpx` usage (lower-level control)

### 2. Tenacity
- **Purpose**: API retry logic
- **Why chosen**: Clean decorator-based implementation
- **Alternative**: `backoff`, manual implementation

### 3. aiohttp
- **Purpose**: Async HTTP requests (model metadata)
- **Why chosen**: Perfect integration with asyncio
- **Alternative**: `httpx` (supports both sync/async)

### 4. python-dotenv
- **Purpose**: Environment variable management
- **Why chosen**: Standard `.env` file format
- **Alternative**: `python-decouple`, direct OS environment variables

## Extension Guide

### 1. Adding New File Type Support
```python
# Add method to file_handler.py
def _handle_video_file(self, video_path: str) -> List[Dict[str, Any]]:
    # Video processing logic
    pass

# Add pattern to constants.py
FILE_COMMANDS['VIDEO'] = r"#\s*video\s+(.+)"
```

### 2. Adding Custom AI Provider
```python
# Create new client class
class CustomAIClient(AIModelClient):
    async def _get_ai_response_stream(self, messages, extra_body):
        # Custom API call logic
        pass
```

### 3. Adding New Workflow Types
```python
# Create new parser or extend existing
class WorkflowParser(PromptParser):
    def parse_workflow_specific_tags(self, content: str):
        # Handle workflow-specific tags
        pass
```

### 4. Implementing Plugin System
```python
# Define plugin interface
class AIForgePlugin:
    def pre_prompt_execution(self, prompt: Prompt): pass
    def post_response_processing(self, response: PromptResult): pass
```