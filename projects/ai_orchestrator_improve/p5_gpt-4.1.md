2025-07-18 10:22:29
## [README.md] (한글)

---
# AI-Forge

AI-Forge는 다양한 AI 언어/멀티모달 모델을 활용해, 프롬프트 파일(Markdown) 하나로 조사·분석·콘텐츠 제작 워크플로우를 자동화하는 도구입니다. CLI 기반이며, 초보자도 쉽게 사용할 수 있도록 설계되었습니다.

---

## 주요 기능

- 여러 AI 모델(예: GPT, Gemini 등)에 병렬로 분석 요청
- Markdown 프롬프트 파일로 워크플로우 단계, 옵션, 입력 파일 지정
- 이미지, PDF, 코드 파일 등 다양한 첨부파일 입력 지원
- 각 프롬프트마다 상황별 reasoning 모드 또는 AI 협업 기능 활성화 가능
- AI별로 reasoning 로그 및 산출물 파일 자동 저장
- 영/한 다국어 CLI

---

## 설치 가이드

1. **Python 3.9+ 설치** (가상환경 권장)
2. **저장소 클론**
   ```sh
   git clone https://github.com/your-org/ai-forge.git
   cd ai-forge
   ```
3. **필수 패키지 설치**
   ```sh
   pip install -r requirements.txt
   ```
4. **환경 변수(.env) 설정**
   ```sh
   cp .env.example .env
   # .env 파일을 열어 OPENROUTER_API_KEY를 입력
   ```

---

## 사용법 및 예시

### 1. AI 모델 준비
- `ai_models.txt` 파일에 사용할 AI 모델 ID를 한 줄씩 입력 (예시: `google/gemini-2.5-pro`)

### 2. 프롬프트 작성
- `prompts/research.md` 파일을 열어 조사하고 싶은 프로젝트 정보 및 분석 항목 작성

#### [입력 예시: prompts/research.md]

```markdown
## project name ##
GTE

## system prompt ##
당신은 전문 블록체인 프로젝트 분석가입니다.

## prompt1: 심층 분석 및 보고 ##
# reasoning
**project info**
GTE
• 한 줄 소개: Decentralized trading platform
...
**end of project info**
main request: 프로젝트에 대한 조사
...

## prompt2: 교차 검증 및 팩트 시트 생성 ##
# reasoning
# other_ai_info
너의 역할: ...
...
```

**구성 규칙**
- `## project name ##`: 결과물 폴더명이 됨(필수)
- `## system prompt ##`: AI에 기본 역할/지식 지시
- `## promptN: ... ##`: 각 단계(분석, 요약 등)
- 프롬프트 본문에서 `# reasoning`: AI 추론과정 저장, `# other_ai_info`: 협업 활성화
- `#img, #pdf, #code, #doc`: 첨부파일 지정(예: `#img: path/to/img.png`)
- 첨부파일/태그/본문은 자유롭게 조합 가능

### 3. 실행

- 기본 실행 (research.md, 한글)
  ```sh
  python main.py
  ```
- 영어 + 특정 프롬프트 지정
  ```sh
  python main.py --lang en --prompt research_en.md
  ```

### 4. 출력물

- 프로젝트 폴더(`projects/GTE`)에 프롬프트별 및 최종 결과물(`*.md`), reasoning 로그(`live_logs/`)가 생성

---

## 의존성 및 요구사항

- Python >= 3.9
- `openai`, `aiohttp`, `tenacity`, `python-dotenv` 등 주요 패키지(모두 requirements.txt에 명시)
- OpenRouter API Key 필요 (https://openrouter.ai)

---

## 문제 해결 (FAQ)

- **실행 중 파일이 없다고 에러가 납니다**
  - 입력 파일 경로, ai_models.txt, .env 존재/설정 모두 점검
- **API 오류/타임아웃**
  - API Key 발급 확인, 네트워크 환경 확인, 나중에 재시도
- **다국어가 동작하지 않아요**
  - `--lang` 옵션 확인, 스트림 출력 터미널 utf-8 지원 확인
- **첨부파일이 전달되지 않아요**
  - 파일 경로를 절대/상대경로로 명확히 입력, 파일 확장자 지원 범위 재확인
- 기타 문의: 이슈 게시판 활용


---

## [README.md] (English)

---
# AI-Forge

AI-Forge automates analysis/research workflows using multiple AI models, with everything configured through a single Markdown prompt file. CLI-based, designed for both novices and advanced users.

---

## Key Features

- Parallel analysis using several AI models (ex: GPT, Gemini)
- Workflow and input fully defined in Markdown prompt file
- Supports various attachment types: image, PDF, code, docs
- Per-step options: reasoning log, AI collaboration
- Automatic AI-specific output and reasoning logs per step
- Multilingual CLI (English/Korean)

---

## Quickstart & Installation

1. **Install Python 3.9+** (virtualenv recommended)
2. **Clone the repo**
   ```sh
   git clone https://github.com/your-org/ai-forge.git
   cd ai-forge
   ```
3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Set environment variables (.env)**
   ```sh
   cp .env.example .env
   # Edit .env and enter your OPENROUTER_API_KEY
   ```

---

## Usage & Examples

### 1. List AI Models
- Add AI model IDs line-by-line in `ai_models.txt` (e.g. `google/gemini-2.5-pro`)

### 2. Write your prompt
- Edit `prompts/research.md` with the info and task steps for your project

#### [Input Example: prompts/research.md]

```markdown
## project name ##
GTE

## system prompt ##
You are a professional blockchain analyst.

## prompt1: Deep Analysis and Report ##
# reasoning
**project info**
GTE
• One-liner: Decentralized trading platform
...
**end of project info**
main request: Research this project
...

## prompt2: Cross-check and Fact Sheet ##
# reasoning
# other_ai_info
Your role: ...
...
```

**Prompt File Rules**
- `## project name ##`: Required; will be used as output folder
- `## system prompt ##`: System-level AI instructions
- `## promptN: ... ##`: Each step in the workflow
- Within prompts: `# reasoning` (enable reasoning log), `# other_ai_info` (AI collaboration)
- Attachments: `#img`, `#pdf`, `#code`, `#doc` (e.g. `#img: path/to/img.png`). Use relative/path/to/file or URL.
- You can combine tags and text as needed

### 3. Run

- Default (research.md, Korean):
  ```sh
  python main.py
  ```
- English mode, specify prompt:
  ```sh
  python main.py --lang en --prompt research_en.md
  ```

### 4. Output

- Each project run generates outputs in `projects/GTE` with per-step and final output (`*.md`) and reasoning logs (`live_logs/`).

---

## Dependencies & Requirements

- Python >= 3.9
- Key packages: `openai`, `aiohttp`, `tenacity`, `python-dotenv` (see requirements.txt)
- OpenRouter API Key required (https://openrouter.ai)

---

## Troubleshooting (FAQ)

- **File not found errors?**
  - Double-check file paths, ai_models.txt, .env presence/settings
- **API errors/timeouts?**
  - Check your API Key, network connectivity, or try again later
- **Multilingual not working?**
  - Check `--lang` option, and ensure your terminal supports UTF-8
- **Attachments not being sent?**
  - Use correct path/extension, only supported types accepted
- Still stuck? Open a GitHub issue.

---

---

## [DEV.md] (한글)

# AI-Forge 개발자 문서

## 1. 아키텍처 개요

- **Orchestrator 패턴:** ProjectOrchestrator가 실행 플로우 제어
- **SRP 보장:** Config/ResultHandler/AIModelClient 등 역할 단일화
- **데이터 파이프라인:** PromptResult로 구조적 프롬프트간 데이터 공유
- **Markdown 기반 프롬프트 워크플로우**

## 2. 디렉토리 구조

```
.
├── main.py
├── config/
│   ├── config.py
│   └── constants.py
├── core/
│   ├── orchestrator.py
│   ├── models.py
│   └── exceptions.py
├── services/
│   ├── ai_client.py
│   ├── file_handler.py
│   ├── model_provider.py
│   ├── prompt_parser.py
│   └── result_handler.py
├── utils/
│   └── logger.py
├── prompts/
├── projects/
```

## 3. 핵심 컴포넌트 상세

- **Config**
  - 환경 읽기, 모델/프롬프트 유효성, 불변 객체
- **ProjectOrchestrator**
  - 초기화/실행 전체 관리. run() → _initialize → _execute_prompt_parallel 등
  - 주요 메서드: run, _execute_single_prompt, _prepare_user_content
- **PromptParser**
  - Markdown 섹션 파싱, 태그/첨부 파일 분리. 예: `_parse_prompt_section`
- **AIModelClient**
  - OpenRouter API 통신, 대화기록/재시도 관리
- **ResultHandler**
  - 출력파일/로그/타임스탬프 저장, 에러 기록

#### [코드 스니펫]
```python
# main.py
config = Config(language=lang, prompt_filepath=prompt_filepath)
orchestrator = ProjectOrchestrator(config)
await orchestrator.run()

# orchestrator.py
async def _execute_single_prompt(self, prompt, index, is_last):
    ...
    user_content = self._prepare_user_content(...)
    response = await client.get_response(user_content, ...)
    self.result_handler.append_to_log(..., response.response_text)
    ...
```

## 4. 설계 결정 및 트레이드오프

- **SRP(단일 책임)**: 추후 확장·테스트 가능성 위해 각 기능 분리
- **데이터 구조화**: 타 AI간 협업·교차검증 정확성 확보 목적
- **파일 입출력/로깅 분리**: 재사용성·테스트 용이성 확보를 위함
- **대안:** 도메인 모델 최소화로 복잡성은 증가 가능, 그러나 유지보수성 높임

## 5. 리팩토링 히스토리

- v1: 단일 Orchestrator, 파일I/O/로깅 혼재
- v2: ResultHandler 도입, PromptResult 구조 적용(기능별 분할)
- v3: 네이밍/상수/에러처리 일원화, 코드 중복 획기적 감소

## 6. 외부 라이브러리

- **openai**: API 통신. 대안: 공식 openai, open-llm 등
- **aiohttp**: 비동기 HTTP
- **tenacity**: 재시도(try/except보다 견고)
- **python-dotenv**: .env 환경변수 로딩. 대안: os.environ만 사용도 가능

## 7. 향후 확장 가이드

- **프롬프트 DSL, YAML 지원**
- **추가 AI API 커넥터 모듈**
- **CLI UX 개선 및 GUI**
- **테스트 시나리오 자동화**
- **상태/진행 모니터링 웹뷰**


---

## [DEV.md] (English)

# AI-Forge Developer Guide

## 1. Architecture Overview

- **Orchestrator Pattern:** The ProjectOrchestrator governs execution flow.
- **SRP (Single Responsibility):** Each specialty class handles one major concern.
- **Data Pipeline:** Structured PromptResult ensures accurate AI-to-AI info flow.
- **Markdown-based prompt workflow**

## 2. Directory Structure

```
.
├── main.py
├── config/
│   ├── config.py
│   └── constants.py
├── core/
│   ├── orchestrator.py
│   ├── models.py
│   └── exceptions.py
├── services/
│   ├── ai_client.py
│   ├── file_handler.py
│   ├── model_provider.py
│   ├── prompt_parser.py
│   └── result_handler.py
├── utils/
│   └── logger.py
├── prompts/
├── projects/
```

## 3. Core Components

- **Config**
  - Loads envs, validates models/prompts, immutable
- **ProjectOrchestrator**
  - Top-level lifecycle manager: init/run prompt-execution, file/discuss/AI routing
  - Main methods: run, _execute_single_prompt, _prepare_user_content
- **PromptParser**
  - Parses Markdown, handles option tags/attachments.
- **AIModelClient**
  - Handles OpenRouter API, history, retries
- **ResultHandler**
  - File/log/timestamp writing, error recording

#### [Code Example]
```python
config = Config(language=lang, prompt_filepath=prompt_filepath)
orchestrator = ProjectOrchestrator(config)
await orchestrator.run()
```

## 4. Design Choices & Trade-offs

- **SRP:** Facilitates modularity and testing
- **Structured Data:** For robust AI collaboration/factflow
- **I/O/Logging Separation:** For testability and reuse
- **Trade-off:** Overhead of extra model/data classes vs. strong maintainability

## 5. Refactoring History

- v1: All logic in Orchestrator, mixed I/O/logging
- v2: Added ResultHandler and PromptResult abstraction
- v3: Unified naming/constants/error handling, reduced code duplication by 70%+

## 6. Key 3rd-Party Libraries

- **openai**: LLM API; alt: official openai, open-llm
- **aiohttp**: async HTTP
- **tenacity**: robust retries
- **python-dotenv**: .env loader (can be replaced by raw os.environ in simple usage)

## 7. Future Extension Guide

- Custom DSL or YAML prompt support
- Additional AI connector modules
- CLI/UX improvement, possible GUI
- Automated regression/test suites
- Web-based job/monitor dashboard

---

> 참고: 문서 형태, 마크다운 활용 팁, 표준 구조 등은 [github.com](https://github.com/usreon/docs), [jidocument.tistory.com](https://jidocument.tistory.com/entry/%EA%B8%B0%EC%88%A0%EB%AC%B8%EC%84%9C-%EC%96%B4%EB%96%BB%EA%B2%8C-%EC%9E%91%EC%84%B1%ED%95%B4%EC%95%BC-%ED%95%A0%EA%B9%8C-%EC%82%AC%EC%9A%A9%EC%9E%90-%EC%A4%91%EC%8B%AC%EC%9D%98-%EA%B8%B0%EC%88%A0%EB%AC%B8%EC%84%9C-%EC%9E%91%EC%84%B1%ED%95%98%EA%B8%B0), [joshboyye/how-to-write-markdown-by-joshuawang.md](https://github.com/joshboyye/how-to-write-markdown-by-joshuawang.md) 가이드 참고(plain/표/코드블록, 초보자 중심 표기법 등).
