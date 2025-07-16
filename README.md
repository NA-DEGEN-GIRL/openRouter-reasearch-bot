# AI-Forge: AI Workflow Orchestrator

**여러 AI 모델을 동시에 실행하며, 프롬프트 설계와 첨부파일 선언만으로 AI 협업·멀티모달(이미지/문서 포함) 워크플로우를 자유롭게 구현하세요.**

---

## 🧠 한글 안내

OpenRouter 기반 LLM들을 prompts/의 마크다운 프롬프트(.md) 설계,  
이미지/PDF 첨부(line 단위 # img / # pdf) 선언,  
교차 reasoning 및 파일 로깅,  
파일/섹션 "비활성화(deactive)" 등  
모든 최신 멀티모달 기능을 함께 지원하는 CLI 파이프라인 자동화 플랫폼입니다.

---

### ✨ 최신 주요 특징

- **다중 AI 동시 실행:** ai_models.txt에 입력한 모델 모두 병렬 처리
- **프롬프트/첨부 기반 자동화:** prompts/ 폴더 `.md`에 원하는 분석, 검증, 이미지/PDF 첨부 `# img`, `# pdf` 라인만 추가하면 멀티모달 입력 자동 구현
- **Multimodal options 예시:**
    ```
    # img ./images/example.jpg
    # pdf ./docs/whitepaper.pdf
    ```
- **AI 협업 옵션:** `# reasoning`, `# other_ai_info` 태그로 reasoning 노출, 다른 AI 답변 참고 등 고급 워크플로 구축
- **비활성화 섹션:** `## deactive`로 시작하면 해당 섹션은 분석에서 자동으로 skip
- **PDF 플러그인 엔진 선택:** (`--pdf-engine pdf-text` 등) 모델별 PDF 처리방법 세밀 제어 가능
- **실시간 로그 모니터링:** view_log.py로 AI 별 reasoning/진행 상황 실시간 확인
- **파일 체크/경고:** 이미지/PDF 파일 경로 오류 시 경고 메시지로 안내

---

### 🚀 빠른 시작 (Quick Start)

1. 환경설정
    ```bash
    git clone https://github.com/NA-DEGEN-GIRL/openRouter-ai-forge.git
    cd openRouter-ai-forge
    pip install -r requirements.txt
    cp copy.env .env      # API KEY 입력
    ```
2. 모델 선택 및 프롬프트 관리  
    ```
    python utils/search_ai_models.py
    ```
    - ai_models.txt(한 줄씩)
    - .md 프롬프트(modal, research 등)는 반드시 prompts/ 폴더(및 하위 디렉토리)에 위치

3. 실행 예시
    ```bash
    python main.py
    python main.py --lang en --prompt research_en.md
    python main.py --pdf-engine mistral-ocr --prompt myflow.md
    ```

4. 실시간 reasoning 로그 확인 (선택)
    ```
    python view_log.py
    ```

---

### 📦 prompts/ 및 프롬프트/첨부파일 설계 규칙

- prompts/ 하위에 .md 파일로 워크플로 작성
- 각 프롬프트에
    - `# img [이미지경로 or URL]` : 이미지 첨부
    - `# pdf [파일경로]` : PDF 첨부
    - `# reasoning`, `# other_ai_info` : 옵션 태그
- 주석줄/첨부줄/옵션줄은 실행 시 본문에서 자동 제거되어 오염 무방
- `## deactive`로 시작하는 섹션은 완전히 무시됨(분석/실행/로그 해당없음)
- prompts/ 하위에 폴더/파일 자유롭게(예: prompts/myset/mycase.md 사용 가능)

---

#### 👇 주요 예시

```markdown
## project name ##
SampleProj

## prompt1: 정보분석 ##
# reasoning
# img images/logo.png
# pdf docs/whitepaper.pdf
간단한 분석 요청...

## prompt2: 요약 ##
# other_ai_info
이전답변 참고하여 요약...

## deactive 실험용JSON ##
실행되지 않음
```

---

## 🗂️ 주요 파일 구조

```
/
├── main.py                # 메인(멀티모달 오케스트레이터)
├── view_log.py            # 실시간 reasoning 로그뷰어
├── localization.py        # 다국어/다언어 메시지
├── utils/
│   └── search_ai_models.py  # 모델/스펙 검색, ai_models.txt 생성
├── ai_models.txt          # 모델ID 단일 목록
├── requirements.txt
├── copy.env
└── prompts/
    ├── research.md     # 한글 예시
    ├── research_en.md  # 영어 예시
    └── sub/anycase.md  # 하위폴더 사용 가능
```

---

# AI-Forge: AI Workflow Orchestrator (English)

**Control all your multi-AI, multimodal analysis via prompt design—attach images, PDFs, specify reasoning/logging, deactivate with a single marker.**

---

### ✨ Key Features

  * **Parallel multi-model:** All listed models process in parallel
  * **Prompt-driven, declarative workflow:** All .md prompts and attachments must live under the prompts/ folder and are parsed automatically
  * **Multimodal support:** Use `# img [path or URL]` or `# pdf [path]` in the prompt—auto-attached to AI input (images, PDFs)
  * **Customization:**
    - `# reasoning` tag: enables reasoning process log
    - `# other_ai_info` tag: referencing prior AI outputs for cross-check/merging logic
    - PDF parsing engine (--pdf-engine) argument at runtime
  * **Section deactivation:** `## deactive` disables sections on execution/logging
  * **Dynamic, flexible foldering:** prompts/ and all subfolders are supported (ex: prompts/subfolder/myflow.md)
  * **Attachment warnings:** Nonexistent image or PDF files produce visible warnings

---

**Prompt Example:**
```markdown
## project name ##
MyProject

## prompt1: Info Analysis ##
# reasoning
# img images/test1.png
# pdf docs/whitepaper.pdf
Prompt text here...

## prompt2: Summary ##
# other_ai_info
Prompt text...

## deactive Archive Step ##
(This section is ignored)
```

---

### 🗂️ File Structure

```
/
├── main.py
├── view_log.py
├── localization.py
├── utils/
│   └── search_ai_models.py
├── ai_models.txt
├── requirements.txt
├── copy.env
└── prompts/
    ├── research.md
    ├── research_en.md
    └── [subfolders/additional-prompts].md
```