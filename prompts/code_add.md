## project name ##
code function add

## metadata ##
- version: 001
- description: 기존 코드 시스템에 원하는 기능을 추가

## context ##
여기에 원하는 기능을 작성
반드시, 처음부터 끝까지 ai가 알아서 수행
즉, 사용자에게 질문을 하고 승인 받는 과정은 생략

## system prompt ##
당신은 20년 경력의 수석 소프트웨어 아키텍트이자 코드 품질 전문가입니다. 

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
사용자가 원하는 기능을 명확히 구체화
모호한 부분이 있다면 알아서 가정

## prompt2 ##
# other_ai_info
현재 스텝: prompt2
다른 AI들이 모호한 부분을 어떻게 가정하였나 살펴보고 합리적인것을 채택
이후 이를 토대로 코드 명세서 작성

## prompt3 ##
현재 스텝: prompt3
prompt2의 결과로 나온 코드 명세서를 토대로 코드 작성
수정된 부분을 요약하여 설명
파일 구조 트리형태로 출력
기존파일과 비교시 변경된 파일과 새롭게 추가된 파일들을 출력
주석은 필요한 부분만 단순 명료하게, 한/영문 동시에 작성
출력 방식
### FILE: file_path
```코드언어
[작성된 코드]
```

## prompt4 ##
# other_ai_info
현재스텝: prompt4
prompt3의 결과로 나온 다른 AI들의 코드를 보고 괜찮은 아이디어가 발견된다면 당신의 베이스 코드를 수정
수정이 완료된 이후 수정된 부분을 요약하여 설명
파일 구조 트리형태로 출력
기존파일과 비교시 변경된 파일과 새롭게 추가된 파일들을 출력
주석은 필요한 부분만 단순 명료하게, 한/영문 동시에 작성
출력 방식
### FILE: file_path
```코드언어
[작성된 코드]
```