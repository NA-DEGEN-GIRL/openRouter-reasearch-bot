2025-07-18 10:23:56
## 한글 버전

### README.md

# AI-Forge: AI 워크플로우 오케스트레이터

여러 AI 모델을 동시에 실행하고, 프롬프트 파일 하나로 복잡한 AI 협업 워크플로우를 자동화하는 프레임워크입니다.

## 주요 기능

- **다중 AI 병렬 처리**: 여러 AI 모델에 동일한 작업을 동시에 요청하여 처리 시간 단축
- **프롬프트 기반 워크플로우**: 마크다운 파일로 전체 작업 흐름을 정의
- **AI 간 협업**: 이전 단계의 AI 응답을 다음 단계에서 참조하여 결과 개선
- **멀티모달 입력**: 이미지, PDF, 코드, 문서 파일을 AI에게 직접 전달
- **실시간 로그 모니터링**: 각 AI의 작업 진행 상황을 실시간으로 확인

## 설치 가이드

### 1. 저장소 복제
```bash
git clone https://github.com/your-username/ai-forge.git
cd ai-forge
```

### 2. Python 가상 환경 설정 (권장)
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 또는
venv\Scripts\activate  # Windows
```

### 3. 의존성 설치
```bash
pip install -r requirements.txt
```

### 4. 환경 설정
```bash
cp .env.example .env
```

`.env` 파일을 열고 OpenRouter API 키를 입력하세요:
```
OPENROUTER_API_KEY=your_api_key_here
```

### 5. AI 모델 설정
`ai_models.txt` 파일에 사용할 모델을 한 줄에 하나씩 입력:
```
google/gemini-2.0-flash-thinking-exp:free
anthropic/claude-3.5-sonnet
openai/gpt-4-turbo
```

## 사용법 및 예시

### 기본 실행
```bash
python main.py
```

실행하면 다음과 같은 선택 화면이 나타납니다:
1. 언어 선택 (한국어/영어)
2. 봇 모드 선택 (표준 리서치 봇/커스텀 프롬프트)

### 명령줄 옵션
```bash
# 언어와 프롬프트 파일 직접 지정
python main.py --lang ko --prompt my_custom.md

# AI 협업 비활성화
python main.py --no-collaboration

# PDF 처리 엔진 지정
python main.py --pdf-engine mistral-ocr
```

### 프롬프트 파일 작성법

프롬프트 파일은 `prompts/` 폴더 안에 `.md` 파일로 작성합니다.

#### 기본 구조
```markdown
## project name ##
내 프로젝트 이름

## system prompt ##
당신은 전문 분석가입니다. 정확하고 상세한 분석을 제공하세요.

## prompt1: 첫 번째 작업 ##
# reasoning
프로젝트에 대한 기본 정보를 수집하고 분석하세요.

## prompt2: 두 번째 작업 ##
# other_ai_info
이전 분석을 바탕으로 심층 분석을 수행하세요.
```

#### 특수 태그 설명

1. **`# reasoning`**: AI의 사고 과정을 로그에 기록
2. **`# other_ai_info`**: 이전 단계의 다른 AI 응답을 참조
3. **파일 첨부 태그**:
   - `# img: path/to/image.jpg` - 이미지 첨부
   - `# pdf: path/to/document.pdf` - PDF 첨부
   - `# code: path/to/script.py` - 코드 파일 첨부
   - `# doc: path/to/readme.md` - 문서 파일 첨부

### 기본 예시: research.md

`prompts/research.md`는 프로젝트 분석을 위한 기본 템플릿입니다:

```markdown
## project name ##
GTE

## system prompt ##
당신은 전문 블록체인 프로젝트 분석가입니다...

## prompt1: 심층 분석 및 보고 ##
# reasoning
**project info**
GTE
• 한 줄 소개: Decentralized trading platform
• Tag: DeFi, DEX
• web: https://www.gte.xyz/
...
**end of project info**
```

이 예시를 사용하려면:
1. `**project info**`와 `**end of project info**` 사이의 내용을 분석하려는 프로젝트 정보로 교체
2. 프로젝트 이름, 웹사이트, 투자자 정보 등을 입력
3. `python main.py` 실행

### 출력 결과

실행이 완료되면 `projects/프로젝트명/` 폴더에 다음 파일들이 생성됩니다:
- `p1_모델명.md`: 첫 번째 프롬프트 결과
- `p2_모델명.md`: 두 번째 프롬프트 결과
- `final_모델명.md`: 최종 결과
- `live_logs/모델명.log`: 실시간 처리 로그

## 의존성 및 요구사항

### Python 버전
- Python 3.8 이상

### 주요 라이브러리
- `openai`: OpenRouter API 통신
- `aiohttp`: 비동기 HTTP 요청
- `python-dotenv`: 환경 변수 관리
- `tenacity`: API 재시도 로직

### API 요구사항
- OpenRouter API 키 필요
- 인터넷 연결 필수

## 문제 해결 (FAQ)

### Q: API 키 오류가 발생합니다
A: `.env` 파일에 `OPENROUTER_API_KEY`가 올바르게 설정되었는지 확인하세요.

### Q: 특정 모델이 작동하지 않습니다
A: `ai_models.txt`의 모델 ID가 정확한지 확인하세요. OpenRouter에서 지원하는 모델 목록을 확인하세요.

### Q: 파일 첨부가 작동하지 않습니다
A: 파일 경로가 정확한지, 파일이 존재하는지 확인하세요. 상대 경로는 프로젝트 루트 기준입니다.

### Q: 메모리 부족 오류가 발생합니다
A: 동시에 실행하는 모델 수를 줄이거나, 더 작은 모델을 사용하세요.

---

### DEV.md

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

## 영문 버전

### README.md

# AI-Forge: AI Workflow Orchestrator

A framework that executes multiple AI models concurrently and automates complex AI collaboration workflows with a single prompt file.

## Key Features

- **Parallel Multi-AI Processing**: Execute the same task across multiple AI models simultaneously to reduce processing time
- **Prompt-Driven Workflow**: Define entire workflows using markdown files
- **AI Collaboration**: Enhance results by allowing AIs to reference responses from previous steps
- **Multimodal Input**: Pass images, PDFs, code, and documents directly to AI
- **Real-time Log Monitoring**: Track each AI's progress in real-time

## Installation Guide

### 1. Clone Repository
```bash
git clone https://github.com/your-username/ai-forge.git
cd ai-forge
```

### 2. Set Up Python Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment
```bash
cp .env.example .env
```

Open `.env` file and enter your OpenRouter API key:
```
OPENROUTER_API_KEY=your_api_key_here
```

### 5. Configure AI Models
Add models to `ai_models.txt`, one per line:
```
google/gemini-2.0-flash-thinking-exp:free
anthropic/claude-3.5-sonnet
openai/gpt-4-turbo
```

## Usage and Examples

### Basic Execution
```bash
python main.py
```

When executed, you'll see:
1. Language selection (Korean/English)
2. Bot mode selection (Standard research bot/Custom prompt)

### Command Line Options
```bash
# Specify language and prompt file directly
python main.py --lang en --prompt my_custom.md

# Disable AI collaboration
python main.py --no-collaboration

# Specify PDF processing engine
python main.py --pdf-engine mistral-ocr
```

### Writing Prompt Files

Prompt files should be written as `.md` files in the `prompts/` folder.

#### Basic Structure
```markdown
## project name ##
My Project Name

## system prompt ##
You are a professional analyst. Provide accurate and detailed analysis.

## prompt1: First Task ##
# reasoning
Collect and analyze basic information about the project.

## prompt2: Second Task ##
# other_ai_info
Perform in-depth analysis based on previous analysis.
```

#### Special Tags

1. **`# reasoning`**: Records AI's thinking process in logs
2. **`# other_ai_info`**: References other AI responses from previous steps
3. **File Attachment Tags**:
   - `# img: path/to/image.jpg` - Attach image
   - `# pdf: path/to/document.pdf` - Attach PDF
   - `# code: path/to/script.py` - Attach code file
   - `# doc: path/to/readme.md` - Attach document file

### Default Example: research.md

`prompts/research.md` is the default template for project analysis:

```markdown
## project name ##
GTE

## system prompt ##
You are a professional blockchain project analyst...

## prompt1: In-depth Analysis and Report ##
# reasoning
**project info**
GTE
• One-liner: Decentralized trading platform
• Tag: DeFi, DEX
• web: https://www.gte.xyz/
...
**end of project info**
```

To use this example:
1. Replace content between `**project info**` and `**end of project info**` with your project's information
2. Enter project name, website, investor information, etc.
3. Run `python main.py`

### Output Results

Upon completion, the following files are created in `projects/project_name/`:
- `p1_modelname.md`: First prompt results
- `p2_modelname.md`: Second prompt results
- `final_modelname.md`: Final results
- `live_logs/modelname.log`: Real-time processing logs

## Dependencies and Requirements

### Python Version
- Python 3.8 or higher

### Main Libraries
- `openai`: OpenRouter API communication
- `aiohttp`: Asynchronous HTTP requests
- `python-dotenv`: Environment variable management
- `tenacity`: API retry logic

### API Requirements
- OpenRouter API key required
- Internet connection required

## Troubleshooting (FAQ)

### Q: I'm getting API key errors
A: Ensure `OPENROUTER_API_KEY` is correctly set in your `.env` file.

### Q: A specific model isn't working
A: Verify the model ID in `ai_models.txt` is correct. Check OpenRouter's supported models list.

### Q: File attachments aren't working
A: Check that file paths are correct and files exist. Relative paths are based on project root.

### Q: I'm getting out of memory errors
A: Reduce the number of concurrent models or use smaller models.

---

### DEV.md

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