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

### 예시: research.md

`prompts/research.md`는 프로젝트 분석을 위한 기본 템플릿입니다:

```markdown
## project name ##
GTE

## metadata ##
- version: 001
- description: web3 프로젝트에 대한 조사

## system prompt ##
당신은 전문 블록체인 프로젝트 분석가입니다. 반드시 웹 검색을 통해 가장 정확한 최신 정보를 찾아야 합니다.

## prompt1: 심층 분석 및 보고 ##
# reasoning
# doc ./prompts/web3_projects/gte.md
현재단계: prompt1
project info: 첨부된 파일 (.md 혹은 .txt 파일)
main request: **project info** 프로젝트에 대한 조사
...
```

이 예시를 사용하려면:
1. doc 을 분석하려는 프로젝트 정보로 교체

   `gte.md` 파일 예시
   ```
   GTE
   • 한 줄 소개: Decentralized trading platform
   • Tag: DeFi, DEX, OrderBook DEX
   • web: https://www.gte.xyz/
   • X: https://x.com/gte_xyz
   💰 총 투자액: $25,000,000
   👑 Tier 1 투자자:
     - Paradigm
   🥂 Tier 2 투자자:
     - Robot Ventures, Wintermute
   🔹 기타 투자자:
     - Flow Traders, Guy Young, IMC Trading, Maven 11, Max Resnick
   Rootdata (https://www.rootdata.com/Projects/detail/GTE?k=MTQ4ODc=)
   팀원정보
   founder: https://x.com/0xBurbo
   co-founder: https://x.com/mlunghi2000
   co-founder: https://x.com/moses_gte
   co-founder: https://x.com/enzo_gte
   ```

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

# AI-Forge: AI Workflow Orchestrator

A framework for running multiple AI models simultaneously and automating complex AI collaboration workflows with a single prompt file.

## Key Features

- **Multi-AI Parallel Processing**: Request the same task to multiple AI models simultaneously to reduce processing time
- **Prompt-Based Workflow**: Define entire work flows using markdown files
- **AI Collaboration**: Reference previous AI responses in subsequent steps to improve results
- **Multimodal Input**: Directly send images, PDFs, code, and document files to AI
- **Real-time Log Monitoring**: Monitor each AI's work progress in real-time

## Installation Guide

### 1. Clone Repository
```bash
git clone https://github.com/your-username/ai-forge.git
cd ai-forge
```

### 2. Python Virtual Environment Setup (Recommended)
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

### 4. Environment Configuration
```bash
cp .env.example .env
```

Open the `.env` file and enter your OpenRouter API key:
```
OPENROUTER_API_KEY=your_api_key_here
```

### 5. AI Model Configuration
Add the models you want to use in the `ai_models.txt` file, one per line:
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

Running this will display the following selection screen:
1. Language selection (Korean/English)
2. Bot mode selection (Standard Research Bot/Custom Prompt)

### Command Line Options
```bash
# Directly specify language and prompt file
python main.py --lang en --prompt my_custom.md

# Disable AI collaboration
python main.py --no-collaboration

# Specify PDF processing engine
python main.py --pdf-engine mistral-ocr
```

### How to Write Prompt Files

Prompt files are written as `.md` files in the `prompts/` folder.

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

#### Special Tags Explained

1. **`# reasoning`**: Record AI's thought process in logs
2. **`# other_ai_info`**: Reference previous AI responses from other steps
3. **File attachment tags**:
   - `# img: path/to/image.jpg` - Attach image
   - `# pdf: path/to/document.pdf` - Attach PDF
   - `# code: path/to/script.py` - Attach code file
   - `# doc: path/to/readme.md` - Attach document file

### Example: research.md

`prompts/research.md` is a basic template for project analysis:

```markdown
## project name ##
GTE

## metadata ##
- version: 001
- description: Research on web3 project

## system prompt ##
You are a professional blockchain project analyst. You must find the most accurate and up-to-date information through web searches.

## prompt1: In-depth Analysis and Reporting ##
# reasoning
# doc ./prompts/web3_projects/gte.md
Current stage: prompt1
project info: Attached file (.md or .txt file)
main request: Research on **project info** project
...
```

To use this example:
1. Replace the doc with project information you want to analyze

   Example `gte.md` file:
   ```
   GTE
   • One-line description: Decentralized trading platform
   • Tag: DeFi, DEX, OrderBook DEX
   • web: https://www.gte.xyz/
   • X: https://x.com/gte_xyz
   💰 Total Investment: $25,000,000
   👑 Tier 1 Investors:
     - Paradigm
   🥂 Tier 2 Investors:
     - Robot Ventures, Wintermute
   🔹 Other Investors:
     - Flow Traders, Guy Young, IMC Trading, Maven 11, Max Resnick
   Rootdata (https://www.rootdata.com/Projects/detail/GTE?k=MTQ4ODc=)
   Team Information
   founder: https://x.com/0xBurbo
   co-founder: https://x.com/mlunghi2000
   co-founder: https://x.com/moses_gte
   co-founder: https://x.com/enzo_gte
   ```

2. Enter project name, website, investor information, etc.
3. Run `python main.py`

### Output Results

Upon completion, the following files will be generated in the `projects/ProjectName/` folder:
- `p1_ModelName.md`: First prompt results
- `p2_ModelName.md`: Second prompt results
- `final_ModelName.md`: Final results
- `live_logs/ModelName.log`: Real-time processing logs

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
- Internet connection essential

## Troubleshooting (FAQ)

### Q: API key error occurs
A: Check if `OPENROUTER_API_KEY` is correctly set in the `.env` file.

### Q: A specific model doesn't work
A: Verify that the model ID in `ai_models.txt` is correct. Check the list of models supported by [OpenRouter]([openrouter.ai](https://openrouter.ai/)).

### Q: File attachment doesn't work
A: Check if the file path is correct and the file exists. Relative paths are based on the project root.

### Q: Memory shortage error occurs
A: Reduce the number of models running simultaneously or use smaller models.