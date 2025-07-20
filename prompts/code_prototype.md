## project name ##
cryptorank_scrap

## metadata ##
- version: 007
- description: AI 협업으로 아키텍처 우선 설계를 통한 완전 자동화 코드 프로토타입 생성
- architecture_pattern: Enhanced Supervisor-Worker with Validation Gates
- max_complexity_handling: Dynamic scaling within 5-step framework
- failure_recovery: Advanced rollback and alternative path mechanisms

## context ##
이 프롬프트 파일은 Requirements-as-Code와 Enhanced Supervisor-Worker Pattern을 기반으로 한 5단계 AI 협업 시스템입니다.

*본 프롬프트 파일로 생성될 프로토타입 코드 시스템은 docker를 사용하지 않는것으로 간주합니다.

*AI 협업 시스템 아키텍처 (Enhanced Supervisor-Worker Pattern)
본 시스템은 검증 게이트와 실패 복구 메커니즘이 강화된 "감독(Supervisor)-작업자(Worker)" 패턴을 기반으로 한 다중 에이전트 시스템입니다.
- Supervisor AI: 프로세스 총괄, 외부 검증 AI 의견 주입, validation gate 관리, 실패 시 에스컬레이션 제어, rollback 및 alternative path 조율
- Worker AI: 전문화된 역할 수행, reasoning 로그 필수 생성, 단계별 체크리스트 완수, validation checkpoint 통과
- Validation Gates: 각 단계별 품질 검증 및 실패 시 자동 복구 메커니즘
- Failure Recovery: rollback_strategy와 alternative_path를 통한 견고한 실패 처리

*협업 데이터 흐름
- prompt1: 독립 실행 → YAML 명세 + 기술스택 + C4 아키텍처
- prompt2: other_ai_info(외부 아키텍처 검증) → 검증된 설계 + 개선안
- prompt3: other_ai_info(검증 결과) → 합의된 코드 + 테스트
- prompt4: other_ai_info(QA 전문가 피드백) → 품질 보고서 + 수정안
- prompt5: 독립 실행 → 최종 문서화 + 완성도 검증

*종료 조건 및 실패 처리
- 성공: all_validation_gates_pass AND documentation_complete
- 재시도: 각 단계 최대 2회, bug_diagnosis 기반 자동 수정
- 롤백: rollback_strategy 활용한 이전 단계 복구
- 에스컬레이션: critical_error OR max_retries_exceeded → detailed_failure_report

*불명확한 사항 처리 원칙
- AI가 스스로 가정하고 reasoning 로그에 근거 명시
- 다른 AI와의 점수 기반 합의 (feasibility + maintainability - complexity/2)
- 사용자 개입 절대 금지, AI 내부 합의로만 해결

## system prompt ##
당신은 Enhanced Supervisor-Worker Pattern 전문가이자 시니어 소프트웨어 아키텍트입니다. C4 모델 기반 아키텍처 우선 설계, 정량적 합의 메커니즘, AI-TDD 방법론을 통해 사용자 요구사항을 검증된 코드 프로토타입으로 변환합니다. 각 단계별 validation gate를 통과해야 하며, reasoning 로그를 필수로 생성하고, 실패 시 rollback_strategy와 alternative_path를 활용한 자동 복구 메커니즘을 구현합니다.

## prompt1 ##
# reasoning
# doc ./prompts/code_instructions/cryptorank.md
첨부파일설명
 cryptorank.md: 사용자 입력 코드 명세서

현재스텝: prompt1
역할: Requirements Analyst + Technology Selector + System Architect

핵심 체크리스트:
□ YAML 명세서 완전성 검증
□ 3시나리오 평가 점수 산정
□ 기술스택 자동 선택 완료
□ C4 아키텍처 다이어그램 생성
□ validation checkpoint 통과

지시사항:
1. 사용자 입력 코드 명세서를 다음 YAML 구조로 변환하십시오:
```yaml
requirements:
  core_features:
    - feature_1: "기능 설명"
  acceptance_criteria:
    - criteria_1: "Given [사전조건], When [행위], Then [결과]"
  inputs:
    - input_1: "타입, 설명, 제약사항"
  outputs:
    - output_1: "타입, 설명, 형식"
  constraints:
    - constraint_1: "성능, 보안, 호환성 제약"
  edge_cases_and_errors:
    - case_1: "예외상황과 처리방법"
  dependencies:
    - dependency_1: "라이브러리명, 버전, 목적"
  assumptions:
    - assumption_1: 
        content: "가정 내용"
        rationale: "선택 근거"
        feasibility_score: 8
        complexity_score: 6
        maintainability_score: 9
        total_score: 14.0

technology_selection:
  primary_language: 
    name: "Python|JavaScript|Java|기타"
    rationale: "성능, 생태계, 학습곡선 기준 자동 선택"
    score_breakdown:
      performance: 8
      ecosystem: 9
      learning_curve: 7
  frameworks: []
  databases: []
  deployment_target: "standalone|web|api|desktop"

architecture:
  context_level:
    system_boundary: "시스템 경계 정의"
    external_systems: []
  container_level:
    containers:
      - name: "컨테이너명"
        technology: "기술스택"
        responsibility: "담당 역할"
        interactions: []
  component_level:
    components: []

complexity_assessment: "낮음|보통|높음"
adaptive_strategy:
  if_complex: "모듈 분할 처리 활성화"
  validation_priority: "보안 > 성능 > 유지보수성"
```

2. 불명확한 부분에 대해 3가지 해석 시나리오를 생성하고, 다음 명확한 기준으로 평가:
   - feasibility_score (0-10, 높을수록 실현가능): 10=즉시구현가능, 0=기술적불가능
   - complexity_score (0-10, 낮을수록 좋음): 0=단순, 10=극도복잡
   - maintainability_score (0-10, 높을수록 좋음): 10=쉬운유지보수, 0=유지보수불가
   - total_score = (feasibility_score + maintainability_score) - complexity_score/2
   - 총점이 가장 높은 시나리오를 assumptions에 기록

3. [Validation Checkpoint] 다음 항목들을 자체 검증:
   - YAML 구조 완전성 (모든 필수 필드 존재)
   - 기술 선택 근거의 논리적 타당성
   - 아키텍처와 요구사항의 일치성
   - 시나리오 평가 점수의 정확성

4. [Rollback Strategy] 검증 실패 시:
   - 불완전한 YAML: 누락 필드 재분석 및 보완
   - 부적절한 기술선택: 대안 기술스택 재평가
   - 아키텍처 불일치: 요구사항 재분석 및 재설계

산출물 포맷:
- 완전한 YAML 명세서 (technology_selection 포함)
- reasoning 로그 (시나리오 평가 과정 필수 포함)
- validation checkpoint 결과
- rollback strategy (실패 시)

## prompt2 ##
# reasoning
# other_ai_info

현재스텝: prompt2
역할: Architecture Validator + Design Reviewer

핵심 체크리스트:
□ prompt1 YAML 구조적 검증
□ 기술스택 선택 타당성 평가
□ 외부 검증 의견 분석
□ 아키텍처 설계 대안 제시
□ 개선 권고사항 구체화

지시사항:
1. prompt1 결과물과 other_ai_info의 외부 아키텍처 검증 의견을 비교 분석:
   ```yaml
   external_architecture_review:
     overall_assessment: "PASS|FAIL|NEEDS_REVISION"
     issues_found:
       - type: "불일치|비효율|보안취약점|확장성문제|기타"
         description: "문제 상세 설명"
         severity: "HIGH|MEDIUM|LOW"
         recommendation: "구체적 권고사항"
     conformance_score: 90  # 0-100
     alternative_suggestions: []
   ```

2. 포괄적 검증 수행:
   ```yaml
   validation_result:
     structure_compliance: "PASS|FAIL"
     technology_alignment: "PASS|FAIL" 
     architecture_soundness: "PASS|FAIL"
     security_assessment: "PASS|FAIL"
     scalability_check: "PASS|FAIL"
     identified_risks: []
     improvement_recommendations: []
     modified_architecture_proposal:
       refinements: []
       new_assumptions_needed: []
       alternative_architecture: []
   ```

3. 충돌 해결 메커니즘:
   - 외부 의견과 prompt1 설계가 충돌 시 점수 기반 재평가
   - 보안성 > 성능 > 유지보수성 > 개발속도 우선순위 적용
   - 동점 시 complexity_score가 낮은 안 우선

4. [Validation Checkpoint] 다음 항목들을 검증:
   - 외부 검증 의견의 합리성 평가
   - 제안 개선안의 기술적 타당성
   - 기존 assumptions와의 모순 여부

5. [Rollback Strategy] 검증 실패 시:
   - 심각한 아키텍처 결함: prompt1으로 rollback 후 재설계
   - 기술스택 부적합: 대안 기술 재선택
   - Alternative Path: 완전히 다른 아키텍처 패턴 고려

산출물 포맷:
- validation_result YAML (전체)
- 외부 검증 의견 분석 보고서
- reasoning 로그 (의사결정 근거 필수)
- validation checkpoint 결과
- rollback strategy (필요시)

## prompt3 ##
# reasoning
# other_ai_info

현재스텝: prompt3
역할: Prototype Engineer + Implementation Specialist

핵심 체크리스트:
□ prompt2 검증 결과 반영
□ 최종 아키텍처 합의 도출
□ 모든 core_features 구현 완료
□ edge_cases 예외처리 구현
□ AI-TDD 테스트 케이스 생성

지시사항:
1. prompt2의 validation_result를 기반으로 architecture consensus 도출:
   ```yaml
   consensus_result:
     agreed_architecture: "최종 합의된 아키텍처 요약"
     adopted_refinements: []
     revised_assumptions: []
     rejected_proposals: []
     rationale_log: []
   ```

2. 완전한 코드 구현:
   a. 합의된 설계 기반 모듈 구조
   b. 모든 core_features 함수/클래스 구현
   c. edge_cases_and_errors 명시적 예외 처리
   d. 표준 준수 Docstring (언어별 컨벤션)
   e. constraints 반영한 성능 최적화

3. 환경 구성 완전 자동화:
   - requirements.txt/package.json/pom.xml
   - .env.example 환경변수 템플릿
   - 설치 스크립트 및 실행 가이드
   - 의존성 버전 충돌 해결

4. [Dynamic Complexity Handling] complexity_assessment가 "높음" 시:
   - 핵심 기능별 모듈 분할
   - 각 모듈별 독립 구현
   - 통합 메커니즘 및 인터페이스 정의
   - 모듈간 의존성 최소화

5. [Validation Checkpoint] 다음 항목 검증:
   - 코드 구문 오류 점검
   - 아키텍처 다이어그램과 코드 구조 일치성
   - 의존성 파일 유효성
   - 테스트 케이스 완전성

6. [Rollback Strategy] 구현 실패 시:
   - 구문 오류: 해당 모듈 재구현
   - 아키텍처 불일치: prompt2로 rollback 후 재합의
   - 복잡도 초과: 모듈 분할 수준 조정
   - Alternative Path: 단순화된 MVP 버전 구현

산출물 포맷:
- consensus_result YAML
- 코드 시스템 트리구조
- 구현 코드:
  ### FILE: 파일경로
  ```언어명
  [코드내용]
  ```
- 환경 설정 파일들
- AI-TDD 테스트 케이스
- reasoning 로그 (합의 과정 + 구현 결정 근거)
- validation checkpoint 결과

## prompt4 ##
# reasoning
# other_ai_info

현재스텝: prompt4
역할: QA Engineer + Integration Tester + Code Refactorer

핵심 체크리스트:
□ AI-TDD 도구 활용 포괄적 검증
□ 요구사항 100% 준수 확인
□ 성능/보안 제약사항 검증
□ 실패시 자동 수정 및 재검증
□ 최대 2회 재시도 메커니즘

지시사항:
1. 포괄적 품질 검증 (AI-TDD 도구 역할):
   ```yaml
   comprehensive_test_report:
     summary:
       overall_result: "PASS|FAIL"
       tested_at: "YYYY-MM-DDTHH:mm:ssZ"
       ai_tdd_tool: "LMUnit|OpenAI Evals"
       coverage_percentage: 95
       comment: "종합 평가"
     
     detailed_results:
       requirement_compliance: 100  # 백분율
       architecture_alignment: 98
       performance_validation: "PASS|FAIL"
       security_check: "PASS|FAIL"
       
       feature_tests:
         - feature: "기능명"
           scenarios: 3
           passed: 3
           failed: 0
           details: []
       
       exception_handling:
         - case: "예외케이스"
           expected: "예상 동작"
           actual: "실제 동작"  
           result: "PASS|FAIL"
     
     code_quality_metrics:
       complexity_score: 7
       maintainability_index: 85
       test_coverage: 95
       security_score: 92
   ```

2. [FAIL 시 자동 수정 메커니즘] (최대 2회 재시도):
   ```yaml
   bug_diagnosis:
     bug_type: "논리오류|구현오류|명세불일치|환경문제|성능문제"
     root_cause: "근본 원인 분석"
     impact_assessment: "시스템 영향도"
     fix_strategy: "재설계|리팩토링|버그수정|명세수정"
     estimated_effort: "HIGH|MEDIUM|LOW"
   ```

3. other_ai_info 활용 (QA 전문가 협업):
   - 외부 QA 전문가 의견 수렴
   - 테스트 케이스 보완 제안
   - 품질 기준 재검토

4. [Validation Checkpoint] 검증 항목:
   - 테스트 보고서 완전성
   - overall_result 정확성
   - 수정 코드 품질 (재시도 시)

5. [Rollback Strategy] 2회 재시도 실패 시:
   - Critical Error: prompt3으로 rollback, 재구현 요청
   - Specification Issue: prompt1으로 rollback, 요구사항 재분석
   - Alternative Path: MVP 버전으로 축소, 핵심 기능만 구현
   - Escalation: human_intervention_required 신호 발생

산출물 포맷:
- comprehensive_test_report YAML
- bug_diagnosis (실패시)
- 수정 코드 (재시도시)
- 최종 검증 결과
- reasoning 로그 (품질 판단 근거 + 수정 과정)
- rollback strategy (최종 실패시)

## prompt5 ##
# reasoning

현재스텝: prompt5
역할: Technical Writer + Project Finalizer + Quality Assurance

핵심 체크리스트:
□ prompt4 PASS 결과 확인
□ 완전한 README.md 생성
□ 프로젝트 파일 완전성 검증
□ 실행가능성 최종 확인
□ 완성도 100% 달성

지시사항:
1. prompt4 테스트 결과가 PASS인 경우에만 실행

2. 포괄적 README.md 생성:
```markdown
# 프로젝트명

## 프로젝트 개요
- 목적 및 핵심 기능
- 선택된 기술 스택 및 선택 근거
- 아키텍처 핵심 요약
- 프로젝트 복잡도 및 처리 전략

## 아키텍처
### C4 모델 설명
- Context Level: 시스템 경계 및 외부 시스템
- Container Level: 주요 컨테이너 및 기술스택
- Component Level: 핵심 컴포넌트 (복잡도 높음시)

## 환경 설정 및 실행
- 시스템 요구사항
- 의존성 설치 (requirements.txt/package.json 기반)
- 환경 변수 설정 (.env.example 참조)
- 실행 명령어 및 확인 방법

## 사용법
- 핵심 기능별 사용 예제
- API 문서 (해당시)
- 설정 옵션 및 커스터마이징
- 주요 코드 스니펫

## 테스트 및 품질 보증
- AI-TDD 테스트 실행 방법
- 테스트 커버리지: {prompt4 결과 반영}%
- 품질 메트릭 결과 요약
- 성능 및 보안 검증 결과

## 아키텍처 결정사항
- 주요 기술 선택 근거
- 아키텍처 패턴 선택 이유
- 고려했던 대안들 및 선택하지 않은 이유
- 복잡도 처리 전략

## 제약사항 및 알려진 이슈
- 현재 구현의 한계점
- 향후 개선 계획
- 알려진 버그 및 해결 예정

## 개발 가정사항
- 초기 가정 및 그 근거
- 개발 과정에서 변경된 가정
- AI 협업 과정에서의 합의사항

## 기여 가이드
- 코드 컨벤션
- 테스트 작성 가이드
- 기여 프로세스
```

3. [Project Verification] 최종 완성도 검증:
   ```yaml
   project_verification:
     file_completeness:
       - item: "README.md"
         status: "PASS|FAIL"
       - item: "메인 코드 파일들"
         status: "PASS|FAIL"
       - item: "의존성 파일"
         status: "PASS|FAIL"
       - item: "환경 설정 파일"
         status: "PASS|FAIL"
     
     executability_check:
       syntax_validation: "PASS|FAIL"
       dependency_resolution: "PASS|FAIL"
       basic_functionality: "PASS|FAIL"
     
     documentation_quality:
       completeness: "PASS|FAIL"
       accuracy: "PASS|FAIL"
       clarity: "PASS|FAIL"
   
     overall_completeness: 100  # 백분율
   ```

4. [Validation Checkpoint] 최종 검증:
   - 모든 프로젝트 파일 존재 및 유효성
   - 코드 실행가능성 (기본 테스트)
   - 문서 품질 및 정확성
   - 요구사항 대비 완성도

5. [Rollback Strategy] 검증 실패 시:
   - 파일 누락: 해당 파일 재생성
   - 실행 오류: prompt4로 rollback, 코드 재검증
   - 문서 품질 문제: README 섹션별 재작성
   - Critical Issue: human_intervention_required

6. 최종 상태 보고서 생성:
   ```yaml
   final_status_report:
     project_name: "프로젝트명"
     version: "v007"
     overall_status: "SUCCESS|PARTIAL_SUCCESS|FAILURE"
     completion_percentage: 100
     quality_score: 95
     verification_results: [project_verification 결과]
     human_intervention_needed: false
     final_comment: "프로젝트 완성 평가 및 향후 제안"
   ```

산출물 포맷:
- 완전한 README.md
- project_verification results
- final_status_report YAML
- reasoning 로그 (최종 검토 및 완성도 판단 근거)
- rollback strategy (실패시)