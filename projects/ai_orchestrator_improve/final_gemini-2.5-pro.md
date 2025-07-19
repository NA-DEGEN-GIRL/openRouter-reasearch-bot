2025-07-18 10:24:34
알겠습니다. 프로덕트 전략가로서, 현재의 안정적인 코드 베이스를 기반으로 AI-Forge를 **강력한 프레임워크**에서 **지속 가능한 플랫폼**으로 성장시키기 위한 향후 개선 방향을 제안합니다.

---

### **프로덕트 전략 제안 (한글)**

---

#### **1. 성능 최적화**

##### **[P-1] API 응답 캐싱 도입**

-   **현재 상태**: 동일한 프롬프트라도 실행할 때마다 매번 새로운 API를 호출하여 비용과 시간이 발생합니다.
-   **목표 상태**: 프롬프트 내용과 첨부 파일의 해시(hash) 값을 키로 사용하여, 동일한 요청에 대해서는 캐시된 AI 응답을 즉시 반환합니다. 결과적으로 비용과 시간을 절약합니다.
-   **예상 난이도**: 보통
-   **예상 영향도**: 중간 (디버깅 및 반복 테스트 시 비용/시간 절감 효과가 큼)
-   **구현 우선순위**: **높음**

---

#### **2. 기능 확장**

##### **[F-1] 시각적 워크플로 편집기 (Web UI)**

-   **현재 상태**: 개발자만 CLI 환경에서 `.md` 파일을 수정하여 워크플로를 설계할 수 있습니다.
-   **목표 상태**: 웹 기반의 GUI를 제공하여, 비개발자(기획자, 분석가 등)도 노드를 드래그 앤 드롭하는 방식으로 AI 워크플로를 직관적으로 설계하고 실행할 수 있도록 합니다. 이는 프로젝트의 사용자 기반을 극적으로 확장시킬 수 있습니다.
-   **예상 난이도**: 어려움
-   **예상 영향도**: **높음**
-   **구현 우선순위**: **중간** (차세대 메이저 업데이트)

##### **[F-2] 고급 워크플로 제어 (조건 분기, 반복)**

-   **현재 상태**: 워크플로가 `prompt1` → `prompt2` 순서로 선형적으로만 실행됩니다.
-   **목표 상태**: 프롬프트 파일에 `## if ... ##`, `## for_each ... ##` 와 같은 제어문을 도입합니다. 예를 들어, "AI의 답변에 '성공'이라는 단어가 포함된 경우에만 `prompt3`을 실행"하는 식의 동적인 워크플로를 구현할 수 있습니다.
-   **예상 난이도**: 보통
-   **예상 영향도**: **높음** (단순 스크립트에서 진정한 '오케스트레이터'로 진화)
-   **구현 우선순위**: **높음**

##### **[F--3] 외부 트리거 및 API 연동 (웹훅)**

-   **현재 상태**: 사용자가 직접 CLI를 실행해야만 워크플로가 시작됩니다.
-   **목표 상태**: 외부 시스템의 이벤트(예: GitHub 커밋, Slack 메시지, 이메일 수신)를 통해 워크플로를 자동으로 트리거할 수 있는 웹훅(Webhook) 기능을 제공합니다.
-   **예상 난이도**: 보통
-   **예상 영향도**: 중간
-   **구현 우선순위**: 중간

---

#### **3. 유지보수성**

##### **[M-1] 중앙 집중식 모니터링 대시보드 구축**

-   **현재 상태**: 로그가 각 `projects` 폴더에 텍스트 파일로 흩어져 있어 전체적인 동향 파악이 어렵습니다.
-   **목표 상태**: Grafana, ELK 스택 등을 활용하여 모든 실행 로그와 결과를 중앙에서 수집합니다. 이를 통해 모델별 실패율, 평균 응답 시간, 토큰 사용량 등을 시각화하여 모니터링하고, 잠재적 문제를 사전에 탐지합니다.
-   **예상 난이도**: 보통
-   **예상 영향도**: 중간
-   **구현 우선순위**: 중간

##### **[M-2] 테스트 자동화 및 커버리지 확대**

-   **현재 상태**: 수동 QA에 의존하여 기능 무결성을 검증합니다.
-   **목표 상태**: 주요 서비스(파서, 핸들러 등)에 대한 단위 테스트(Unit Test)와 전체 워크플로에 대한 통합 테스트(Integration Test)를 자동화합니다. 테스트 커버리지를 80% 이상으로 끌어올려 코드 변경에 대한 안정성을 확보합니다.
-   **예상 난이도**: 보통
-   **예상 영향도**: **높음** (장기적인 안정성 및 유지보수 비용 절감에 필수적)
-   **구현 우선순위**: **높음**

---

#### **4. 개발자 경험(DX)**

##### **[D-1] Docker를 통한 컨테이너화**

-   **현재 상태**: 개발 환경을 수동으로 설정해야 합니다. (Python 버전, `pip install` 등)
-   **목표 상태**: `docker-compose.yml` 파일을 제공하여, `docker-compose up` 명령어 하나로 모든 의존성이 포함된 격리된 개발 환경을 즉시 실행할 수 있도록 합니다. 이는 신규 참여자의 온보딩 과정을 획기적으로 단축시킵니다.
-   **예상 난이도**: 쉬움
-   **예상 영향도**: 중간
-   **구현 우선순위**: **높음**

##### **[D-2] 기여 가이드 및 CI 파이프라인 구축**

-   **현재 상태**: 코드 기여에 대한 명확한 가이드라인과 자동화된 검증 절차가 없습니다.
-   **목표 상태**: `CONTRIBUTING.md` 문서를 작성하고, GitHub Actions를 활용하여 Pull Request 시 자동으로 코드 포맷팅(Black), 린팅(Linting), 테스트를 수행하는 CI 파이프라인을 구축합니다. 이는 코드 품질을 일관되게 유지하고 리뷰 부담을 줄여줍니다.
-   **예상 난이도**: 쉬움
-   **예상 영향도**: 중간 (오픈소스 생태계 확장의 기반)
-   **구현 우선순위**: 중간

---

### **Product Strategy Proposal (English)**

---

#### **1. Performance Optimization**

##### **[P-1] Introduce API Response Caching**

-   **Current State**: Every execution calls the API, even for identical prompts, incurring costs and time.
-   **Target State**: Use a hash of the prompt content and attachments as a key to return a cached AI response for identical requests, saving both cost and time.
-   **Difficulty**: Medium
-   **Impact**: Medium (Significant cost/time savings during debugging and iterative testing).
-   **Priority**: **High**

---

#### **2. Feature Expansion**

##### **[F-1] Visual Workflow Editor (Web UI)**

-   **Current State**: Only developers can design workflows by editing `.md` files in a CLI environment.
-   **Target State**: Provide a web-based GUI that allows non-developers (planners, analysts) to intuitively design and run AI workflows by dragging and dropping nodes. This would dramatically expand the project's user base.
-   **Difficulty**: Hard
-   **Impact**: **High**
-   **Priority**: **Medium** (As a next-generation major update).

##### **[F-2] Advanced Workflow Control (Conditional Logic, Loops)**

-   **Current State**: Workflows execute linearly (`prompt1` → `prompt2`).
-   **Target State**: Introduce control flow statements like `## if ... ##` and `## for_each ... ##` in the prompt file. This allows for dynamic workflows, e.g., "only run `prompt3` if the AI's response contains the word 'success'."
-   **Difficulty**: Medium
-   **Impact**: **High** (Evolves the tool from a simple script to a true 'orchestrator').
-   **Priority**: **High**

##### **[F-3] External Triggers and API Integration (Webhooks)**

-   **Current State**: A user must manually run the CLI to start a workflow.
-   **Target State**: Provide webhook functionality to automatically trigger workflows from external system events (e.g., a new GitHub commit, a Slack message, a received email).
-   **Difficulty**: Medium
-   **Impact**: Medium
-   **Priority**: Medium

---

#### **3. Maintainability**

##### **[M-1] Implement a Centralized Monitoring Dashboard**

-   **Current State**: Logs are scattered as text files in individual `projects` folders, making it difficult to grasp overall trends.
-   **Target State**: Collect all execution logs and results centrally using tools like the ELK Stack or Grafana. This enables monitoring of key metrics like model failure rates, average response times, and token usage, allowing for proactive problem detection.
-   **Difficulty**: Medium
-   **Impact**: Medium
-   **Priority**: Medium

##### **[M-2] Automate Testing and Increase Coverage**

-   **Current State**: Relies on manual QA for verifying feature integrity.
-   **Target State**: Automate unit tests for key services (parser, handlers) and integration tests for the entire workflow. Increase test coverage to over 80% to ensure stability during code changes.
-   **Difficulty**: Medium
-   **Impact**: **High** (Essential for long-term stability and reducing maintenance costs).
-   **Priority**: **High**

---

#### **4. Developer Experience (DX)**

##### **[D-1] Containerization with Docker**

-   **Current State**: The development environment must be set up manually (Python version, `pip install`, etc.).
-   **Target State**: Provide a `docker-compose.yml` file that allows developers to launch an isolated, fully dependency-managed environment with a single `docker-compose up` command. This significantly shortens the onboarding process for new contributors.
-   **Difficulty**: Easy
-   **Impact**: Medium
-   **Priority**: **High**

##### **[D-2] Establish a Contribution Guide and CI Pipeline**

-   **Current State**: Lacks clear guidelines for code contributions and an automated verification process.
-   **Target State**: Create a `CONTRIBUTING.md` document and set up a CI pipeline using GitHub Actions to automatically run code formatting (Black), linting, and tests on every Pull Request. This enforces consistent code quality and reduces the review burden on maintainers.
-   **Difficulty**: Easy
-   **Impact**: Medium (Foundation for expanding the open-source ecosystem).
-   **Priority**: Medium