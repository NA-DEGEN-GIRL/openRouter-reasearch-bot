2025-07-18 10:11:32
알겠습니다. 20년 경력의 수석 소프트웨어 아키텍트로서, 제공된 `AI-Forge` 프로젝트의 전체 코드 베이스를 분석하고 개선 계획을 수립하겠습니다. 모든 평가는 핵심 가치(안정성 > 가독성 > 성능 > 확장성)와 측정 가능한 지표에 기반합니다.

---

### 기능 보존 체크리스트
본 리팩토링 계획은 아래 기능들의 완전한 보존을 전제로 합니다.

- [x] **모든 기존 기능 목록화**
- [x] **리팩토링 전/후 동작 비교 기준 설정:** 기존 `research.md` 프롬프트 실행 시, 최종 생성되는 3가지 결과물 (상세 보고서, 텔레그램 요약, 트위터 게시물)의 내용과 구조가 동일해야 함.
- [x] **각 개선사항의 예상 효과 수치화:** 아래 '개선 계획' 섹션에 명시.
- [x] **리스크 평가 및 완화 전략:** 각 제안은 핵심 로직의 변경을 최소화하고, 관심사 분리를 통해 테스트 용이성을 높이는 방향으로 설계하여 리스크를 완화함.

---

### 1. 기존 기능 목록 (보존 대상)

코드를 분석한 결과, `AI-Forge`는 다음 핵심 기능들을 보유하고 있습니다.

1.  **CLI 기반 실행:** `main.py`를 통해 언어(`--lang`), 프롬프트 파일(`--prompt`) 등의 옵션을 받아 실행됩니다.
2.  **동적 설정 로딩:** `.env`에서 API 키를, `ai_models.txt`에서 사용할 모델 목록을 동적으로 로드합니다.
3.  **프롬프트 기반 워크플로:** `prompts/` 내의 Markdown(`.md`) 파일 하나로 전체 작업 흐름을 정의합니다.
    -   `## project name ##`: 결과물 폴더명을 지정합니다.
    -   `## system prompt ##`: 모든 AI 모델에 공통적으로 적용될 시스템 프롬프트를 설정합니다.
    -   `## promptN: [이름] ##`: 순차적으로 실행될 작업 단계를 정의합니다.
4.  **다중 AI 병렬 처리:** `ai_models.txt`에 명시된 모든 모델에게 각 프롬프트 단계를 동시에(concurrently) 요청합니다.
5.  **AI 협업 기능 (`#other_ai_info`):** 이전 단계에서 다른 AI들이 생성한 결과를 현재 단계의 AI가 참고하여 답변을 생성합니다.
6.  **멀티모달 입력:** 프롬프트 내에서 `#img`, `#pdf`, `#code`, `#doc` 태그를 사용하여 로컬 파일 또는 URL을 AI에 전달합니다. [OpenRouter](https://openrouter.ai/docs)는 이러한 복합적인 입력을 처리할 수 있는 API를 제공합니다.
7.  **실시간 로그 및 결과물 저장:**
    -   `projects/{project_name}/live_logs/{model_nickname}.log`: 각 모델의 실시간 응답(스트리밍) 및 추론 과정을 기록합니다.
    -   `projects/{project_name}/`: 단계별, 최종 결과물을 `.md` 파일로 저장합니다.
8.  **API 안정성 확보:** `tenacity`를 활용하여 API 요청 실패 시 자동 재시도(`retry`) 로직을 포함하고 있습니다.

---

### 2. 문제점 분석 결과 (정량/정성)

코드베이스는 잘 구조화되어 있으나, 안정성과 가독성 측면에서 개선이 필요한 몇 가지 핵심적인 문제가 식별되었습니다.

#### **Critical (안정성에 직결)**

*   **C-1: SRP(단일 책임 원칙) 위반 및 높은 결합도 (High Coupling)**
    *   **현상:** `ProjectOrchestrator`와 `AIModelClient`가 너무 많은 책임을 가지고 있습니다. 예를 들어, `AIModelClient.get_response` 메소드는 (1)API 메시지 준비, (2)API 요청, (3)스트림 처리, (4)실시간 로그 파일 쓰기, (5)최종 결과 파일 쓰기, (6)내부 히스토리 관리 등 6가지 이상의 책임을 수행합니다. 이는 코드의 테스트와 유지보수를 어렵게 만드는 핵심 원인입니다.
    *   **영향:** 한 기능의 수정이 다른 기능에 예기치 않은 버그를 유발할 가능성이 높습니다 (안정성 저하). 단위 테스트 작성이 거의 불가능한 구조입니다 (가독성/유지보수성 저하).
    *   **관련 파일:** `core/orchestrator.py`, `services/ai_client.py`

*   **C-2: 취약한 데이터 파이프라인 (Fragile Data Pipeline)**
    *   **현상:** AI 간의 협업(`other_ai_info`) 시, 구조화되지 않은 순수 텍스트(raw text)를 그대로 전달합니다. `prompts/research.md`의 `deactive` 섹션을 보면, 원래는 구조화된 `JSON` 데이터를 사용하려던 의도가 명확히 보입니다. 텍스트 기반 전달은 AI가 이전 단계의 정보를 정확히 파싱하기 어렵게 만들어 정보 유실 및 오해석을 유발합니다.
    *   **영향:** 워크플로가 복잡해질수록(prompt 단계가 많아질수록) 결과의 일관성과 정확성이 급격히 저하됩니다 (안정성 저하). 이는 현재 프레임워크의 가장 큰 잠재적 실패 지점입니다.
    *   **관련 파일:** `core/orchestrator.py` (`_prepare_user_content`), `prompts/research.md`

#### **Major (가독성 및 확장성에 영향)**

*   **M-1: 설정 객체의 상태 변화 (Mutable Config State)**
    *   **현상:** `Config` 객체가 `main.py`에서 생성된 후, `Orchestrator` 내부에서 `set_project_info` 메소드를 통해 `project_name`, `output_dir` 등의 주요 상태가 변경됩니다. 설정(Configuration) 객체는 애플리케이션 시작 시점에 불변(immutable) 상태로 고정되는 것이 이상적입니다.
    *   **영향:** 객체의 상태를 추적하기 어려워지고, 프로그램의 어느 시점에서 어떤 값이 설정되었는지 파악하기 힘들어집니다 (가독성/디버깅 난이도 증가).
    *   **관련 파일:** `config/config.py`, `core/orchestrator.py`

*   **M-2: 복잡한 프롬프트 파싱 로직**
    *   **현상:** `prompt_parser.py`의 `_parse_prompt_section` 함수는 정규식과 문자열 처리를 복합적으로 사용하여 프롬프트 텍스트에서 플래그와 파일 경로를 추출하고 제거합니다. 이 로직은 복잡하고 새로운 태그가 추가될 때마다 수정이 어렵습니다.
    *   **영향:** 파싱 로직의 가독성이 낮고, 새로운 프롬프트 문법을 추가하거나 변경하기가 어렵습니다 (확장성 저하).
    *   **관련 파일:** `services/prompt_parser.py`

#### **Minor (코드 품질 및 유지보수)**

*   **Mi-1: 흩어져 있는 상수 (Scattered Constants):** `model_cache.json`, `ai_models.txt`와 같은 파일 이름이 `constants.py`가 아닌 각 서비스 코드에 하드코딩되어 있습니다.
*   **Mi-2: 함수 길이 초과:** `AIModelClient.get_response` (~58줄), `Orchestrator._execute_prompt_parallel` (~52줄) 등 일부 핵심 함수의 길이가 권장 기준(50줄)을 초과하여 가독성을 저해합니다.
*   **Mi-3: 과도한 책임의 `file_handler`:** `make_message_content` 함수는 다양한 파일 유형을 처리하여 OpenAI API 형식에 맞는 복잡한 리스트/사전 구조를 생성합니다. 이는 PDF, 이미지, 코드 처리를 위한 각각의 헬퍼 함수로 분리하여 명확성을 높일 수 있습니다. [GitHub](https://github.com/OlympiaAI/open_router)의 Ruby 클라이언트 예시처럼, API 요청 본문을 구성하는 로직은 별도의 빌더 클래스로 분리하는 것이 더 나은 구조일 수 있습니다.

---

### 3. 개선 계획 초안 (Proposal_A)

위 문제점들을 해결하고 핵심 가치를 실현하기 위한 구체적인 개선 계획입니다.

**A-1. SRP 준수를 위한 서비스 책임 재분배 (대상: C-1)**

*   **Why (목표):** `Orchestrator`와 `AIClient`의 책임을 분리하여 코드의 **안정성**과 **가독성**을 극대화합니다. 각 컴포넌트가 하나의 명확한 역할만 수행하도록 만들어 테스트와 유지보수를 용이하게 합니다.
*   **What (실행 계획):**
    1.  **`ResultHandler` 서비스 신설:**
        -   파일 I/O (결과 저장, 로그 헤더 작성) 책임을 `Orchestrator`와 `AIClient`에서 이관합니다.
        -   `save_interim_result(prompt_id, model_nick, content)` 와 같은 메서드를 가집니다.
    2.  `AIModelClient` 리팩토링:
        -   `get_response` 메서드는 이제 API 호출과 응답 반환에만 집중합니다. 파일 I/O 로직을 모두 제거합니다.
        -   메서드는 `APIResponse` 객체만 반환하고, 파일 저장은 호출자인 `Orchestrator`의 책임이 됩니다.
*   **측정 가능한 개선:**
    -   `AIModelClient.get_response`, `Orchestrator._execute_prompt_parallel` 함수의 라인 수 **30% 이상 감소** (목표: < 40줄).
    -   순환 복잡도 **10 이하**로 감소.

**A-2. 구조적 데이터 파이프라인 도입 (대상: C-2)**

*   **Why (목표):** AI 협업 과정에서 발생하는 정보 유실을 방지하고, 워크플로의 **안정성**과 예측 가능성을 획기적으로 향상시킵니다.
*   **What (실행 계획):**
    1.  `prompts/research.md`의 `deactive` 되어 있는 JSON 기반 프롬프트를 활성화하는 것을 최종 목표로 삼습니다.
    2.  `core/models.py`에 `PromptResult` 데이터 클래스를 정의합니다. (`raw_text: str`, `structured_data: Optional[Dict] = None` 포함)
    3.  `Orchestrator`의 `last_turn_responses`를 `Dict[str, str]`에서 `Dict[str, PromptResult]`로 변경합니다.
    4.  `#other_ai_info` 태그 처리 시, `PromptResult`의 `structured_data`를 우선적으로 활용하여 다음 프롬프트를 구성하도록 로직을 개선합니다. 텍스트만 있을 경우 기존 방식을 유지(하위 호환성).
*   **측정 가능한 개선:**
    -   복잡한 워크플로(5단계 이상)에서의 최종 결과물 품질 일관성 점수 향상 (정성적 평가).
    -   JSON 출력을 요구하는 프롬프트의 실패율 **0%** 달성.

**A-3. `ProjectContext` 도입을 통한 설정 불변성 확보 (대상: M-1)**

*   **Why (목표):** 설정(Config)과 실행 문맥(Context)을 분리하여 프로그램의 상태 변화 추적을 용이하게 하고 **가독성**을 높입니다.
*   **What (실행 계획):**
    1.  `core/models.py`에 `ProjectContext` 데이터 클래스를 새로 정의 (`project_name`, `system_prompt`, `output_dir` 등 포함).
    2.  `Orchestrator`는 초기화 시 `prompt_parser`를 통해 얻은 정보로 `ProjectContext` 객체를 생성하여 내부 상태로 관리합니다.
    3.  `Config` 클래스의 `set_project_info` 메서드를 제거하고, `Config`는 실행 중에 변경되지 않는 불변 객체로 유지합니다.
*   **측정 가능한 개선:**
    -   `Config` 클래스에서 setter 메서드 완전 제거.
    -   전역적으로 공유되는 상태(실행 컨텍스트)를 명시적인 객체로 관리하여 코드 추적 용이성 증대.

**A-4. 상수 중앙화 및 파서 개선 (대상: M-2, Mi-1)**

*   **Why (목표):** **유지보수성**을 높이고 파싱 로직의 명확성을 개선합니다.
*   **What (실행 계획):**
    1.  `config.py`, `model_provider.py` 등에 하드코딩된 파일 이름(`ai_models.txt`, `model_cache.json`)을 모두 `config/constants.py`로 이전합니다. `pypi.org`에서 볼 수 있는 패키지들처럼 설정 값은 한 곳에 모으는 것이 표준적인 관례입니다. [pypi.org](https://pypi.org/project/owega/5.22.2/)
    2.  `PromptParser` 내부에서 각 플래그(`'#reasoning'`) 및 파일 명령어 처리를 별도의 작은 함수로 분리하여 `_parse_prompt_section`의 복잡도를 낮춥니다.
*   **측정 가능한 개선:**
    -   애플리케이션 코드 내 하드코딩된 상수(파일 경로, 매직 스트링) **0개** 달성.
    -   `PromptParser._parse_prompt_section` 함수의 순환 복잡도 **8 이하**로 감소.

---

### 4. Baseline 메트릭

리팩토링 전 현재 코드의 정량적 상태는 다음과 같습니다.

| 메트릭                | `AIModelClient.get_response` | `Orchestrator._execute_prompt_parallel` | `PromptParser._parse_prompt_section` |
| --------------------- | ---------------------------- | --------------------------------------- | ------------------------------------ |
| **함수 라인 수 (LoC)**  | ~58 줄                       | ~52 줄                                  | ~45 줄                               |
| **순환 복잡도 (추정)**  | **~12 (초과)**               | **~11 (초과)**                          | ~9                                   |
| **주요 책임 수 (SRP)**  | 6+                           | 7+                                      | 3                                    |