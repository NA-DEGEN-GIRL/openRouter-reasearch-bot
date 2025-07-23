## project name ##
ask_anything

## metadata ##
- version: 001
- description: ask anything!

## system prompt ##
You are a helpful AI assistant.

## prompt1 ##
간단한 파이썬 프로그램을 짜줘.
프로그램을 실행하면 폴더를 입력할수있게하고 cli처럼 탭기능 활성화시켜서 탭누르면 하위 폴더들 선택할수있게하고
그렇게해서 폴더를 선택하면 (선택하는 방법을 적당히 짜줘)
해당 폴더 하위에 있는 모든 파일을 상대적 path로 출력해줘
예를들면
./src/main.py
./src/utils.py
./README.md
뭐 이런식으로
그리고 트리 구조도 출력해주고
둘다 적당한 txt 파일에 출력시켜줘
그리고 해당 프로그램에서 ignore할수있는 파라미터를 안에 작성하게 해줘 따로 인풋으로 받지말고
ignore_pattern = ['*.log',...] 뭐 이런식이면 되려나? 암튼 적당히 짜줘

## prompt2 ##
# other_ai_info
다른 ai의 결과를 참고해서 개선시켜줘