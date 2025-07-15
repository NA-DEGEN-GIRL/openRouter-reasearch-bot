# AI-Forge: AI Workflow Orchestrator

**여러 AI 모델을 동시에 실행하며, 프롬프트 설계만으로 AI 협업 워크플로를 자유롭게 구현하는 프레임워크입니다.**

OpenRouter 기반 LLM들을 사용자가 설계한 마크다운 프롬프트(`.md`) 시나리오대로 병렬 실행/교차 검증/협업/종합까지, 모든 과정을 CLI에서 자동화합니다.

> **Note:** 전체 코드는 `code_instruction.txt` 요구사양서를 기반으로 LLM과의 협업 방식으로 생성되었습니다.

---

## ✨ 주요 특징

- **다중 AI 병렬 처리:** `ai_models.txt`에 명시된 AI 모델에 동시에 작업 분산, 빠른 결과
- **프롬프트 기반 워크플로:** 코드 수정 없이, prompts/ 폴더 아래 `.md` 프롬프트 파일 수정/추가만으로 전체 워크플로를 설계/제어
- **AI 협업 옵션:** `# reasoning`, `# other_ai_info` 등 태그로 각 단계별 reasoning 공개, 타 AI의 답변 교차 참고/활용 지원
- **실시간 로그 시각화:** view_log.py로 모델별 진행 상황 reasoning 실시간 확인
- **확장성:** prompts/에 신규 프롬프트 파일만 추가하면 리서치, 번역, 창작, 리뷰, 자동 합의 등 원하는 어떤 AI 협업도 즉시 구현
- **모든 프롬프트는 prompts/ 폴더에 위치해야 하며, deactive:로 시작하는 프롬프트(예: ## deactive: ... ##)는 자동으로 무시되어 실행되지 않습니다.**
- **utils/ 폴더 제공:**  
    - `utils/search_ai_models.py`로 최신 지원 모델 탐색/필터/스펙 확인 가능

---

## 🚀 빠른 시작 (Quick Start)

1. 환경설정
    ```bash
    git clone https://github.com/NA-DEGEN-GIRL/openRouter-ai-forge.git
    cd openRouter-ai-forge
    pip install -r requirements.txt
    cp copy.env .env
    # .env 파일을 열고 OpenRouter API 키 입력
    ```

2. 모델 선정 및 프롬프트 준비
    ```
    python utils/search_ai_models.py
    ```
    - 모델 ID → ai_models.txt(한 줄씩)
    - 워크플로 설계/분석 시나리오는 반드시 prompts/ 폴더에 `.md` 파일로 저장

3. 실행
    ```bash
    python main.py
    # 언어/프롬프트 직접 지정 예시:
    python main.py --lang en --prompt research_en.md
    ```

4. 실시간 로그 (선택)
    ```
    python view_log.py
    ```

---

## ⚙️ 프롬프트 파일 설계 규칙 및 관리

- **모든 프롬프트 파일(.md)은 반드시 prompts/ 폴더 아래에 위치해야 하며**,  
  main.py 에서는 prompts/ 외부의 파일이나,  
  섹션 헤더가 `## deactive:`로 시작하는 구간(예: `## deactive:json merge##`)은 무시하고 읽지 않습니다.
- 섹션 비활성화(실행제외) 하고 싶으면 `## deactive: ... ##`로 헤더 타이틀을 시작하면 됨

**프롬프트 구조 예시:**
```markdown
## project name ##
MyProject

## prompt1: 리서치 ##
# reasoning
[프롬프트...]

## prompt2: 요약 ##
# other_ai_info
[프롬프트...]

## deactive: 구조화JSON ##   <-- 이 섹션은 실행되지 않음
[프롬프트...]
```

- `## project name ##`: 반드시 최상단, 결과물 폴더명 자동 지정
- `## promptN: [제목] ##`: 각 단계 여러 개 가능, 이름·순서 자유
- `# reasoning` 등 태그 활용 강력 (promptN 헤더 밑 한 줄에)
- prompts/ 아래 원하는 만큼 파일 추가, 필요 없는 단계/섹션은 그냥 deactive로 정의해 두어도 됨

---

## 🗂️ 주요 파일/폴더 구조

```
/
├── main.py                # 메인 실행/오케스트레이터
├── view_log.py            # 실시간 로그 뷰어
├── localization.py        # 다국어 UI 메시지
├── utils/
│   └── search_ai_models.py  # 모델 정보/추천/ai_models.txt 자동생성
├── ai_models.txt          # 사용할 모델ID(한 줄씩)
├── requirements.txt       # python dependency
├── copy.env               # 환경변수 템플릿
└── prompts/
    ├── research.md        # (한글) 예시/실제 프롬프트
    └── research_en.md     # (영문) 예시
    └── ...                # 커스텀 프롬프트 추가 가능
```

---

## 💡 활용 팁/참고

- prompts/에 deactive: prefix로 임시 블록/폐쇄 단계 넣을 수 있음(실행 제외)
- utils/search_ai_models.py 활용해 최신 모델/스펙 찾아 ai_models.txt 설계 추천
- 모든 파이프라인/협업/합의/분석/번역 등 설계의 유연성/확장성은 prompts/의 자유로운 커스텀 .md 파일 관리에 달림

---

# AI-Forge: AI Workflow Orchestrator (English)

**Orchestrate and automate any workflow with multiple AI models using only prompt file design.**

---

### ✨ Key Features

  * **Concurrent multi-AI processing:** Models listed in ai_models.txt all run simultaneously
  * **Prompt-driven workflow:** Design any automation by editing/adding .md prompt files in prompts/ (no code change needed)
  * **AI collaboration options:** Use tags like `# reasoning`, `# other_ai_info` directly in prompt steps for reasoning log or to enable referencing other AI's outputs
  * **Live log viewing:** view_log.py lets you stream real-time reasoning logs for any model as they operate
  * **Flexible extensions:** Add as many prompts as you want; write new .md files in prompts/ for any workflow—research, content, translation, review, etc.
  * **Prompt section “deactivation”:** Any prompt section header starting with `## deactive:` is skipped/ignored by main.py during execution—use to comment-out/deactivate steps without deleting them
  * **utils folder:**  
    - `utils/search_ai_models.py`: Discover/filter supported OpenRouter models and easily populate ai_models.txt

---

### ⚙️ How To Design Prompt Files

All prompt (.md) files **must be in the prompts/ directory** to be detected and used.  
Sections whose header starts with `## deactive:` are automatically ignored (not run); use this to disable phases you don’t want without deleting.

**Prompt example:**
```markdown
## project name ##
My Awesome Project

## prompt1: [Step 1] ##
# reasoning
...

## prompt2: [Step 2] ##
# other_ai_info
...

## deactive: Old JSON Output Step ##
...
```

- `## project name ##`: Must be first, sets output folder name
- `## promptN: ... ##`: Steps can have any title; number and sequence are flexible
- Section options:  
    - `# reasoning`: Forces reasoning process to be logged
    - `# other_ai_info`: This phase references prior AI outputs
- Add as many prompt templates/files in prompts/ as needed; deactivate steps using the `## deactive:` prefix when you want to leave them in but skip execution

---

### 🗂️ File Structure

```
/
├── main.py                # 메인 실행/오케스트레이터
├── view_log.py            # 실시간 로그 뷰어
├── localization.py        # 다국어 UI 메시지
├── utils/
│   └── search_ai_models.py  # 모델 정보/추천/ai_models.txt 자동생성
├── ai_models.txt          # 사용할 모델ID(한 줄씩)
├── requirements.txt       # python dependency
├── copy.env               # 환경변수 템플릿
└── prompts/
    ├── research.md        # (한글) 예시/실제 프롬프트
    └── research_en.md     # (영문) 예시
    └── ...                # 커스텀 프롬프트 추가 가능
```

---