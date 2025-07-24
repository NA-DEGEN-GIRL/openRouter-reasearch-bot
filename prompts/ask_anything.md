## project name ##
ask_anything

## ai models ##
openai/gpt-4.1
google/gemini-2.5-pro
anthropic/claude-opus-4

## metadata ##
- version: 001
- description: ask anything!

## system prompt ##
You are a helpful AI assistant.

## prompt1 ##
# doc ./prompts/research.md
# doc ./prompts/batch_run/research_batch.md
첨부된 research.md를 input으로 돌리는 프로그램의 함수가 main.py라고 해보자.
명령어는 `python main.py -l ko -p research.md` 인 상황이야.
근데 이걸 batch 런을 돌리는 스크립트(혹은 파이썬 코드) 짜고 싶은데 research.md의 내용을 바꿔야해
research_batch.md에 있는 파일들 목록들에 대해서 쭉 실행을 할꺼야.
바꿀 내용1:
project name 섹션하에 있는건 **파일명**으로 하면돼.
예를들어 ./prompts/web3_projects/digitalx.txt 이 경우엔 project name 섹션에 digitalx가 들어가면돼.
그리고 
바꿀 내용2:
prompt1 섹션하에 doc 뒤에 있는 path를 이제 ./prompts/web3_projects/digitalx.txt 이런 식으로 수정하면돼.
그리고 나서 명령어 실행. 다 끝나고 나면 그다음 프로젝트에 대해서 동일하게 실행

## prompt2 ##
# other_ai_info
다른 ai들이 짠 스크립트나 코드를 보고 괜찮은 아이디어가 있으면 보완 개선해줘