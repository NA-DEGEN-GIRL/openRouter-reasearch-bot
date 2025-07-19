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
