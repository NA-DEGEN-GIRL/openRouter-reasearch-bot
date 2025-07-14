import os
import re
import argparse
import sys
import concurrent.futures
import shutil
from dotenv import load_dotenv
from openai import OpenAI, APITimeoutError, APIConnectionError
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type

# --- CONFIGURATION ---

# 컨텍스트 히스토리 유지 갯수 (user/assistant 쌍 기준)
# Number of context history pairs (user/assistant) to maintain.
TRIMMED_HISTORY_COUNT = 25 

# UI 텍스트 현지화 / UI Text Localization
STRINGS = {
    'ko': {
        "select_language": "언어를 선택하세요 (1: 한국어, 2: English): ",
        "invalid_input": "잘못된 입력입니다. 1 또는 2를 입력하세요.",
        "mode_selected": "\n'{lang_upper}' 모드로 실행합니다. 프롬프트 파일: '{prompt_filepath}'",
        "error_no_models": "오류: '{filepath}'에 사용할 모델이 지정되지 않았음.",
        "error_file_not_found": "오류: '{filepath}' 파일을 찾을 수 없음.",
        "error_no_headers": "오류: '{filepath}'에서 '## 섹션명 ##' 형식의 헤더를 찾을 수 없음.",
        "error_no_project_info": "오류: '## project info ##' 섹션을 찾을 수 없음.",
        "error_no_api_key": "오류: .env 파일에 OPENROUTER_API_KEY가 설정되지 않았음.",
        "research_start": "🚀 프로젝트 '{project_name}' 리서치를 시작합니다. (백그라운드 로깅 전용)",
        "output_folder_info": "📂 결과는 '{output_dir}' 폴더에 저장됩니다.",
        "live_log_info": "👁️  실시간 로그는 `python view_log.py`로 확인하세요.",
        "models_in_use": "🤖 사용할 모델: {models_list}",
        "collaboration_disabled": "🤝 AI 협업 기능이 비활성화되었습니다.",
        "prompt_execution": "▶️ 프롬프트 {prompt_id}/{total_prompts} 실행: {prompt_name}",
        "reasoning_activated": "   ✨ Reasoning 모드가 활성화되었습니다.",
        "request_start": "   (총 {num_models}개 모델에 동시 요청 및 로깅 시작...)",
        "system_prompt": "당신은 전문 블록체인 프로젝트 분석가입니다. 반드시 웹 검색을 통해 가장 정확한 최신 정보를 찾아야 합니다.",
        "log_prompt_header": "\n\n{divider} 프롬프트 {prompt_id} ({prompt_name}) {divider}\n\n",
        "log_reasoning_header": "\n--- [생각 과정] ---\n",
        "log_error_header": "\n\n--- 오류 ---\n{error_message}\n",
        "log_error_message": "오류 발생: {e}",
        "task_completed": "✅ '{nick}' 작업 완료.",
        "task_failed": "❌ '{nick}' 작업 실패.",
        "task_error": "❌ '{model_nickname}' 작업 처리 중 최종 오류: {e}",
        "prompt_finished": "\n--- 프롬프트 {prompt_id} 모든 작업 완료 ---",
        "all_finished": "✅ 모든 리서치 과정이 완료되었습니다."
    },
    'en': {
        "select_language": "Select language (1: 한국어, 2: English): ",
        "invalid_input": "Invalid input. Please enter 1 or 2.",
        "mode_selected": "\nRunning in '{lang_upper}' mode. Prompt file: '{prompt_filepath}'",
        "error_no_models": "Error: No models specified in '{filepath}'.",
        "error_file_not_found": "Error: File not found at '{filepath}'.",
        "error_no_headers": "Error: Could not find headers in '## Section ##' format in '{filepath}'.",
        "error_no_project_info": "Error: '## project info ##' section not found.",
        "error_no_api_key": "Error: OPENROUTER_API_KEY is not set in the .env file.",
        "research_start": "🚀 Starting research for project '{project_name}'. (Background Logging Only)",
        "output_folder_info": "📂 Results will be saved in the '{output_dir}' folder.",
        "live_log_info": "👁️  Check live logs with `python view_log.py`.",
        "models_in_use": "🤖 Models in use: {models_list}",
        "collaboration_disabled": "🤝 AI collaboration is disabled.",
        "prompt_execution": "▶️ Executing Prompt {prompt_id}/{total_prompts}: {prompt_name}",
        "reasoning_activated": "   ✨ Reasoning mode activated.",
        "request_start": "   (Starting concurrent requests and logging for {num_models} models...)",
        "system_prompt": "You are a professional blockchain project researcher. You must use web search to find the most up-to-date and accurate information.",
        "log_prompt_header": "\n\n{divider} PROMPT {prompt_id} ({prompt_name}) {divider}\n\n",
        "log_reasoning_header": "\n--- [REASONING PROCESS] ---\n",
        "log_error_header": "\n\n--- ERROR ---\n{error_message}\n",
        "log_error_message": "Error occurred: {e}",
        "task_completed": "✅ Task for '{nick}' completed.",
        "task_failed": "❌ Task for '{nick}' failed.",
        "task_error": "❌ Final error while processing task for '{model_nickname}': {e}",
        "prompt_finished": "\n--- All tasks for Prompt {prompt_id} are complete ---",
        "all_finished": "✅ All research processes have been completed."
    }
}

# --- HELPER FUNCTIONS ---

def load_ai_models(filepath="ai_models.txt"):
    # ai_models.txt 파일에서 모델 목록을 읽어옴
    # Reads the list of models from ai_models.txt
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            models = [line.strip() for line in f if line.strip()]
        if not models:
            print(f"Error: No models specified in '{filepath}'.")
            sys.exit(1)
        return models
    except FileNotFoundError:
        print(f"Error: File not found at '{filepath}'.")
        sys.exit(1)

def parse_prompt_file(filepath, loc_strings):
    # prompt.md 파일을 파싱하여 프로젝트 정보, 프롬프트, 각종 옵션을 반환
    # Parses the prompt.md file to return project info, prompts, and various options.
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(loc_strings["error_file_not_found"].format(filepath=filepath))
        sys.exit(1)

    headers = re.findall(r"##\s*(.*?)\s*##", content)
    parts = re.split(r"##\s*.*?\s*##", content)[1:]

    if not headers:
        print(loc_strings["error_no_headers"].format(filepath=filepath))
        sys.exit(1)

    project_info_text = None
    prompts = []
    for header, text in zip(headers, parts):
        clean_text = text.strip()
        if header.lower() == "project info":
            project_info_text = clean_text
        elif header.lower().startswith("prompt"):
            use_reasoning = '# reasoning' in clean_text.lower()
            has_other_ai_info = '# other_ai_info' in clean_text.lower()
            prompt_content = re.sub(r'#\s*(reasoning|other_ai_info)', '', clean_text, flags=re.IGNORECASE).strip()
            
            prompts.append({
                'id': int(re.search(r'\d+', header).group()), 
                'name': header.lower(), 
                'text': prompt_content,
                'use_reasoning': use_reasoning,
                'has_other_ai_info': has_other_ai_info
            })

    if not project_info_text:
        print(loc_strings["error_no_project_info"])
        sys.exit(1)

    project_name = project_info_text.split('\n', 1)[0].strip()
    return project_name, project_info_text, sorted(prompts, key=lambda x: x['id'])

def print_divider(char="=", length=80):
    # 구분선 출력
    # Prints a divider line.
    print(char * length)

def get_model_nickname(model_id):
    # 모델 ID에서 식별하기 쉬운 별명을 추출
    # Extracts a user-friendly nickname from the model ID.
    return model_id.split('/')[-1]

# --- API CALL & PROCESSING FUNCTIONS ---

@retry(
    wait=wait_fixed(5),
    stop=stop_after_attempt(2),
    retry=retry_if_exception_type((APITimeoutError, APIConnectionError)),
    reraise=True
)
def get_ai_response_stream(client, model, messages, extra_body=None):
    # OpenRouter API를 호출하고 스트림 객체를 반환
    # Calls the OpenRouter API and returns a stream object.
    return client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
        timeout=180,
        extra_body=extra_body or {}
    )

def process_and_log_request(args_tuple):
    # 모델 요청, 실시간 로깅, 결과 반환을 병렬로 처리하는 작업자 함수
    # Worker function that handles a single model request, live logging, and returns the result concurrently.
    client, model, messages, output_path, live_log_path, api_params, loc_strings = args_tuple
    model_nickname = get_model_nickname(model)
    full_response = ""
    
    try:
        stream = get_ai_response_stream(client, model, messages, extra_body=api_params)
        
        with open(live_log_path, 'a', encoding='utf-8') as log_file:
            # Reasoning 모드가 활성화된 경우, 로그에 헤더 추가
            # If reasoning mode is active, add a header to the log.
            if api_params.get('reasoning'):
                log_file.write(loc_strings["log_reasoning_header"])
                log_file.flush()

            for chunk in stream:
                delta = chunk.choices[0].delta
                
                # 'reasoning' 필드가 있는지 확인하고 로그에 기록
                # Check for 'reasoning' field and log it.
                if hasattr(delta, 'reasoning') and delta.reasoning:
                    log_file.write(delta.reasoning)
                    log_file.flush()

                # 'content' 필드가 있는지 확인하고 로그 및 최종 응답에 기록
                # Check for 'content' field, log it, and append to the final response.
                if delta.content:
                    full_response += delta.content
                    log_file.write(delta.content)
                    log_file.flush()
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(full_response)
        
        return (model_nickname, full_response, messages[-1]['content'])

    except Exception as e:
        error_message = loc_strings["log_error_message"].format(e=e)
        with open(live_log_path, 'a', encoding='utf-8') as log_file:
            log_file.write(loc_strings["log_error_header"].format(error_message=error_message))
        return (model_nickname, None, messages[-1]['content'])

# --- MAIN LOGIC ---

def main():
    # 메인 실행 함수
    # Main execution function.
    parser = argparse.ArgumentParser(description="An automated project research bot using AI models.")
    parser.add_argument(
        '--lang', '-l',
        type=str,
        choices=['ko', 'en'],
        help="Select language (ko/en). If not specified, an interactive prompt will be shown."
    )
    parser.add_argument(
        '--prompt', '-p',
        type=str,
        help="Specify a custom prompt file to use (e.g., 'prompt_en.md'). Overrides the default based on language selection."
    )
    parser.add_argument(
        '--no-collaboration',
        action='store_true',
        help="Skips the collaboration step where AIs reference each other's answers."
    )
    args = parser.parse_args()

    # 언어 선택 로직 / Language selection logic
    lang = args.lang
    if not lang:
        while True:
            choice = input(STRINGS['en']["select_language"]) # Show prompt in both languages
            if choice == '1':
                lang = 'ko'
                break
            elif choice == '2':
                lang = 'en'
                break
            else:
                print(STRINGS['en']["invalid_input"])
    
    loc_strings = STRINGS[lang]
    # 프롬프트 파일 경로 결정 / Determine prompt file path
    prompt_filepath = args.prompt if args.prompt else ('prompt_en.md' if lang == 'en' else 'prompt.md')
    print(loc_strings["mode_selected"].format(lang_upper=lang.upper(), prompt_filepath=prompt_filepath))

    load_dotenv()
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print(loc_strings["error_no_api_key"]); sys.exit(1)

    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)

    ai_models = load_ai_models()
    project_name, project_info, prompts = parse_prompt_file(prompt_filepath, loc_strings)
    
    project_folder_name = re.sub(r'[^\w-]', '_', project_name).lower()
    output_dir = f"projects/{project_folder_name}"
    live_log_dir = os.path.join(output_dir, "live_logs")
    
    if os.path.exists(live_log_dir):
        shutil.rmtree(live_log_dir)
    os.makedirs(live_log_dir, exist_ok=True)
    
    print_divider()
    print(loc_strings["research_start"].format(project_name=project_name))
    print(loc_strings["output_folder_info"].format(output_dir=output_dir))
    print(loc_strings["live_log_info"])
    print(loc_strings["models_in_use"].format(models_list=', '.join([get_model_nickname(m) for m in ai_models])))
    if args.no_collaboration: print(loc_strings["collaboration_disabled"])
    print_divider()

    model_histories = {get_model_nickname(m): [] for m in ai_models}
    last_turn_responses = {}
    
    for i, prompt_data in enumerate(prompts):
        prompt_id, prompt_name, prompt_text = prompt_data['id'], prompt_data['name'], prompt_data['text']
        use_reasoning = prompt_data.get('use_reasoning', False)
        has_other_ai_info = prompt_data.get('has_other_ai_info', False)
        is_last_prompt = (i == len(prompts) - 1)
        
        current_prompt_responses = {}
        
        print(f"\n\n"); print_divider(char="*")
        print(loc_strings["prompt_execution"].format(prompt_id=prompt_id, total_prompts=len(prompts), prompt_name=prompt_name))
        if use_reasoning:
            print(loc_strings["reasoning_activated"])
        print(loc_strings["request_start"].format(num_models=len(ai_models)))
        
        future_to_model = {}
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(ai_models)) as executor:
            for model in ai_models:
                model_nickname = get_model_nickname(model)
                system_prompt = loc_strings["system_prompt"]
                
                if i == 0:
                    user_content = f"## PROJECT INFO ##\n{project_info}\n\n## REQUEST ##\n{prompt_text}"
                else:
                    if args.no_collaboration or not has_other_ai_info:
                        user_content = f"## CURRENT REQUEST ##\n{prompt_text}"
                    else:
                        other_responses = [f"--- RESPONSE FROM {nick} ---\n{resp}\n" for nick, resp in last_turn_responses.items() if nick != model_nickname]
                        user_content = f"## PREVIOUS RESPONSES FROM OTHER AIs ##\n{''.join(other_responses)}\n\n## CURRENT REQUEST ##\n{prompt_text}"

                messages = [{"role": "system", "content": system_prompt}]
                messages.extend(model_histories[model_nickname][-(TRIMMED_HISTORY_COUNT*2):])
                messages.append({"role": "user", "content": user_content})
                
                filename_prefix = "final" if is_last_prompt else f"p{prompt_id}"
                output_path = os.path.join(output_dir, f"{filename_prefix}_{model_nickname}.md")
                live_log_path = os.path.join(live_log_dir, f"{model_nickname}.log")

                with open(live_log_path, 'a', encoding='utf-8') as f:
                    divider = '=' * 20
                    f.write(loc_strings["log_prompt_header"].format(divider=divider, prompt_id=prompt_id, prompt_name=prompt_name))

                api_params = {"transforms": ["web_search"]}
                if use_reasoning:
                    api_params['reasoning'] = {}

                future = executor.submit(process_and_log_request, (client, model, messages, output_path, live_log_path, api_params, loc_strings))
                future_to_model[future] = model

            for future in concurrent.futures.as_completed(future_to_model):
                model_id = future_to_model[future]
                model_nickname = get_model_nickname(model_id)
                try:
                    nick, response_text, user_prompt_content = future.result()
                    if response_text:
                        print(loc_strings["task_completed"].format(nick=nick))
                        current_prompt_responses[nick] = response_text
                        model_histories[nick].extend([
                            {"role": "user", "content": user_prompt_content},
                            {"role": "assistant", "content": response_text}
                        ])
                    else:
                        print(loc_strings["task_failed"].format(nick=nick))
                except Exception as e:
                    print(loc_strings["task_error"].format(model_nickname=model_nickname, e=e))
        
        if current_prompt_responses:
            last_turn_responses = current_prompt_responses.copy()
        
        print(loc_strings["prompt_finished"].format(prompt_id=prompt_id))

    print_divider()
    print(loc_strings["all_finished"])
    print_divider()

if __name__ == "__main__":
    main()
