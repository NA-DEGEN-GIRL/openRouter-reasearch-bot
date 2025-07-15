import os
import sys
import time
import re

def find_prompt_files(directory="prompts"):
    """'prompts' 디렉토리에서 .md 파일 목록을 찾아서 반환"""
    # Find and return a list of .md files in the 'prompts' directory.
    if not os.path.exists(directory):
        print(f"오류: '{directory}' 디렉토리를 찾을 수 없습니다.\nError: Directory '{directory}' not found.")
        return []
    return [f for f in os.listdir(directory) if f.endswith('.md')]

def get_project_name_from_prompt(filepath):
    """지정된 프롬프트 파일에서 '## project name ##' 섹션을 찾아 프로젝트 이름을 파싱"""
    # Parse the project name from the '## project name ##' section in the specified prompt file.
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            match = re.search(r"##\s*project name\s*##\s*(.*?)\s*(?:\n##|$)", content, re.IGNORECASE | re.DOTALL)
            if match:
                return match.group(1).strip()
        return None
    except FileNotFoundError:
        return None

def load_ai_models(filepath="ai_models.txt"):
    """ai_models.txt 파일에서 모델 목록을 읽어옴"""
    # Reads the list of models from ai_models.txt.
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            models = [line.strip() for line in f if line.strip()]
        return models if models else None
    except FileNotFoundError:
        return None

def get_model_nickname(model_id):
    """모델 ID에서 식별하기 쉬운 별명을 추출"""
    # Extracts a user-friendly nickname from the model ID.
    return model_id.split('/')[-1]

def tail_file(filepath):
    """파일의 새로운 내용을 실시간으로 출력"""
    # Outputs new content of a file in real-time.
    print(f"\n--- 로그 파일 '{os.path.relpath(filepath)}' 감시 시작 ---\n--- Starting to watch log file '{os.path.relpath(filepath)}' ---\n")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            f.seek(0, 2)
            while True:
                line = f.readline()
                if not line:
                    time.sleep(0.1)
                    continue
                sys.stdout.write(line)
                sys.stdout.flush()
    except FileNotFoundError:
         print(f"오류: 로그 파일 '{filepath}'를 찾을 수 없습니다.\nError: Log file '{filepath}' not found.")
    except KeyboardInterrupt:
        print("\n뷰어를 종료합니다.\nExiting viewer.")
        sys.exit(0)

def main():
    # 1. 프롬프트 파일 선택
    # 1. Select prompt file.
    prompt_files = find_prompt_files()
    if not prompt_files:
        print("오류: 'prompts' 디렉토리에 프롬프트 파일(.md)이 없습니다.\nError: No prompt files (.md) found in the 'prompts' directory.")
        sys.exit(1)
    
    print("로그를 확인할 작업을 선택하세요:\nSelect a task to watch logs for:\n")
    for i, filename in enumerate(prompt_files):
        print(f"  [{i + 1}] {filename}")

    selected_prompt_path = None
    while True:
        try:
            choice = input(f"\n번호를 입력하세요 (1-{len(prompt_files)}): \nEnter a number (1-{len(prompt_files)}): ")
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(prompt_files):
                selected_prompt_path = os.path.join("prompts", prompt_files[choice_idx])
                break
            else:
                print("잘못된 번호입니다. 다시 입력해주세요.\nInvalid number. Please try again.")
        except (ValueError, IndexError):
            print("잘못된 입력입니다. 숫자를 입력해주세요.\nInvalid input. Please enter a number.")
        except (KeyboardInterrupt, EOFError):
            print("\n선택을 취소하고 종료합니다.\nSelection cancelled. Exiting.")
            sys.exit(0)

    # 2. 프로젝트 이름 가져오기
    # 2. Get project name.
    project_name = get_project_name_from_prompt(selected_prompt_path)
    if not project_name:
        print(f"오류: '{selected_prompt_path}' 파일에서 '## project name ##' 섹션을 찾을 수 없습니다.\nError: Could not find '## project name ##' section in '{selected_prompt_path}'.")
        sys.exit(1)

    # 3. 모델 선택
    # 3. Select model.
    ai_models = load_ai_models()
    if not ai_models:
        print("오류: 'ai_models.txt' 파일을 찾을 수 없거나 내용이 비어있습니다.\nError: 'ai_models.txt' not found or is empty.")
        sys.exit(1)

    print("\n실시간으로 확인할 모델을 선택하세요:\nSelect a model to watch in real-time:\n")
    for i, model_id in enumerate(ai_models):
        print(f"  [{i + 1}] {get_model_nickname(model_id)}")
    
    selected_model_nickname = None
    while True:
        try:
            choice = input(f"\n번호를 입력하세요 (1-{len(ai_models)}): \nEnter a number (1-{len(ai_models)}): ")
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(ai_models):
                selected_model_nickname = get_model_nickname(ai_models[choice_idx])
                break
            else:
                print("잘못된 번호입니다. 다시 입력해주세요.\nInvalid number. Please try again.")
        except (ValueError, IndexError):
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
    print("봇이 실행되면 로그 출력이 시작됩니다. (종료: Ctrl+C)")
    print("Log output will begin when the bot is running. (Exit: Ctrl+C)")
    
    while not os.path.exists(log_file_path):
        time.sleep(1)

    tail_file(log_file_path)

if __name__ == "__main__":
    main()
