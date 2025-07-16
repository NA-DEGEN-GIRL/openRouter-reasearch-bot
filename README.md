# AI-Forge: AI Workflow Orchestrator

**여러 AI를 동시에 협업/병렬 실행, 이미지를 비롯한 멀티모달 입력까지 단 하나의 프롬프트 설계로 자동화하는 OpenRouter 기반 워크플로 프레임워크**

---

## 🧠 한글 안내

OpenRouter 기반 LLM들을 prompts/ 폴더의 .md 프롬프트,  
최신 멀티모달 첨부(# img, # pdf) 및 reasoning/협업 옵션 태그,  
"비활성화(deactive)"로 섹션 관리까지 모두 CLI에서 자동화할 수 있습니다.

---

### ✨ 주요 특징

- ai_models.txt에 명시된 모델들로 **동시 병렬 분석**
- prompts/ 폴더 .md 프롬프트 설계 하나로 워크플로/분석/검증/창작/합의까지 전체 설계
- 실시간 reasoning/진행 로그(view_log.py)
- 이미지/PDF 첨부하면 자동으로 AI multimodal 입력 변환
- prompts/ 어디든 하위폴더/여러 파일/블록 지정 가능
- **비활성(deactive) 헤더로 실행에서 자유롭게 단계/파일 제외**

---

## 🚀 실행/설정 (Quick Start)

```bash
git clone https://github.com/NA-DEGEN-GIRL/openRouter-ai-forge.git
cd openRouter-ai-forge
pip install -r requirements.txt
cp copy.env .env   # API키 입력
```
모델 탐색/지정:  
```
python utils/search_ai_models.py
```

프롬프트(.md)는 반드시 prompts/ 하위에 배치(폴더 가능)  
```bash
python main.py
python main.py --lang en --prompt research_en.md
python main.py --pdf-engine mistral-ocr --prompt myflow.md
```

실시간 reasoning 확인:
```
python view_log.py
```

---

## 🏷️ 프롬프트 헤더/옵션 태그 사용법 (중요!)

### 📌 헤더(블록) 구분 규칙

- 모든 프롬프트는 `## ... ##`로 구간(header/블록)을 나누며,  
   - **`## project name ##`**: 프롬프트 파일 최상단(결과 폴더명이 됨)
   - **`## promptN: ... ##`**: 워크플로 단계(번호+설명 자유). 번호(1~)에 의해 순서 적용
   - **`## deactive: ... ##`**: 헤더만 `deactive:`로 시작하면 파일/단계 무시(실행/로그 모두 해당 없음), 반드시 ##로 구간을 감싸야 함

- 헤더마다 줄바꿈 뒤로 (본문, 옵션 태그, 첨부파일선언 등 자유롭게 배치)
- prompts/ 내 하위폴더에도 지원

**예시**
```markdown
## project name ##
MyProject

## prompt1: 초기분석 ##
# reasoning
# img ./imgs/pic.png
분석 본문 ...

## prompt2: 종합 ##
# other_ai_info
종합 내용...

## deactive: 테스트 ##
테스트 블록(실행 안 됨)
```

---

### 📌 [중요] 옵션 태그/첨부파일 기능 안내

각 헤더(프롬프트 단계) 하단에 줄바꿈으로 추가, 원하는 만큼 조합/복수 적용 가능

- `# reasoning`:  
  해당 AI가 각 프롬프트에 대해 reasoning(추론과정)을 실시간 로그와 파일에 남깁니다.
- `# other_ai_info`:  
  현재 단계의 AI가 타 AI의 이전답변을 참고해 협업/교차/최종 합의 분석을 자동으로 진행합니다.
- `# img [경로/URL]`:  
  해당 이미지 파일 (로컬 경로 or URL) 첨부, multimodal/비전 처리가 지원되는 모델은 자동 분석 (예: # img images/graph.png)
- `# pdf [경로]`:  
  첨부 PDF문서 기반 요약/질문/OCR 등 분석

*이 모든 태그/첨부파일 선언 줄은 실제 프롬프트로 AI에 전달되는 내용에서는 자동 제거되어 프롬프트 오염이 없습니다.*

---

## 🗂️ 주요 파일 구조

```
/
├── main.py                # 메인(오케스트레이터)
├── view_log.py            # 실시간 log viewer
├── localization.py        
├── utils/
│   └── search_ai_models.py
├── ai_models.txt          
├── requirements.txt
├── copy.env
└── prompts/
    ├── research.md     
    ├── research_en.md  
    └── anysubfolder/another.md
```

---

# AI-Forge: AI Workflow Orchestrator (English)

**Run multiple AIs in parallel, design complex collaborative/multimodal/automated AI workflows—with just prompt files and simple tag lines.**

---

### ✨ Key Features

- Multi-AI parallel execution specified in ai_models.txt
- **Prompt-driven, declarative workflow**: freely add/edit prompt `.md` files under prompts/ (supporting subfolders!)
- **Multimodal support**: Attach images (`# img path`) or PDFs (`# pdf path`) per prompt block
- Real-time log viewing (view_log.py): monitor each AI's progress stepwise
- **Section skipping**: Any section with header starting `## deactive: ... ##` (must use double hash both sides) is ignored (not executed or logged)
- Prompt files can be nested in subfolders under prompts/

---

### 🏷️ Prompt Header & Option Tag Use

**1. Section Headers**

- Every workflow is set with `## ... ##` double-sharp headers:
    - `## project name ##` (REQUIRED at file top; defines output directory name)
    - `## prompt1: ... ##`, `## prompt2: ... ##`, ... (prompt blocks, sequentially sorted by number)
    - `## deactive: ... ##` (skips that section entirely; must end with "##")

**2. Option Tags**

Each prompt step/block (immediately below the header, one per line):

- `# reasoning`: Log model's thinking/reasoning process stepwise
- `# other_ai_info`: Make this step use/merge other AIs’ prior answers
- `# img [file path or URL]`: Attach image (local file or http/https)
- `# pdf [file path]`: Attach PDF for document analysis

All tag lines and attachment lines are stripped from the AI's prompt.  
Prompt files can be placed anywhere under prompts/ (including subfolders); all major logic is controlled by header/option tags.

**Example**
```markdown
## project name ##
SampleProj

## prompt1: Initial analysis ##
# reasoning
# img ./imgs/logo.png
Prompt detail here...

## prompt2: Summary ##
# other_ai_info
Summary here...

## deactive: legacy step ##
(This section will be ignored)
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
    └── subfolder/other.md
```
---