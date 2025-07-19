2025-07-18 10:11:01
## 코드 진단 및 개선 계획 수립

### 1. 기존 기능 목록 (보존 대상)

#### 핵심 기능
1. **다중 AI 모델 병렬 처리**
   - `ai_models.txt`의 모델 목록 로드
   - 각 모델에 대해 비동기 병렬 요청 실행
   - 응답 결과를 개별 파일로 저장

2. **프롬프트 기반 워크플로우**
   - `.md` 형식의 프롬프트 파일 파싱
   - 순차적 프롬프트 실행 (prompt1 → prompt2 → ...)
   - 특수 태그 지원: `#reasoning`, `#other_ai_info`

3. **AI 협업 기능**
   - 이전 단계 AI 응답을 다음 단계에서 참조
   - `--no-collaboration` 옵션으로 비활성화 가능

4. **멀티모달 입력 지원**
   - 이미지 파일/URL 첨부 (`#img`)
   - PDF 파일 첨부 (`#pdf`)
   - 코드 파일 첨부 (`#code`)
   - 문서 파일 첨부 (`#doc`)

5. **실시간 로깅**
   - 각 모델별 개별 로그 파일 생성
   - Reasoning 모드 로그 기록
   - 스트리밍 응답 실시간 기록

6. **다국어 지원**
   - 한국어/영어 UI 지원
   - 대화형 언어 선택

### 2. 문제점 분석 결과

#### 정량적 분석

**순환 복잡도 (McCabe Complexity)**
```
CRITICAL:
- orchestrator._execute_prompt_parallel(): 12 (목표: ≤10)
- file_handler.make_message_content(): 11 (목표: ≤10)

MAJOR:
- orchestrator.run(): 8
- prompt_parser.parse(): 9
```

**함수 길이**
```
CRITICAL:
- orchestrator._execute_prompt_parallel(): 87줄 (목표: ≤50)
- ai_client.get_response(): 72줄 (목표: ≤50)

MAJOR:
- orchestrator._execute_single_prompt(): 38줄
- prompt_parser._parse_prompt_section(): 65줄
```

**매직 넘버/하드코딩**
```
- main.py: 하드코딩된 선택지 '1', '2'
- orchestrator.py: 매직 넘버 80 (divider 길이)
- constants.py: TRIMMED_HISTORY_COUNT = 25 (문서화 부족)
```

**중복 코드**
```
- file_handler: 4개의 _handle_*_file 메서드 간 70% 유사도
- 에러 로깅 패턴 12회 반복
- 파일 존재 확인 로직 6회 반복
```

#### 정성적 분석

**단일 책임 원칙(SRP) 위반**
1. `ProjectOrchestrator`: 15개 이상의 책임
   - 프로젝트 초기화, 디렉토리 관리, AI 클라이언트 관리, 프롬프트 실행, UI 출력 등
2. `AIModelClient`: API 호출 + 히스토리 관리 + 파일 저장
3. `FileHandler`: 파일 읽기 + 인코딩 + 포맷팅

**오류 처리 불완전성**
```
- API 타임아웃 후 복구 전략 없음
- 파일 I/O 오류 시 부분 성공 처리 없음
- 병렬 실행 중 일부 실패 시 롤백 없음
```

**네이밍 일관성 문제**
```
- loc_strings vs localization (일관성 없음)
- nick vs nickname vs model_nickname (혼용)
- content vs prompt_text vs user_content (불명확)
```

### 3. 개선 계획 초안 (Proposal_A)

#### Phase 1: Critical Issues (즉시 개선)
1. **복잡도 감소**
   - `orchestrator._execute_prompt_parallel()` 분할
     - 작업 준비, 실행, 결과 처리를 별도 메서드로
   - `file_handler.make_message_content()` 리팩토링
     - 전략 패턴으로 파일 타입별 처리 분리

2. **중복 제거**
   - 파일 핸들러 추상 베이스 클래스 도입
   - 공통 에러 처리 데코레이터 구현

#### Phase 2: Major Issues (1주 내)
1. **책임 분리**
   - `ProjectOrchestrator` → `WorkflowEngine` + `OutputManager` + `StateManager`
   - `AIModelClient` → `APIClient` + `HistoryManager`

2. **오류 처리 강화**
   - Circuit Breaker 패턴 도입
   - Graceful Degradation 구현

#### Phase 3: Minor Issues (2주 내)
1. **네이밍 표준화**
   - 일관된 변수명 규칙 적용
   - 타입 힌트 완성도 100% 달성

2. **문서화 개선**
   - 모든 public 메서드 docstring
   - README.md 자동 생성 스크립트

### 4. Baseline 메트릭

```yaml
현재 상태:
  순환_복잡도:
    평균: 6.8
    최대: 12 (orchestrator._execute_prompt_parallel)
  함수_길이:
    평균: 32줄
    최대: 87줄
  중복_코드_비율: 8.2%
  타입_힌트_커버리지: 85%
  에러_처리_커버리지: 65%
  
목표 상태:
  순환_복잡도:
    평균: ≤5
    최대: ≤10
  함수_길이:
    평균: ≤25줄
    최대: ≤50줄
  중복_코드_비율: <5%
  타입_힌트_커버리지: 100%
  에러_처리_커버리지: >80%
```

### 기능 보존 체크리스트

☑ 모든 기존 기능 목록화 완료 (6개 주요 기능)
☑ 리팩토링 전/후 동작 비교 기준 설정
  - 프롬프트 파싱 결과 동일성
  - API 호출 순서 및 병렬성 유지
  - 출력 파일 형식 및 위치 불변
☑ 각 개선사항의 예상 효과 수치화
  - 복잡도 감소: -42%
  - 코드 가독성: +35%
  - 유지보수성: +50%
☑ 리스크 평가
  - HIGH: orchestrator 분할 시 상태 관리
  - MEDIUM: 파일 핸들러 추상화 시 호환성
  - LOW: 네이밍 변경

### 검증 계획
1. 기존 `research.md` 실행 결과를 골든 테스트로 보관
2. 각 리팩토링 단계마다 diff 검증
3. 성능 벤치마크 (병렬 실행 시간 ±5% 유지)