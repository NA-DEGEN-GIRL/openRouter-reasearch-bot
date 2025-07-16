import os
import re
import argparse
import sys
import concurrent.futures
import shutil
import requests
from dotenv import load_dotenv
from openai import OpenAI, APITimeoutError, APIConnectionError
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type
from localization import STRINGS
import mimetypes
import base64

# --- CONFIGURATION ---
TRIMMED_HISTORY_COUNT = 25 # Number of context history pairs (user/assistant) to maintain.
MAX_TOKENS = 65536 # default max tokens
TIMEOUT = 1200 # 20 mins

# --- HELPER FUNCTIONS ---
def fetch_model_data(loc_strings):
    # OpenRouter에서 모델 데이터를 가져와 딕셔너리로 반환
    # Fetches model data from OpenRouter and returns it as a dictionary.
    print(loc_strings["fetching_models"])
    try:
        response = requests.get("https://openrouter.ai/api/v1/models")
        response.raise_for_status()
        models_raw = response.json().get('data', [])
        
        model_data = {
            model['id']: {
                'max_completion_tokens': model.get('top_provider', {}).get('max_completion_tokens')
            }
            for model in models_raw
        }
        
        return model_data
    except requests.RequestException as e:
        print(f"{loc_strings['fetching_models_failed']} ({e})")
        return {}

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

    project_name = None
    prompts = []
    for header, text in zip(headers, parts):
        clean_text = text.strip()
        
        # 'deactive:'로 시작하는 섹션은 건너뜀
        # Skip sections starting with 'deactive'
        if header.lower().startswith("deactive"):
            continue

        # --- 이미지/PDF 입력 파싱 ---
        img_files = []
        pdf_files = []
        new_lines = []
        for line in clean_text.splitlines():
            img_match = re.match(r"#\s*img\s+(.+)", line, re.IGNORECASE)
            pdf_match = re.match(r"#\s*pdf\s+(.+)", line, re.IGNORECASE)
            if img_match:
                img_files.append(img_match.group(1).strip())
            elif pdf_match:
                pdf_files.append(pdf_match.group(1).strip())
            else:
                new_lines.append(line)
        prompt_text = '\n'.join(new_lines).strip()

        if header.lower() == "project name":
            project_name = prompt_text.strip()

        elif header.lower().startswith("prompt"):
            use_reasoning = '# reasoning' in prompt_text.lower()
            has_other_ai_info = '# other_ai_info' in prompt_text.lower()
            prompt_content = re.sub(r'#\s*(reasoning|other_ai_info)', '', prompt_text, flags=re.IGNORECASE).strip()
            
            prompts.append({
                'id': int(re.search(r'\d+', header).group()), 
                'name': header.lower(), 
                'text': prompt_content,
                'use_reasoning': use_reasoning,
                'has_other_ai_info': has_other_ai_info,
                'img_files': img_files,
                'pdf_files': pdf_files
            })

    if not project_name:
        print(loc_strings["error_no_project_name"])
        sys.exit(1)

    return project_name, sorted(prompts, key=lambda x: x['id'])

def make_message_content(prompt_text, img_files, pdf_files):
    content = []
    content.append({"type": "text", "text": prompt_text})

    # 이미지 첨부
    for img_path in img_files:
        if img_path.startswith("http"):
            content.append({
                "type": "image_url",
                "image_url": {"url": img_path}
            })
        else:
            if os.path.isfile(img_path):
                mime, _ = mimetypes.guess_type(img_path)
                if not mime:
                    mime = "image/jpeg"
                with open(img_path, "rb") as f:
                    b64 = base64.b64encode(f.read()).decode()
                data_url = f"data:{mime};base64,{b64}"
                content.append({
                    "type": "image_url",
                    "image_url": {"url": data_url}
                })
            else:
                print(f"[Warning] Image file not found: {img_path}")
    # PDF 첨부
    for pdf_path in pdf_files:
        if os.path.isfile(pdf_path):
            with open(pdf_path, "rb") as f:
                b64 = base64.b64encode(f.read()).decode()
            data_url = f"data:application/pdf;base64,{b64}"
            content.append({
                "type": "file",
                "file": {
                    "filename": os.path.basename(pdf_path),
                    "file_data": data_url
                }
            })
        else:
            print(f"[Warning] PDF file not found: {pdf_path}")
    return content

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
def get_ai_response_stream(client, model, messages, max_tokens, extra_body=None):
    # OpenRouter API를 호출하고 스트림 객체를 반환
    # Calls the OpenRouter API and returns a stream object.
    return client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
        timeout=TIMEOUT,
        max_tokens=max_tokens,
        extra_body=extra_body or {}
    )

def process_and_log_request(args_tuple):
    # 모델 요청, 실시간 로깅, 결과 반환을 병렬로 처리하는 작업자 함수
    # Worker function that handles a single model request, live logging, and returns the result concurrently.
    client, model, messages, output_path, live_log_path, api_params, max_tokens, loc_strings = args_tuple
    model_nickname = get_model_nickname(model)
    full_response = ""
    
    try:
        stream = get_ai_response_stream(client, model, messages, max_tokens, extra_body=api_params)
        
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
        print(e)
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
        help="Specify a custom prompt file inside the 'prompts/' directory (e.g., 'research_en.md'). Bypasses menus."
    )
    parser.add_argument(
        '--no-collaboration',
        action='store_true',
        help="Skips the collaboration step where AIs reference each other's answers."
    )
    parser.add_argument(
        '--pdf-engine', type=str, choices=['pdf-text', 'mistral-ocr', 'native'], default='pdf-text',
        help="Specify the PDF processing engine (default: pdf-text)."
    )
    args = parser.parse_args()

    # --- 1. 언어 선택 ---
    lang = args.lang
    if not lang:
        while True:
            choice = input(STRINGS['en']["select_language"])
            if choice == '1': lang = 'ko'; break
            elif choice == '2': lang = 'en'; break
            else: print(STRINGS['en']["invalid_input"])
    
    loc_strings = STRINGS[lang]

    # --- 2. 프롬프트 파일 경로 결정 ---
    prompt_filepath = None
    if args.prompt:
        # 옵션으로 파일이 직접 지정된 경우
        prompt_filepath = os.path.join("prompts", args.prompt)
    else:
        # 메뉴를 통해 파일 선택
        print(loc_strings["select_bot"])
        print(f"  {loc_strings['bot_option_research']}")
        print(f"  {loc_strings['bot_option_custom']}")
        
        while True:
            choice = input(f"\n번호를 입력하세요 (1-2): ")
            if choice == '1':
                prompt_filepath = 'prompts/research_en.md' if lang == 'en' else 'prompts/research.md'
                break
            elif choice == '2':
                filename = input(loc_strings['enter_prompt_filename'])
                prompt_filepath = os.path.join("prompts", filename)
                break
            else:
                print(loc_strings["invalid_input"])

    print(loc_strings["mode_selected"].format(lang_upper=lang.upper(), prompt_filepath=prompt_filepath))

    load_dotenv()
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print(loc_strings["error_no_api_key"]); sys.exit(1)

    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)

    model_data = fetch_model_data(loc_strings)
    ai_models = load_ai_models()
    project_name, prompts = parse_prompt_file(prompt_filepath, loc_strings)
    
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
                    user_content = prompt_text
                else:
                    if args.no_collaboration or not has_other_ai_info:
                        user_content = prompt_text
                    else:
                        other_responses = [f"--- RESPONSE FROM {nick} ---\n{resp}\n" for nick, resp in last_turn_responses.items() if nick != model_nickname]
                        user_content = f"## PREVIOUS RESPONSES FROM OTHER AIs ##\n{''.join(other_responses)}\n\n## CURRENT REQUEST ##\n{prompt_text}"
                
                img_files = prompt_data.get('img_files', [])
                pdf_files = prompt_data.get('pdf_files', [])
                messages = [{"role": "system", "content": system_prompt}]
                messages.extend(model_histories[model_nickname][-(TRIMMED_HISTORY_COUNT*2):])

                content = make_message_content(user_content, img_files, pdf_files)
                # image/pdf가 없는 경우 기존처럼 string, 그렇지 않으면 [{...}, {...}]
                if len(content) == 1 and content[0]["type"] == "text":
                    messages.append({"role": "user", "content": content[0]["text"]})
                else:
                    messages.append({"role": "user", "content": content})

                #messages.append({"role": "user", "content": user_content})
                
                filename_prefix = "final" if is_last_prompt else f"p{prompt_id}"
                output_path = os.path.join(output_dir, f"{filename_prefix}_{model_nickname}.md")
                live_log_path = os.path.join(live_log_dir, f"{model_nickname}.log")

                with open(live_log_path, 'a', encoding='utf-8') as f:
                    divider = '=' * 20
                    f.write(loc_strings["log_prompt_header"].format(divider=divider, prompt_id=prompt_id, prompt_name=prompt_name))

                api_params = {"plugins": [{"id": "web"}]}
                if use_reasoning:
                    api_params['reasoning'] = {}

                max_tokens = MAX_TOKENS
                if model_data and model in model_data:
                    model_max = model_data[model].get('max_completion_tokens')
                    if model_max is not None:
                        max_tokens = model_max

                future = executor.submit(process_and_log_request, (client, model, messages, output_path, live_log_path, api_params, max_tokens, loc_strings))
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
