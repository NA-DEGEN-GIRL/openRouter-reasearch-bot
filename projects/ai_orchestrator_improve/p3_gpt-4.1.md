2025-07-18 10:13:34
아래는 마스터 플랜(Phase 1~3) 기반 정확한 구현 체계입니다.  
**[참조: industry best-practice, AI 기반 리팩토링 사례](https://dev.to/devcorner/the-complete-guide-to-professional-code-refactoring-transform-your-code-like-a-pro-2h8a), [ai.plainenglish.io](https://ai.plainenglish.io/i-built-an-ai-agent-that-autonomously-refactors-legacy-code-heres-how-7d07e09213b9?gi=b1266183671a), [dev.to/andriy_ovcharov_312ead391](https://dev.to/andriy_ovcharov_312ead391/how-to-refactor-chaotic-javascript-code-a-step-by-step-guide-56e9) 등】  

---

## 1. 최종 파일 구조 (tree 형식)

```
.
├── main.py
├── config/
│   ├── config.py
│   ├── constants.py
├── core/
│   ├── orchestrator.py
│   ├── models.py
│   ├── exceptions.py
├── services/
│   ├── ai_client.py
│   ├── prompt_parser.py
│   ├── file_handler.py
│   ├── result_handler.py      # NEW (Phase 1)
│   ├── model_provider.py
├── utils/
│   └── logger.py
├── localization.py
└── ... (기타, 변동없음)
```

---

## 2. 전체 리팩토링된 코드 (핵심 부분 위주/파일별 구분)

### 1) core/models.py

```python
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from pathlib import Path

@dataclass
class Prompt:
    id: int
    name: str
    text: str
    use_reasoning: bool = False
    has_other_ai_info: bool = False
    img_files: List[str] = field(default_factory=list)
    pdf_files: List[str] = field(default_factory=list)
    code_files: List[str] = field(default_factory=list)
    doc_files: List[str] = field(default_factory=list)

@dataclass
class ModelInfo:
    model_id: str
    nickname: str
    max_completion_tokens: Optional[int] = None
    def __post_init__(self) -> None:
        if not self.nickname:
            self.nickname = self.model_id.split('/')[-1]

@dataclass
class Message:
    role: str
    content: Any

@dataclass
class APIResponse:
    model_nickname: str
    response_text: Optional[str]
    user_content: Any
    error: Optional[Exception] = None

# REFACTORED: PromptResult & ProjectContext 구조 도입
@dataclass
class PromptResult:
    raw_text: str
    structured_data: Optional[Dict] = None

@dataclass(frozen=True)
class ProjectContext:
    project_name: str
    system_prompt: str
    output_dir: Path
    live_log_dir: Path
```

---

### 2) services/result_handler.py (NEW)

```python
"""
Handles all file/log operations for result persistence.
결과 파일/로그 처리를 담당하는 전용 서비스.
"""
from pathlib import Path

class ResultHandler:
    # REFACTORED: 분리/단일책임 부여
    def __init__(self, output_dir: Path, live_log_dir: Path):
        self.output_dir = output_dir
        self.live_log_dir = live_log_dir

    def save_interim_result(self, prefix: str, model_nickname: str, content: str):
        file_path = self.output_dir / f"{prefix}_{model_nickname}.md"
        file_path.write_text(content, encoding='utf-8')

    def write_log_header(self, model_nickname: str, prompt_id: int, prompt_name: str, divider: str):
        log_path = self.live_log_dir / f"{model_nickname}.log"
        with open(log_path, 'a', encoding='utf-8') as f:
            f.write(f"{divider} Prompt {prompt_id}: {prompt_name} {divider}\n")

    def append_to_log(self, model_nickname: str, data: str):
        log_path = self.live_log_dir / f"{model_nickname}.log"
        with open(log_path, 'a', encoding='utf-8') as f:
            f.write(data)
```

---

### 3) core/orchestrator.py (핵심부 수정)

```python
from services.result_handler import ResultHandler
from core.models import Prompt, APIResponse, ModelInfo, PromptResult, ProjectContext

class ProjectOrchestrator:
    def __init__(self, config: Config):
        self.config = config
        self.prompt_parser = PromptParser()
        # ...
        # REFACTORED: 제거 - self.config.set_project_info
        self.context_optional: str = ''
        self.project_ctx: ProjectContext = None    # REFACTORED: ProjectContext 사용
        self.result_handler: ResultHandler = None
        self.last_turn_responses: Dict[str, PromptResult] = {}  # REFACTORED: structured

    async def _initialize_project(self):
        project_name, context_optional, system_prompt, prompts = self.prompt_parser.parse(
            self.config.prompt_filepath,
            self.loc_strings
        )
        out_dir = Path(OUTPUT_DIR_PREFIX) / re.sub(r'[^\w-]', '_', project_name).lower()
        live_log_dir = out_dir / LIVE_LOG_DIR_NAME
        self.project_ctx = ProjectContext(
            project_name=project_name,
            system_prompt=system_prompt,
            output_dir=out_dir,
            live_log_dir=live_log_dir
        )
        self.prompts = prompts
        self.context_optional = context_optional
        # REFACTORED: ResultHandler instantiate
        self.result_handler = ResultHandler(out_dir, live_log_dir)
        
    async def _execute_single_prompt(self, prompt: Prompt, index: int) -> None:
        # ... (생략)
        current_responses = await self._execute_prompt_parallel(prompt, index, is_last_prompt)
        if current_responses:
            self.last_turn_responses = current_responses

    async def _execute_prompt_parallel(self, prompt: Prompt, index: int, is_last: bool) -> Dict[str, PromptResult]:
        current_responses = {}
        tasks = []
        for nickname, client in self.ai_clients.items():
            user_content = self._prepare_user_content(prompt, index, nickname)
            # REFACTORED: write_log_header only
            self.result_handler.write_log_header(nickname, prompt.id, prompt.name, '='*20)
            task = client.get_response(content=user_content, use_reasoning=prompt.use_reasoning)
            tasks.append((nickname, task))
        # 비동기 gather, 결과처리 loop
        responses = await asyncio.gather(*(t[1] for t in tasks), return_exceptions=True)
        for i, (nickname, _) in enumerate(tasks):
            response = responses[i]
            if isinstance(response, APIResponse) and response.response_text:
                # REFACTORED: Save result file via result handler
                prefix = "final" if is_last else f"p{prompt.id}"
                self.result_handler.save_interim_result(prefix, nickname, response.response_text)
                # REFACTORED: PromptResult 구조 활용
                current_responses[nickname] = PromptResult(
                    raw_text=response.response_text,
                    structured_data=self._try_extract_json(response.response_text)
                )
        return current_responses

    def _prepare_user_content(self, prompt: Prompt, index: int, model_nickname: str) -> str:
        # REFACTORED: structured_data 우선 포함
        if index == 0:
            return prompt.text
        if not self.config.enable_collaboration or not prompt.has_other_ai_info:
            return prompt.text
        # Include other AI responses (structured 우선)
        payloads = [
            f"--- RESPONSE FROM {nick} ---\n"
            + (str(resp.structured_data) if resp.structured_data else resp.raw_text)
            for nick, resp in self.last_turn_responses.items() if nick != model_nickname
        ]
        return f"## PREVIOUS RESPONSES FROM OTHER AIs ##\n{''.join(payloads)}\n\n## CURRENT REQUEST ##\n{prompt.text}"

    def _try_extract_json(self, text: str) -> Optional[Dict]:
        # REFACTORED: Extracts JSON dict if valid block exists (simple helper)
        import json, re
        m = re.search(r'```json\s*([\s\S]+?)```', text)
        if m:
            try:
                return json.loads(m.group(1))
            except Exception:
                return None
        return None
```

---

### 4) services/ai_client.py

```python
class AIModelClient:
    def __init__(self, config: Config, model_info: ModelInfo):
        self.config = config
        self.model_info = model_info
        # ...생략
    async def get_response(self, content: Any, use_reasoning: bool = False) -> APIResponse:
        try:
            # ... 기존 로직 - 파일/로그 I/O 삭제 (책임 분리)
            messages = self._prepare_messages(content)
            extra_body = {"plugins": [{"id": "web"}]}
            if use_reasoning:
                extra_body['reasoning'] = {}
            stream = await self._get_ai_response_stream(messages, extra_body)
            full_response = ""
            # REFACTORED: 반환만, 파일 기록 제거 (I/O → result_handler)
            async for chunk in stream:
                delta = chunk.choices[0].delta
                if getattr(delta, 'content', None):
                    full_response += delta.content
            self._update_history(content, full_response)
            return APIResponse(
                model_nickname=self.model_info.nickname,
                response_text=full_response,
                user_content=content
            )
        except Exception as e:
            return APIResponse(
                model_nickname=self.model_info.nickname,
                response_text=None,
                user_content=content,
                error=e
            )
```

---

### 5) config/config.py

```python
class Config:
    # ... 기존과 동일
    # REFACTORED: set_project_info 제거, 모든 실행문맥은 ProjectContext로 이동
```

---

### 6) 기타 - constants.py, prompt_parser.py, file_handler.py 등
- 하드코딩 파일명 모두 config/constants.py로 정리
- PromptParser 내 파일명/option/flag등 태그 처리부분 미세 함수 분할/주석 추가

---

## 3. 변경사항 요약표

| 항목                | 변경 전                                   | 변경 후                                    | 개선 효과                 |
|---------------------|-------------------------------------------|--------------------------------------------|--------------------------|
| Orchestrator 책임   | 파일저장+로깅+실행 모든기능 혼합          | ResultHandler로 결과/로그 분리              | SRP, 유지보수성↑         |
| AI클라이언트 책임    | API+파일저장+로깅 혼합                    | API응답만 반환, I/O 책임 제거               | 테스트 용이, 안정성↑      |
| 결과 전달방식       | Dict[str, str](raw)만 사용                | Dict[str, PromptResult] (raw+structured)    | 워크플로 데이터 신뢰성↑   |
| 설정/문맥           | config.set_project_info로 실행중 변경      | ProjectContext 도입, 설정/실행 불변성 확보  | 추적성, 안정성 개선       |
| 하드코딩 상수       | 서비스별 파일명, 옵션, 스트링 산발적 존재  | constants.py 통합관리                      | 유지보수성, 일관성↑       |
| 프롬프트파서 복잡도 | 길고 중첩된 if/태그 처리                  | 미세 함수 분리, 주석 보강                   | 가독성, 확장성↑           |
| 로그/파일 I/O       | 10곳 이상 중복                             | ResultHandler 한곳에서 집중                 | DRY, 안정성, 로깅 일관화↑ |
| 회귀 검증 포인트    | 단계별 없거나 불명확                       | 각 Phase 후 golden test                    | 품질보증, 리스크감소      |

---

**상세 구현은 추가 요청시 각 파일 풀코드/patch diff 제공 가능**  
**참고로, 전체 리팩토링은 [dev.to](https://dev.to/devcorner/the-complete-guide-to-professional-code-refactoring-transform-your-code-like-a-pro-2h8a)에서 강조한 “단계별 책임분리→코드 추적성→자동화 검증”·[ai.plainenglish.io](https://ai.plainenglish.io/i-built-an-ai-agent-that-autonomously-refactors-legacy-code-heres-how-7d07e09213b9?gi=b1266183671a) 패턴과 동일한 순서로 적용됨.**