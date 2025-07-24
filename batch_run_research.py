import os
import re
import subprocess
import sys
import argparse
from pathlib import Path
from datetime import datetime

# --- 설정 (기본값) ---
DEFAULT_BATCH_FILE = Path('./prompts/batch_run/research_batch.md')
DEFAULT_TEMPLATE_FILE = Path('./prompts/research.md')
DEFAULT_MAIN_SCRIPT = Path('main.py')
LOG_DIRECTORY = Path('batch_logs')

def create_modified_prompt(template_content: str, project_path: Path) -> str:
    """템플릿 내용에 프로젝트 이름과 경로를 채워넣어 새로운 프롬프트를 생성합니다."""
    project_name = project_path.stem  # 확장자를 제외한 파일 이름 (예: digitalx)
    
    # 정규표현식을 사용하여 내용을 안정적으로 교체
    # 1. project name 변경
    modified_content = re.sub(
        r'(## project name ##\n)(.*)',
        r'\1' + project_name,
        template_content
    )
    
    # 2. doc 경로 변경
    modified_content = re.sub(
        r'(^# doc ).*$',
        f'# doc ./{project_path.as_posix()}', # Windows 경로 문제를 피하기 위해 posix 스타일로 변환
        modified_content,
        flags=re.MULTILINE
    )
    return modified_content

def write_log(project_name: str, command: list, result: subprocess.CompletedProcess):
    """실행 결과를 로그 파일에 저장합니다."""
    LOG_DIRECTORY.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    status = "SUCCESS" if result.returncode == 0 else "FAILURE"
    log_file = LOG_DIRECTORY / f"{project_name}_{timestamp}_{status}.log"

    log_content = f"""
# {project_name} Execution Log
- Timestamp: {timestamp}
- Status: {status}
- Command: {' '.join(command)}
- Return Code: {result.returncode}

{'='*20} STDOUT {'='*20}
{result.stdout}

{'='*20} STDERR {'='*20}
{result.stderr}
"""
    with open(log_file, 'w', encoding='utf-8') as f:
        f.write(log_content.strip())
    print(f"📄 로그 파일 저장 완료: {log_file}")

def run_batch_process(batch_file: Path, template_file: Path, main_script: Path):
    """배치 파일을 읽어 각 프로젝트에 대한 분석 스크립트를 순차적으로 실행합니다."""
    
    # --- 1. 파일 준비 ---
    try:
        template_content = template_file.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"❌ 오류: 템플릿 파일 '{template_file}'을 찾을 수 없습니다.")
        sys.exit(1)

    try:
        project_paths_str = batch_file.read_text(encoding='utf-8').splitlines()
        project_paths = [Path(line.strip()) for line in project_paths_str if line.strip()]
    except FileNotFoundError:
        print(f"❌ 오류: 배치 파일 '{batch_file}'을 찾을 수 없습니다.")
        sys.exit(1)

    temp_run_file = template_file.with_name(f"_temp_{template_file.name}")
    
    total_projects = len(project_paths)
    print(f"🚀 총 {total_projects}개의 프로젝트 처리를 시작합니다.")

    # --- 2. 각 프로젝트에 대해 반복 실행 ---
    for i, project_path in enumerate(project_paths):
        project_name = project_path.stem
        print("\n" + "="*60)
        print(f"🏃 [{i+1}/{total_projects}] 프로젝트 '{project_name}' 처리 시작...")
        print(f"   (파일 경로: {project_path})")
        print("="*60)

        if not project_path.exists():
            print(f"⚠️  경고: '{project_path}' 파일을 찾을 수 없어 건너뜁니다.")
            continue
        
        try:
            # 수정된 내용 생성 및 임시 파일 작성
            modified_prompt = create_modified_prompt(template_content, project_path)
            temp_run_file.write_text(modified_prompt, encoding='utf-8')
            
            command = ['python', str(main_script), '-l', 'ko', '-p', str(temp_run_file).replace('prompts/','')]
            print(f"  > 실행 명령어: {' '.join(command)}")

            result = subprocess.run(
                command, 
                capture_output=True, 
                text=True, 
                encoding='utf-8'
            )

            if result.returncode == 0:
                print(f"✅ '{project_name}' 프로젝트 처리 성공.")
            else:
                print(f"🔥 '{project_name}' 프로젝트 처리 중 오류 발생!")
            
            # 결과 로깅
            write_log(project_name, command, result)

        except Exception as e:
            print(f"❌ 스크립트 실행 중 치명적인 예외 발생: {e}")
            continue

        # --- 3. 모든 작업 완료 후 임시 파일 정리 ---
        finally:
            if temp_run_file.exists():
                temp_run_file.unlink()
                print("\n" + "="*60)
                print(f"🧹 작업 완료. 임시 파일 '{temp_run_file}'을 삭제했습니다.")

def main():
    parser = argparse.ArgumentParser(description="프로젝트 리서치 배치 실행 스크립트")
    parser.add_argument(
        '-b', '--batch-file', type=Path, default=DEFAULT_BATCH_FILE,
        help=f"프로젝트 목록 파일 경로 (기본값: {DEFAULT_BATCH_FILE})"
    )
    parser.add_argument(
        '-t', '--template-file', type=Path, default=DEFAULT_TEMPLATE_FILE,
        help=f"프롬프트 템플릿 파일 경로 (기본값: {DEFAULT_TEMPLATE_FILE})"
    )
    parser.add_argument(
        '-m', '--main-script', type=Path, default=DEFAULT_MAIN_SCRIPT,
        help=f"실행할 Python 스크립트 (기본값: {DEFAULT_MAIN_SCRIPT})"
    )
    args = parser.parse_args()
    
    run_batch_process(args.batch_file, args.template_file, args.main_script)

if __name__ == '__main__':
    main()