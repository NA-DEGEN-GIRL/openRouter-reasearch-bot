# OpenRouter 기반 AI 멀티모델 자동 리서치 시스템

**이 프로젝트는 OpenRouter 플랫폼에서 제공하는 다양한 최신 AI 언어모델(LLM)을 활용하여, 블록체인/크립토 프로젝트 리서치를 자동화하는 시스템입니다.**

OpenRouter API를 통해 여러 AI 모델을 병렬 호출, 각 모델의 웹검색·심층 분석 기능, AI간 협업 및 결과 교차 검증, 구조화된 보고서 생성까지 전 과정을 단 한 번에 자동 처리합니다.

---

## 📝 시스템 설계 및 코드 자동화 방식 (code_instruction.txt 참고)

이 프로젝트의 전체 설계와 소스코드는 `code_instruction.txt`라는 상세 요구사양서를 기반으로 대형 언어모델(LLM, 예: GPT-4, Claude 등)을 사용해 자동 생성되었습니다.  
즉, code_instruction.txt 파일은 기획서이자 "LLM에 입력하는 프롬프트"로, 아래와 같은 방식으로 동작합니다.

- **code_instruction.txt**에 시스템 목표, 파일구조, 로직, 예외처리, 결과물 형태 등을 상세히 작성
- 이 프롬프트를 OpenRouter 등 LLM에 입력하면, LLM이 본 저장소(코드, 문서, 워크플로)를 자동 생성하도록 설계됨
- 개발자 누구나 code_instruction.txt를 사용해 동일/유사 시스템을 재현, 확장, 커스터마이즈 가능

**즉, 본 프로젝트는 사람이 직접 코딩한 것이 아니라, 명확한 instruction 기반의 LLM 코드 auto-generation 방식을 적극 활용한 사례입니다.**

---

## 주요 파일 설명

- **research_bot.py**
  - 리서치 자동화 워크플로를 담당. 여러 AI 모델에 프롬프트를 병렬로 전달, 각 답변/Reasoning을 실시간 기록, 여러 프롬프트를 순차적으로 처리
  - AI 간 협업(다른 모델 답변을 참고함) 지원
  - 각 프롬프트 결과 및 실시간 로그를 `/projects/[프로젝트명]/` 내부에 저장
- **view_log.py**
  - 실시간 각 모델의 Reasoning 및 결과 진행상황을 모니터링하는 터미널 뷰어
- **prompt.md / prompt_en.md**
  - (필수) 프로젝트 기본정보와 단계별 리서치 프롬프트 정의, 분석 포맷 예시까지 포함
- **ai_models.txt**
  - 사용할 AI 언어모델(OpenRouter ID) 정의. 한 줄에 하나씩
- **utils/search_ai_models.py**
  - OpenRouter에서 지원하는 모델 탐색 및 검색 툴
- **requirements.in**
  - 필요한 파이썬 패키지 집합
- **copy.env**
  - 환경변수 템플릿 (`OPENROUTER_API_KEY` 필요)

---

## 필수 준비 사항

1. **OpenRouter 회원가입** 및 API 키 발급 (https://openrouter.ai/)
2. `copy.env` → `.env` 복사 후 KEY 값 입력
3. `ai_models.txt` 모델 ID 한 줄씩 작성 (`utils/search_ai_models.py`로 탐색 지원)
4. 의존 패키지 설치  
   ```bash
   pip install -r requirements.in
   ```
5. `prompt.md` 또는 `prompt_en.md` 확인/작성

---

## 사용 방법

### 1. AI 모델 탐색 후 `ai_models.txt` 만들기  
```bash
python utils/search_ai_models.py       # 전체 모델 리스트
python utils/search_ai_models.py gpt   # 'gpt' 포함 모델만 검색
```
- 원하는 모델 ID를 `ai_models.txt`에 한 줄씩 작성

### 2. 리서치 봇 실행  
```bash
python research_bot.py
```
- 언어선택/프롬프트 자동감지 (혹은 옵션 명시)
- 결과 및 체계적 로그, 단계별 분석 출력

**협업형(모델 교차참조 Off) 실행:**  
```bash
python research_bot.py --no-collaboration
```

### 3. 실시간 Reasoning 모니터링  
```bash
python view_log.py
```
- 각 AI 모델의 reasoning 로그 스트리밍 확인

---

## 구조 및 결과물

- `projects/프로젝트명/final_MODEL.md`: 각 모델별 최종 분석 결과
- `projects/프로젝트명/live_logs/MODEL.log`: reasoning/진행 과정 로그
- 단계별 결과, 통합(병합) 결과, 구조화된 JSON, 다양한 형태의 보고서, 요약, 트윗 등 자동 생성

---

## 참고 및 고급 정보

- **code_instruction.txt**를 직접 읽어보면 설계 논리, 코드 자동생성 방식, 추가 사용법 등을 빠르게 파악할 수 있습니다.
- 영어권 개발자는 `code_instruction_en.txt`로 동일 컨셉과 코드를 생성할 수 있습니다.
- LLM 기반 자동화 방식 특성상, 재생산성/확장성이 뛰어나고, 프롬프트만 교체하면 다양한 리서치/AI 파이플라인 구현 가능

---

# Multi-model AI Research Automation System (Powered by OpenRouter)

**This project leverages various state-of-the-art AI models from the OpenRouter platform to fully automate blockchain/crypto project research.**

It orchestrates parallel LLM calls, web search, collaborative AI cross-referencing, deep-dive analysis, and multi-format report generation—in a single automated pipeline.

---

## 📝 Design Principle — Automated LLM Code Generation (see `code_instruction_en.txt`)

All system specifications, design principles, and source code in this repository were generated automatically by using a detailed prompt and blueprint defined in `code_instruction_en.txt` (English version of code_instruction).

- `code_instruction_en.txt` acts as the requirement prompt for large language models (LLMs). When input to an LLM on OpenRouter or similar, this prompt will produce the same (or extensible) code and project structure demonstrated here.
- This project stands as an example of using LLMs for precise, fast, and reproducible codebase generation—not hand-crafted, but fully instruction-driven.

**Feel free to examine or use `code_instruction_en.txt` as LLM input to recreate, extend, or adapt this system for your own workflow.**

---

## Main Files

- **research_bot.py**
  - Handles the research automation workflow. Sends prompts to multiple AI models in parallel, logs real-time reasoning, supports collaborative or single-model research, and saves results to `/projects/[ProjectName]/`
- **view_log.py**
  - Terminal-based real-time analyzer for per-model reasoning and progress logs
- **prompt.md / prompt_en.md**
  - (Required) Markdown with all project info, structured prompts, format examples
- **ai_models.txt**
  - Target AI model IDs (one per line); use `utils/search_ai_models.py` for discovery
- **utils/search_ai_models.py**
  - Tool for browsing and filtering OpenRouter-supported models
- **requirements.in**
  - Python pip dependencies
- **copy.env**
  - Template for environment variables (`OPENROUTER_API_KEY` needed)

---

## Prerequisites

1. OpenRouter account and API Key (https://openrouter.ai/)
2. Copy `copy.env` to `.env` and add your API key
3. Write model IDs to `ai_models.txt`
4. Install dependencies  
   ```bash
   pip install -r requirements.in
   ```
5. Prepare a project prompt (`prompt.md` or `prompt_en.md`)

---

## Usage

### 1. Search/select AI models for `ai_models.txt`
```bash
python utils/search_ai_models.py
python utils/search_ai_models.py gpt
```
- Copy the desired model IDs to `ai_models.txt` (one per line)

### 2. Run the research bot
```bash
python research_bot.py
```
- Automatic language detection/prompt file selection (or use options)
- All results, progress logs, and analyses saved systematically

**Disable collaboration:**  
```bash
python research_bot.py --no-collaboration
```

### 3. Monitor real-time reasoning
```bash
python view_log.py
```

---

## Output & Structure

- `projects/ProjectName/final_MODEL.md`: Final analysis per AI model
- `projects/ProjectName/live_logs/MODEL.log`: Reasoning/process log
- Stepwise outputs, merged reports, JSON, summaries, tweets—all automated

---

## Reference

- The actual design logic, code generation principles, and advanced usage can be quickly understood by reviewing `code_instruction_en.txt`.
- You may use or adapt the file as an LLM input to create your own version—extendable to other domains or research pipelines.