import os
import sys
import time
import argparse
import re

def get_project_name_from_prompt(filepath="prompt.md"):
    # prompt.md 파일에서 프로젝트 이름만 파싱
    # Parses only the project name from the prompt.md file.
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            in_project_info = False
            for line in f:
                if "## project info ##" in line.lower():
                    in_project_info = True
                    continue
                if in_project_info and line.strip():
                    # 섹션 시작 후 첫 번째 비어있지 않은 줄이 프로젝트 이름
                    # The first non-empty line after the section starts is the project name.
                    return line.strip()
        return None
    except FileNotFoundError:
        return None

def load_ai_models(filepath="ai_models.txt"):
    # ai_models.txt 파일에서 모델 목록을 읽어옴
    # Reads the list of models from ai_models.txt.
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            models = [line.strip() for line in f if line.strip()]
        return models if models else None
    except FileNotFoundError:
        return None

def get_model_nickname(model_id):
    # 모델 ID에서 식별하기 쉬운 별명을 추출
    # Extracts a user-friendly nickname from the model ID.
    return model_id.split('/')[-1]

def tail_file(filepath):
    # 파일의 새로운 내용을 실시간으로 출력
    # Outputs new content of a file in real-time.
    print(f"\n--- 로그 파일 '{os.path.relpath(filepath)}' 감시 시작 ---\n--- Starting to watch log file '{os.path.relpath(filepath)}' ---\n")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            # 파일이 처음부터 보이도록 시작 위치를 0으로 설정
            # Set the starting position to 0 to see the file from the beginning.
            f.seek(0)
            while True:
                line = f.readline()
                if not line:
                    time.sleep(0.1) # 잠시 대기 / Wait for a moment
                    continue
                sys.stdout.write(line)
                sys.stdout.flush()
    except FileNotFoundError:
         print(f"오류: 로그 파일 '{filepath}'를 찾을 수 없습니다.\nError: Log file '{filepath}' not found.")
    except KeyboardInterrupt:
        print("\n뷰어를 종료합니다.\nExiting viewer.")
        sys.exit(0)

def main():
    # 1. 프로젝트 이름 자동 감지
    # 1. Auto-detect project name.
    project_name = get_project_name_from_prompt()
    if not project_name:
        print("오류: 'prompt.md' 파일에서 '## project info ##' 섹션과 프로젝트 이름을 찾을 수 없습니다.\nError: Could not find '## project info ##' section and project name in 'prompt.md'.")
        sys.exit(1)

    # 2. 사용 가능한 모델 목록 로드
    # 2. Load the list of available models.
    ai_models = load_ai_models()
    if not ai_models:
        print("오류: 'ai_models.txt' 파일을 찾을 수 없거나 내용이 비어있습니다.\nError: 'ai_models.txt' not found or is empty.")
        sys.exit(1)

    # 3. 사용자에게 모델 선택 메뉴 표시
    # 3. Display the model selection menu to the user.
    print("실시간으로 확인할 모델을 선택하세요:\nSelect a model to watch in real-time:\n")
    for i, model_id in enumerate(ai_models):
        print(f"  [{i + 1}] {get_model_nickname(model_id)}")
    
    selected_model_nickname = None
    while True:
        try:
            choice = input(f"\n번호를 입력하세요 (1-{len(ai_models)}): \nEnter a number (1-{len(ai_models)}): ")
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(ai_models):
                selected_model_id = ai_models[choice_idx]
                selected_model_nickname = get_model_nickname(selected_model_id)
                break
            else:
                print("잘못된 번호입니다. 다시 입력해주세요.\nInvalid number. Please try again.")
        except ValueError:
            print("숫자를 입력해야 합니다.\nPlease enter a number.")
        except (KeyboardInterrupt, EOFError):
            print("\n선택을 취소하고 종료합니다.\nSelection cancelled. Exiting.")
            sys.exit(0)

    # 4. 로그 추적 시작
    # 4. Start tracking the log.
    project_folder = re.sub(r'[^\w-]', '_', project_name).lower()
    log_file_path = os.path.join("projects", project_folder, "live_logs", f"{selected_model_nickname}.log")
    
    print(f"\n'{project_name}' 프로젝트의 '{selected_model_nickname}' 모델 로그를 탐색합니다...")
    print(f"Searching for logs of the '{selected_model_nickname}' model for the '{project_name}' project...")
    print(f"감시할 파일: {log_file_path}")
    print(f"File to watch: {log_file_path}")
    print("research_bot.py가 실행되면 로그 출력이 시작됩니다. (종료: Ctrl+C)")
    print("Log output will begin when research_bot.py is running. (Exit: Ctrl+C)")
    
    # 로그 파일이 생성될 때까지 대기
    # Wait for the log file to be created.
    while not os.path.exists(log_file_path):
        time.sleep(1)

    # 파일이 존재하면 즉시 추적 시작
    # Start tracking immediately if the file exists.
    tail_file(log_file_path)

if __name__ == "__main__":
    main()
