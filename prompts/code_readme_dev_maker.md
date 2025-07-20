## project name ##
README DEV docs maker

## metadata ##
- version: 001
- description: 코드 시스템의 README.md와 DEV.md를 작성

## context ##
여기에 언급하고자하는 바를 작성

## system prompt ##
당신은 소프트웨어 개발과 문서화 작업에 능숙한 전문가

## prompt1 ##
# code ./main.py
# code ./localization.py
# code ./config/config.py
# code ./config/constants.py
# code ./core/exceptions.py
# code ./core/models.py
# code ./core/orchestrator.py
# code ./services/ai_client.py
# code ./services/file_handler.py
# code ./services/model_provider.py
# code ./services/prompt_parser.py
# code ./utils/logger.py
현재 스텝: prompt1
주어진 코드를 분석
README.md 와 DEV.md가 첨부되어있다면 이도 참고하여 확인
context 섹션에 정보가 있다면 이를 확인
이를 토대로 README.md DEV.md 작성
작성언어와 순서:
1. README.md
 a. 한글
 b. 영문
2. DEV.md
 a. 한글
 b. 영문

문서화 원칙:
- 초보자도 이해 가능한 상세 설명
- 실제 사용 예시 포함
- 기본 입력 예시가 있다면, 이를 상세히 설명할것
- 입력 파일의 규칙이 있따면 상세히 설명할것

[README.md 구성]
1. 프로젝트 소개: 장황하게 부풀려서 소개하지 말것, 깔끔하고 담백하게 작성
2. 주요 기능
3. 설치 가이드
4. 사용법 및 예시: 기본 예시 인풋이 있다면 반드시 설명, 예시 인풋에 다양한 옵션이 있다면 상세히 설명
5. 의존성 및 요구사항
6. 문제 해결 (FAQ)

[DEV.md 구성]
1. 아키텍처 개요
2. 디렉토리 구조 설명
3. 핵심 컴포넌트 상세
   - 역할과 책임
   - 주요 메서드/함수
   - 코드 스니펫
4. 설계 결정 및 트레이드오프
   - 왜 이 구조를 선택했는가?
   - 고려했던 대안들
   - 선택의 이유
5. 리팩토링 히스토리
6. 외부 library들에 대한 간단한 설명. 대안이 있다면 그에 대해서도 언급.
7. 향후 확장 가이드


## prompt2 ##
# other_ai_info
현재 스텝: prompt2
prompt1의 다른 AI들의 README.md와 DEV.md를 살펴본뒤, 너가 작성한 README 및 DEV를 개선
개선사항에 대해서 간단히 언급 후 prompt1에서의 문서 규칙화에 따라 전체 README.md와 DEV.md를 작성
요약하지말고 온전한 문서를 작성할것