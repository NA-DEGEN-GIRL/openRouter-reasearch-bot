2025-07-18 10:22:10
알겠습니다. 기술 문서 작성가로서, 사용자와 개발자를 위한 명확하고 상세한 문서를 작성하겠습니다.

---
### **한글 버전 (Korean Version)**
---

### `README.md`

# AI-Forge: AI 워크플로 오케스트레이터

**다양한 AI 모델을 병렬 실행하고, 프롬프트 설계만으로 AI 협업, 코드 개선, 멀티모달 분석을 자동화하는 프레임워크입니다.**

## ✨ 주요 기능

-   **다중 AI 병렬 처리**: `ai_models.txt`에 명시된 모든 AI 모델에 작업을 동시에 분산하여 처리 속도를 극대화합니다.
-   **프롬프트 기반 워크플로**: 코드를 수정할 필요 없이, `prompts/` 폴더 안의 마크다운 파일 하나로 전체 작업 흐름(분석, 협업, 출력 형식 등)을 자유롭게 설계하고 제어할 수 있습니다.
-   **구조적 데이터 협업**: AI가 생성한 JSON 형식의 구조화된 데이터를 다음 단계의 AI가 참고하여, 단순 텍스트 전달 방식보다 훨씬 안정적이고 정확한 협업이 가능합니다. (`#other_ai_info` 태그 활용)
-   **멀티모달 입력 지원**: 프롬프트 파일 내에서 `#img`, `#pdf`, `#code` 태그를 사용하여 이미지, PDF, 코드 파일을 AI에게 직접 전달하고 분석시킬 수 있습니다.
-   **실시간 로그 모니터링**: 메인 프로세스와 별도로, 각 모델의 실시간 작업 과정(`reasoning` 포함)을 로그 파일로 확인할 수 있습니다.

## 💾 설치 가이드 (Installation)

### 1. 저장소 복제

```bash
git clone https://github.com/Your-Username/AI-Forge.git
cd AI-Forge
```

### 2. 필요 라이브러리 설치

```bash
pip install -r requirements.txt
```

### 3. 환경 변수 설정

`.env.example` 파일을 복사하여 `.env` 파일을 생성합니다.

```bash
cp .env.example .env
```

생성된 `.env` 파일을 열고, OpenRouter API 키를 입력합니다.

```sh
# .env
OPENROUTER_API_KEY="sk-or-v1-..."
```

### 4. AI 모델 목록 설정

`ai_models.txt` 파일을 열고, 사용하고 싶은 AI 모델의 ID를 한 줄에 하나씩 입력합니다. (예: `google/gemini-flash-1.5`)

## 🚀 사용법 및 예시 (Usage & Example)

### 기본 실행

터미널에서 아래 명령어를 실행하면, 대화형 모드를 통해 언어와 실행할 프롬프트를 선택할 수 있습니다.

```bash
python main.py
```

### 특정 프롬프트 지정 실행

`--lang`과 `--prompt` 옵션을 사용하여 특정 프롬프트 파일을 즉시 실행할 수 있습니다.

```bash
# research_ko.md 프롬프트를 한국어로 실행
python main.py --lang ko --prompt research.md
```

### 프롬프트 파일 설계 (`prompts/research.md` 예시)

이 프레임워크의 모든 동작은 `prompts/` 폴더 안의 `.md` 파일로 제어됩니다. 모든 프롬프트 파일은 아래와 같은 규칙을 따라야 합니다.

-   **`## project name ##`**: 작업의 고유 이름. 결과물이 저장될 폴더명으로 사용되므로 **반드시 파일 최상단에 작성해야 합니다.**
-   **`## system prompt ##`**: 모든 AI 모델에게 공통적으로 적용될 시스템 지침(역할, 톤앤매너 등)입니다.
-   **`## promptN: [설명] ##`**: 순차적으로 실행될 작업 단계를 정의합니다. `N`은 실행 순서를 나타내는 숫자입니다.

```markdown
## project name ##
My Awesome Project

## system prompt ##
당신은 최고의 분석가입니다.

## prompt1: [1단계: 정보 수집] ##
# reasoning
# img: path/to/your/image.jpg
# pdf: path/to/your/document.pdf
# code: path/to/your/code.py
[프롬프트 상세 지시사항...]

## prompt2: [2단계: 교차 검증] ##
# other_ai_info
[프롬프트 상세 지시사항...]
```

#### **옵션 태그 상세 설명**

-   `# reasoning`: AI의 생각 과정을 로그 파일에 기록하여 디버깅을 용이하게 합니다.
-   `# other_ai_info`: 이전 단계(`prompt1`)에서 다른 AI들이 생성한 답변을 현재 AI(`prompt2`)가 참고하도록 합니다.
-   `# img: [경로]`, `# pdf: [경로]`, `# code: [경로]`: 해당 경로의 파일을 프롬프트에 첨부합니다. 로컬 경로 및 URL을 지원합니다.

## 🛠️ 의존성 및 요구사항

-   Python 3.8 이상
-   주요 라이브러리: `openai`, `aiohttp`, `python-dotenv`, `tenacity` (자세한 내용은 `requirements.txt` 참고)

## ❓ 문제 해결 (FAQ)

-   **Q: `OPENROUTER_API_KEY not found` 오류가 발생합니다.**
    -   A: 프로젝트 최상위 디렉토리에 `.env` 파일이 있는지, 파일 내에 `OPENROUTER_API_KEY`가 올바르게 입력되었는지 확인해주세요.
-   **Q: `File not found` 오류가 발생하며 프롬프트 파일을 찾지 못합니다.**
    -   A: 실행하려는 프롬프트 파일이 `prompts/` 디렉토리 안에 있는지 확인해주세요.
-   **Q: AI가 응답을 생성하지 못하거나 오류를 반환합니다.**
    -   A: `ai_models.txt`에 입력한 모델 ID가 올바른지, 해당 모델이 OpenRouter에서 사용 가능한 상태인지 확인해주세요.

---

### `DEV.md`

# AI-Forge 개발자 문서

이 문서는 AI-Forge의 아키텍처, 설계 결정, 그리고 향후 확장 가이드를 제공합니다.

## 1. 아키텍처 개요

AI-Forge는 **관심사 분리(SoC)** 원칙에 따라 설계된 모듈형 아키텍처를 채택했습니다. 각 컴포넌트는 명확한 단일 책임을 가지며(SRP), 이를 통해 시스템의 안정성, 테스트 용이성, 확장성을 확보했습니다.

-   **설정(Config)과 실행 문맥(Context)의 분리**:
    -   `Config`: 실행 전 고정되는 불변 설정 (API 키, 모델 목록 등)
    -   `ProjectContext`: 워크플로 실행 중 생성되는 가변 상태 (프로젝트 이름, 출력 경로 등)
-   **엔진과 서비스의 분리**:
    -   `WorkflowEngine`: 전체 작업 흐름을 지휘하는 중앙 오케스트레이터.
    -   `Services`: 특정 작업을 수행하는 독립적인 서비스들 (API 통신, 파일 처리, 결과 저장 등).

  <!-- 실제 다이어그램 URL로 교체 필요 -->

## 2. 디렉토리 구조 설명

```
.
├── config/       # 환경 설정 및 상수 관리
├── core/         # 애플리케이션 핵심 로직 (엔진, 데이터 모델)
├── services/     # 외부 서비스 연동 및 특정 유틸리티 기능
├── utils/        # 로깅 등 범용 유틸리티
├── prompts/      # 워크플로를 정의하는 .md 파일 저장소
└── projects/     # AI가 생성한 결과물이 저장되는 곳
```

## 3. 핵심 컴포넌트 상세

### `core/engine.py` - WorkflowEngine

-   **역할**: 전체 워크플로의 실행을 총괄하는 중앙 관제탑.
-   **주요 책임**:
    -   설정 및 서비스 초기화.
    -   프롬프트 파일 파싱 및 실행 순서 관리.
    -   각 AI 클라이언트에 대한 병렬 작업 생성 및 실행.
    -   실행 결과 취합 및 다음 단계로의 전달.
-   **코드 스니펫**:
    ```python
    # core/engine.py
    class WorkflowEngine:
        async def run(self):
            await self._initialize_project()
            self._print_startup_info()
            await self._execute_workflow()
            self._print_completion_info()

        async def _execute_single_prompt(self, prompt: Prompt, is_last: bool):
            tasks = [
                self._process_model_task(client, prompt, is_last)
                for client in self.ai_clients.values()
            ]
            results = await asyncio.gather(*tasks, return_exceptions=True)
            # ... 결과 처리
    ```

### `services/ai_client.py` - AIModelClient

-   **역할**: 단일 AI 모델과 OpenRouter API 간의 통신을 전담.
-   **주요 책임**:
    -   API 요청 메시지 생성 (시스템 프롬프트, 히스토리 포함).
    -   API 스트리밍 응답 처리.
    -   대화 히스토리 관리.
-   **코드 스니펫**:
    ```python
    # services/ai_client.py
    class AIModelClient:
        async def get_response_stream(self, content: Any, use_reasoning: bool) -> AsyncGenerator[str, None]:
            # ... API 요청 및 스트림 반환
    ```

### `services/result_handler.py` - ResultHandler

-   **역할**: 모든 파일 입출력(I/O) 작업을 처리.
-   **주요 책임**:
    -   출력 디렉토리 생성 및 정리.
    -   최종 및 중간 결과 파일 저장.
    -   실시간 로그 파일 생성 및 내용 추가.
-   **코드 스니펫**:
    ```python
    # services/result_handler.py
    class ResultHandler:
        def save_result(self, prompt_id: int, response: ModelResponse, is_final: bool):
            # ... 결과 파일 저장 로직
        
        def log_stream_chunk(self, model_nickname: str, chunk: str):
            # ... 로그 파일에 스트림 청크 추가
    ```

## 4. 설계 결정 및 트레이드오프

-   **왜 이 구조를 선택했는가?**
    -   초기 버전은 `Orchestrator` 클래스 하나에 너무 많은 책임(API 통신, 파일 I/O, 상태 관리)이 집중되어 있었습니다. 이는 **높은 결합도(High Coupling)**와 **낮은 응집도(Low Cohesion)**를 유발하여 작은 변경도 시스템 전체에 영향을 미칠 위험이 컸습니다.
    -   리팩토링된 현재 구조는 각 클래스가 하나의 명확한 책임을 갖도록 분리하여 **안정성**과 **유지보수성**을 극대화했습니다. 예를 들어, `AIModelClient`는 이제 API 통신만 신경 쓰면 되므로, 파일 저장 방식이 변경되어도 `AIModelClient` 코드는 수정할 필요가 없습니다.

-   **고려했던 대안들**:
    -   **단일 `Orchestrator` 클래스 유지**: 구현이 빠르지만 장기적으로 유지보수 비용이 급증하고 버그 발생 가능성이 높아 기각했습니다.
    -   **Circuit Breaker 패턴 도입**: API 안정성을 높이기 위해 고려했으나, 현재 `tenacity` 라이브러리를 통한 재시도(Retry) 로직만으로도 충분하다고 판단했습니다. 이는 오버엔지니어링을 피하기 위한 결정입니다.

-   **핵심 결정: 구조적 데이터 파이프라인**
    -   AI 간 협업 시, 단순 텍스트 대신 `PromptResult` 데이터 클래스를 통해 구조화된 JSON 데이터를 전달하도록 설계했습니다. 이는 AI가 이전 단계의 결과를 오해석할 가능성을 크게 줄여, 전체 워크플로의 **안정성**을 획기적으로 향상시키는 핵심적인 설계 결정입니다.

## 5. 리팩토링 히스토리

-   **초기 버전**: 단일 `Orchestrator` 클래스가 대부분의 로직을 처리하는 모놀리식 구조.
-   **1차 리팩토링 (책임 분리)**: `Orchestrator`의 책임을 `WorkflowEngine`, `ResultHandler`, `ProjectContext`로 분리하여 SRP(단일 책임 원칙)를 적용.
-   **2차 리팩토링 (데이터 파이프라인 강화)**: `PromptResult` 모델을 도입하여 AI 간 협업 시 JSON 데이터를 활용할 수 있도록 개선.

## 6. 외부 라이브러리

-   `openai`: OpenRouter의 API와 통신하기 위한 클라이언트. (대체: `httpx` 등을 이용한 직접 구현)
-   `aiohttp`: 모델 메타데이터를 비동기적으로 가져오는 데 사용.
-   `python-dotenv`: `.env` 파일에서 환경 변수를 로드.
-   `tenacity`: API 요청 실패 시 지수 백오프(exponential backoff)를 적용한 재시도를 간편하게 구현.

## 7. 향후 확장 가이드

-   **새로운 서비스 추가 (예: Slack 알림)**
    1.  `services/notification_service.py` 파일을 생성합니다.
    2.  `WorkflowEngine`의 `run` 메서드 마지막에 알림 서비스 호출 로직을 추가합니다.
-   **새로운 프롬프트 파일 명령어 추가 (예: `#db_query`)**
    1.  `config/constants.py`의 `FILE_COMMANDS` 딕셔너리에 새 명령어를 추가합니다.
    2.  `services/prompt_parser.py`의 `_extract_attachments` 메서드에 관련 로직을 추가합니다.
    3.  `services/file_handler.py`에 해당 명령어를 처리할 `_handle_db_query`와 같은 메서드를 구현합니다.

---
### **영문 버전 (English Version)**
---

### `README.md`

# AI-Forge: AI Workflow Orchestrator

**A framework that runs various AI models in parallel and automates AI collaboration, code improvement, and multimodal analysis, all through simple prompt design.**

## ✨ Key Features

-   **Concurrent Multi-AI Processing**: Maximizes processing speed by distributing tasks to all AI models specified in `ai_models.txt` simultaneously.
-   **Prompt-Driven Workflow**: Freely design and control the entire workflow—analysis, collaboration, output formats, etc.—with a single Markdown file in the `prompts/` folder, requiring no code changes.
-   **Structured Data Collaboration**: Enables more stable and accurate collaboration by allowing AIs to reference structured JSON data from previous steps, a significant improvement over plain text. (Utilizes the `#other_ai_info` tag).
-   **Multimodal Input Support**: Directly pass images, PDFs, and code files to the AI for analysis using `#img`, `#pdf`, and `#code` tags within your prompt files.
-   **Live Log Monitoring**: Separately monitor the real-time progress of each model, including its reasoning process, through dedicated log files.

## 💾 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Your-Username/AI-Forge.git
cd AI-Forge
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Copy the `.env.example` file to create a `.env` file.

```bash
cp .env.example .env
```

Open the newly created `.env` file and enter your OpenRouter API key.

```sh
# .env
OPENROUTER_API_KEY="sk-or-v1-..."
```

### 4. Configure AI Models

Open `ai_models.txt` and list the model IDs you want to use, one per line (e.g., `google/gemini-flash-1.5`).

## 🚀 Usage & Example

### Basic Execution

Run the following command in your terminal. You will be guided through an interactive mode to select the language and prompt.

```bash
python main.py
```

### Running a Specific Prompt

You can immediately execute a specific prompt file using the `--lang` and `--prompt` options.

```bash
# Run the research.md prompt in English
python main.py --lang en --prompt research_en.md
```

### Designing a Prompt File (Example: `prompts/research.md`)

All operations of this framework are controlled by `.md` files in the `prompts/` directory. Every prompt file must follow these rules:

-   **`## project name ##`**: A unique name for the task. It **must be the first section in the file** as it's used for the output folder name.
-   **`## system prompt ##`**: A common set of instructions (role, tone, etc.) applied to all AI models.
-   **`## promptN: [Description] ##`**: Defines a sequential step in the workflow. `N` is a number indicating the execution order.

```markdown
## project name ##
My Awesome Project

## system prompt ##
You are a top-tier analyst.

## prompt1: [Step 1: Information Gathering] ##
# reasoning
# img: path/to/your/image.jpg
# pdf: path/to/your/document.pdf
# code: path/to/your/code.py
[Detailed instructions for the prompt...]

## prompt2: [Step 2: Cross-Validation] ##
# other_ai_info
[Detailed instructions for the prompt...]
```

#### **Option Tag Details**

-   `# reasoning`: Logs the AI's thought process to a file, making debugging easier.
-   `# other_ai_info`: Allows the current AI (`prompt2`) to reference the responses generated by other AIs in the previous step (`prompt1`).
-   `# img: [path]`, `# pdf: [path]`, `# code: [path]`: Attaches the specified file to the prompt. Both local paths and URLs are supported.

## 🛠️ Dependencies & Requirements

-   Python 3.8 or higher
-   Key Libraries: `openai`, `aiohttp`, `python-dotenv`, `tenacity` (see `requirements.txt` for details).

## ❓ Troubleshooting (FAQ)

-   **Q: I'm getting an `OPENROUTER_API_KEY not found` error.**
    -   A: Please ensure that a `.env` file exists in the project's root directory and that `OPENROUTER_API_KEY` is correctly entered within it.
-   **Q: I get a `File not found` error for my prompt file.**
    -   A: Make sure the prompt file you are trying to run is located inside the `prompts/` directory.
-   **Q: An AI fails to generate a response or returns an error.**
    -   A: Check if the model ID in `ai_models.txt` is correct and that the model is currently available on OpenRouter.

---

### `DEV.md`

# AI-Forge Developer Documentation

This document provides an overview of the AI-Forge architecture, its design decisions, and a guide for future extensions.

## 1. Architecture Overview

AI-Forge adopts a modular architecture designed according to the **Separation of Concerns (SoC)** principle. Each component has a clear Single Responsibility (SRP), ensuring system stability, testability, and scalability.

-   **Separation of Config and Context**:
    -   `Config`: Immutable, pre-execution settings (API key, model list).
    -   `ProjectContext`: Mutable state generated during workflow execution (project name, output path).
-   **Separation of Engine and Services**:
    -   `WorkflowEngine`: The central orchestrator that directs the entire workflow.
    -   `Services`: Independent services that perform specific tasks (API communication, file handling, result persistence).

 <!-- Replace with actual diagram URL -->

## 2. Directory Structure

```
.
├── config/       # Manages environment configuration and constants
├── core/         # Core application logic (engine, data models)
├── services/     # Handles external service integrations and specific utilities
├── utils/        # General-purpose utilities like logging
├── prompts/      # Stores .md files that define workflows
└── projects/     # Where results generated by the AIs are saved
```

## 3. Core Component Details

### `core/engine.py` - WorkflowEngine

-   **Role**: The central control tower orchestrating the entire workflow execution.
-   **Key Responsibilities**:
    -   Initializing configuration and services.
    -   Parsing prompt files and managing the execution sequence.
    -   Creating and running parallel tasks for each AI client.
    -   Aggregating results and passing them to the next stage.
-   **Code Snippet**:
    ```python
    # core/engine.py
    class WorkflowEngine:
        async def run(self):
            await self._initialize_project()
            self._print_startup_info()
            await self._execute_workflow()
            self._print_completion_info()

        async def _execute_single_prompt(self, prompt: Prompt, is_last: bool):
            tasks = [
                self._process_model_task(client, prompt, is_last)
                for client in self.ai_clients.values()
            ]
            results = await asyncio.gather(*tasks, return_exceptions=True)
            # ... process results
    ```

### `services/ai_client.py` - AIModelClient

-   **Role**: Dedicated to handling all communication between a single AI model and the OpenRouter API.
-   **Key Responsibilities**:
    -   Creating API request messages (including system prompt and history).
    -   Processing API streaming responses.
    -   Managing conversation history.
-   **Code Snippet**:
    ```python
    # services/ai_client.py
    class AIModelClient:
        async def get_response_stream(self, content: Any, use_reasoning: bool) -> AsyncGenerator[str, None]:
            # ... API request and stream yielding logic
    ```

### `services/result_handler.py` - ResultHandler

-   **Role**: Manages all file Input/Output (I/O) operations.
-   **Key Responsibilities**:
    -   Creating and cleaning output directories.
    -   Saving final and intermediate result files.
    -   Creating and appending content to live log files.
-   **Code Snippet**:
    ```python
    # services/result_handler.py
    class ResultHandler:
        def save_result(self, prompt_id: int, response: ModelResponse, is_final: bool):
            # ... logic to save result file
        
        def log_stream_chunk(self, model_nickname: str, chunk: str):
            # ... append stream chunk to log file
    ```

## 4. Design Decisions and Trade-offs

-   **Why This Architecture?**
    -   The initial version concentrated too many responsibilities (API calls, file I/O, state management) into a single `Orchestrator` class. This led to **High Coupling** and **Low Cohesion**, creating a high risk that small changes could have system-wide effects.
    -   The refactored architecture isolates each class to a single, clear responsibility, maximizing **stability** and **maintainability**. For example, `AIModelClient` now only concerns itself with API communication; changes to the file saving logic will not require modifying `AIModelClient`.

-   **Alternatives Considered**:
    -   **Maintaining a Single `Orchestrator` Class**: While faster to implement initially, this approach was rejected because it would lead to soaring long-term maintenance costs and a higher likelihood of bugs.
    -   **Implementing a Circuit Breaker Pattern**: Considered for enhancing API stability, but the current retry logic using the `tenacity` library was deemed sufficient for the use case. This decision was made to avoid over-engineering.

-   **Key Decision: Structured Data Pipeline**
    -   We designed the system to pass structured JSON data via the `PromptResult` data class for AI collaboration, instead of just plain text. This was a critical design choice that dramatically reduces the chance of misinterpretation by AIs, thereby enhancing the **stability** of the entire workflow.

## 5. Refactoring History

-   **Initial Version**: A monolithic structure where a single `Orchestrator` class handled most of the logic.
-   **First Refactoring (Responsibility Separation)**: Applied the SRP by splitting the `Orchestrator`'s responsibilities into `WorkflowEngine`, `ResultHandler`, and `ProjectContext`.
-   **Second Refactoring (Data Pipeline Enhancement)**: Introduced the `PromptResult` model to enable the use of JSON data in AI collaboration.

## 6. External Libraries

-   `openai`: The client for communicating with OpenRouter's API. (Alternative: direct implementation using `httpx`).
-   `aiohttp`: Used for asynchronously fetching model metadata.
-   `python-dotenv`: Loads environment variables from `.env` files.
-   `tenacity`: Simplifies the implementation of retries with exponential backoff for failed API requests.

## 7. Future Extension Guide

-   **Adding a New Service (e.g., Slack notifications)**
    1.  Create a `services/notification_service.py` file.
    2.  Add a call to your notification service at the end of the `WorkflowEngine.run` method.
-   **Adding a New Prompt File Command (e.g., `#db_query`)**
    1.  Add the new command to the `FILE_COMMANDS` dictionary in `config/constants.py`.
    2.  Add the relevant logic to the `_extract_attachments` method in `services/prompt_parser.py`.
    3.  Implement a method like `_handle_db_query` in `services/file_handler.py` to process the command.