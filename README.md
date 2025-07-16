# AI-Forge: AI Workflow Orchestrator

**다양한 AI 모델을 병렬 실행하고, 프롬프트 설계만으로 AI 협업, 코드 개선, 멀티모달 분석을 자동화하는 프레임워크입니다.**

> **프로젝트 생성 배경:** 이 프로젝트의 전체 코드는 `code_instruction.txt`에 명시된 요구사항 명세서를 기반으로, LLM(AI)과의 협업을 통해 생성되었습니다.

## ✨ 주요 특징

  - **다중 AI 병렬 처리:** `ai_models.txt`에 명시된 모든 모델에 작업을 동시에 분산하여 처리 속도를 극대화합니다.
  - **프롬프트 기반 워크플로:** 코드를 수정할 필요 없이, `prompts/` 폴더 안의 마크다운 파일 하나로 전체 작업 흐름(분석, 협업, 출력 형식 등)을 자유롭게 설계하고 제어할 수 있습니다.
  - **AI 협업 및 검증:** 각 AI가 다른 AI의 답변을 참고하여 자신의 결과를 보강하거나 수정하는 '교차 검증' 단계를 워크플로에 포함시킬 수 있습니다. (`# other_ai_info` 태그 활용)
  - **멀티모달 입력 지원:** 프롬프트 파일 내에서 `#img`, `#pdf`, `#code` 태그를 사용하여 이미지, PDF, 코드 파일을 AI에게 직접 전달하고 분석시킬 수 있습니다.
  - **실시간 로그 모니터링:** 메인 프로세스와 별도로, `view_log.py`를 통해 특정 AI의 작업 과정(`reasoning` 포함)을 실시간으로 확인할 수 있습니다.

## 🚀 시작하기 (Quick Start)

### 1\. 환경 설정

```bash
# 1. 저장소 복제
git clone https://github.com/NA-DEGEN-GIRL/openRouter-ai-forge.git
cd openRouter-ai-forge

# 2. 필요 라이브러리 설치
pip install -r requirements.txt

# 3. .env 파일 설정
cp .env.example .env
# nano .env 또는 vim .env 명령어로 .env 파일을 열고 API 키를 입력하세요.
```

### 2\. 설정 파일 준비

  - **`ai_models.txt`**: 사용할 AI 모델의 ID를 한 줄에 하나씩 입력합니다. (예: `google/gemini-2.5-pro`)
  - **`prompts/`**: 실행할 작업 설계도(`.md`)를 이 폴더 안에 넣습니다. `prompts/research.md` 예시를 참고하세요.

### 3\. 봇 실행

  - **기본 실행 (리서치 봇)**
    ```bash
    python main.py
    ```
  - **언어 및 특정 프롬프트 지정하여 실행**
    ```bash
    python main.py --lang en --prompt research_en.md
    ```

### 4\. 실시간 로그 확인 (선택 사항)

  - 새 터미널을 열고 아래 명령어를 실행하면, 특정 모델의 작업 과정을 실시간으로 볼 수 있습니다.
    ```bash
    python view_log.py
    ```

## ⚙️ 기본 리서치 봇 사용법 (`research.md`)

이 프레임워크의 가장 기본적인 사용법은 `prompts/research.md` 파일을 수정하여 특정 프로젝트를 리서치하는 것입니다.

1.  **`prompts/research.md` 파일 열기:** 텍스트 에디터로 해당 파일을 엽니다.
2.  **`project info` 블록 수정:** `## prompt1: 심층 분석 및 보고 ##` 섹션 내부에 있는 아래와 같은 `**project info**` 블록을 찾습니다.
    ```markdown
    **project info**
    GTE
    • 한 줄 소개: Decentralized trading platform
    ...
    **end of project info**
    ```
3.  **정보 교체:** `GTE` 프로젝트의 예시 정보를 **조사하고 싶은 프로젝트의 정보**로 모두 교체합니다. 프로젝트 이름, 웹사이트, 투자사 등 아는 정보를 최대한 상세히 넣어주면 AI가 더 정확한 결과를 찾아냅니다.
4.  **봇 실행:** 터미널에서 `python main.py` 명령어를 실행하면, 수정된 정보를 바탕으로 리서치가 자동으로 시작됩니다.

## 🤡 프롬프트 파일 설계

이 시스템의 모든 동작은 `prompts/` 폴더 안의 `.md` 파일로 제어됩니다.

> **중요:** 모든 프롬프트 파일은 반드시 `prompts/` 폴더 안에 있어야 합니다.

```markdown
## project name ##
My Awesome Project

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

  - `## project name ##`: 작업의 고유 이름. 결과물이 저장될 폴더명으로 사용되므로 **반드시 파일 최상단에 작성해야 합니다.**
  - `## prompt1 ##`: 각 작업 단계를 정의합니다. 번호와 이름은 자유롭게 지정할 수 있습니다.
  - **옵션 태그:**
      - `# reasoning`: AI의 생각 과정을 로그 파일에 기록합니다.
      - `# other_ai_info`: 이전 단계에서 다른 AI가 생성한 답변을 현재 AI가 참고하도록 합니다.
      - `# img`, `# pdf`, `# code`: 해당 경로의 파일을 프롬프트에 첨부합니다. (다중 첨부 가능)

## 🗂️ 주요 파일 구조

  - `main.py`: 메인 실행 스크립트
  - `view_log.py`: 실시간 로그 뷰어
  - `localization.py`: 다국어 UI 텍스트
  - `utils/search_ai_models.py`: 모델 정보 검색 유틸리티
  - `ai_models.txt`: 사용할 AI 모델 목록
  - `requirements.txt`: 필요 라이브러리
  - `.env.example`: `.env` 파일 템플릿
  - `prompts/`: 프롬프트 설계도(`.md`)를 저장하는 디렉토리
      - `research.md`: 프로젝트의 긍정/부정적 측면을 모두 분석하고, 최종적으로 상세 보고서, 텔레그램 요약본, 트위터 홍보글을 생성하는 기본 워크플로입니다.
      - `research_en.md`: 위 `research.md`의 영문 버전입니다.

-----

# AI-Forge: AI Workflow Orchestrator

**A framework that orchestrates multiple AI models to automate user-defined workflows, all through simple prompt design.**

> **About This Project:** The entire codebase for this project was generated in collaboration with an LLM, based on the system requirements specification detailed in `code_instruction_en.txt`.

## ✨ Key Features

  - **Concurrent Multi-AI Processing:** Drastically reduces task time by distributing work to all specified models in `ai_models.txt` simultaneously.
  - **Prompt-Driven Workflow:** The entire workflow—from analysis and collaboration to output formatting—is controlled by a single Markdown file in the `prompts/` folder, requiring no code changes.
  - **AI Collaboration & Validation:** Incorporate a "cross-validation" step in your workflow, where each AI references the outputs of other AIs to enrich or correct its own findings (using the `#other_ai_info` tag).
  - **Multimodal Input Support:** Directly pass images, PDFs, and code files to the AI for analysis by using `#img`, `#pdf`, and `#code` tags within your prompt files.
  - **Live Log Monitoring:** A separate `view_log.py` script allows for real-time monitoring of any specific model's progress, including its reasoning process, without cluttering the main terminal.

## 🚀 Quick Start

### 1\. Environment Setup

```bash
# 1. Clone the repository
git clone https://github.com/NA-DEGEN-GIRL/openRouter-ai-forge.git
cd openRouter-ai-forge

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure .env file
cp .env.example .env
# Open .env with a text editor (e.g., nano .env) and enter your API key.
```

### 2\. Configuration

  - **`ai_models.txt`**: List the OpenRouter model IDs you want to use, one per line (e.g., `google/gemini-2.5-pro`).
  - **`prompts/`**: Place your workflow blueprint (`.md` file) inside this directory. Refer to the `prompts/research_en.md` example.

### 3\. Run the Bot

  - **Default Execution**
    ```bash
    python main.py
    ```
  - **Specify Language and a Custom Prompt File**
    ```bash
    python main.py --lang en --prompt custom_task.md
    ```

### 4\. Monitor Live Logs (Optional)

  - Open a new terminal and run the following command to see a specific model's progress in real-time.
    ```bash
    python view_log.py
    ```

## ⚙️ How to Use the Default Research Bot (`research.md`)

The most basic way to use this framework is to research a specific project by editing the `prompts/research.md` file.

1.  **Open `prompts/research.md`:** Open the file with a text editor.
2.  **Edit the `project info` Block:** Find the `**project info**` block located inside the `## prompt1: In-depth Analysis and Reporting ##` section.
    ```markdown
    **project info**
    GTE
    • One-liner: Decentralized trading platform
    ...
    **end of project info**
    ```
3.  **Replace Information:** Replace the example information for the `GTE` project with the details of the project **you want to research**. The more details you provide (name, website, investors, etc.), the more accurate the AI's results will be.
4.  **Run the Bot:** Execute `python main.py` in your terminal. The research will start automatically based on the information you provided.

## 🤡 Designing the Prompt File

All operations of this system are controlled by `.md` files in the `prompts/` directory.

> **Important:** All prompt files must be placed inside the `prompts/` directory.

```markdown
## project name ##
My Awesome Project

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

  - **`## project name ##`**: A unique name for the task. This **must be the first section** as it is used for the output folder name.
  - **`## prompt1 ##`**: Defines each step of the workflow. The number and name are fully customizable.
  - **Option Tags:**
      - `# reasoning`: Logs the AI's thought process.
      - `# other_ai_info`: Allows the AI to reference responses from other AIs in the previous step.
      - `# img`, `# pdf`, `# code`: Attaches the specified file to the prompt. (Multiple attachments are allowed).

## 🗂️ Key File Structure

  - `main.py`: Main execution script
  - `view_log.py`: Real-time log viewer
  - `localization.py`: Multi-language UI text
  - `utils/search_ai_models.py`: Model search utility
  - `ai_models.txt`: List of AI models to use
  - `requirements.txt`: Required packages
  - `.env.example`: Template for .env file
  - `prompts/`: Directory for prompt blueprints (`.md`)
      - `research.md`: The default workflow that analyzes both positive and negative aspects of a project to generate a detailed report, a Telegram summary, and promotional tweets.
      - `research_en.md`: The English version of `research.md`.