"""
Main entry point for the AI research bot.
AI 연구 봇의 메인 진입점.
"""
import sys
import asyncio
import argparse
from pathlib import Path
from typing import Optional, List, Tuple

from config.config import Config
from config.constants import PRIORITY_PROMPTS
from core.orchestrator import ProjectOrchestrator
from core.exceptions import ConfigurationError, ProjectError
from utils.logger import setup_logger
from localization import STRINGS
from services.prompt_parser import PromptParser


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments / 명령줄 인자를 파싱"""
    parser = argparse.ArgumentParser(
        description="An automated project research bot using AI models."
    )
    parser.add_argument(
        '--lang', '-l',
        type=str,
        choices=['ko', 'en'],
        help="Select language (ko/en). If not specified, an interactive prompt will be shown."
    )
    parser.add_argument(
        '--prompt', '-p',
        type=str,
        help="Specify a custom prompt file inside the 'prompts/' directory."
    )
    parser.add_argument(
        '--no-collaboration',
        action='store_true',
        help="Skips the collaboration step where AIs reference each other's answers."
    )
    parser.add_argument(
        '--pdf-engine',
        type=str,
        choices=['pdf-text', 'mistral-ocr', 'native'],
        default='pdf-text',
        help="Specify the PDF processing engine (default: pdf-text)."
    )
    return parser.parse_args()


def select_language() -> str:
    """Interactive language selection / 대화형 언어 선택"""
    while True:
        choice = input(STRINGS['en']["select_language"])
        if choice == '1':
            return 'ko'
        elif choice == '2':
            return 'en'
        else:
            print(STRINGS['en']["invalid_input"])


def get_prompt_files(prompts_dir: Path, lang: str = None) -> List[Tuple[Path, Optional[str]]]:
    """
    Get list of prompt files with descriptions
    프롬프트 파일 목록과 설명 가져오기
    
    Args:
        prompts_dir: Prompts directory path
        lang: Language filter ('en' for English, 'ko' for Korean)
    """
    prompt_files = []
    
    # Scan only root level .md files / 루트 레벨 .md 파일만 스캔
    for filepath in prompts_dir.glob('*.md'):
        if filepath.is_file():
            filename = filepath.name
            
            # Language filtering / 언어 필터링
            if lang == 'en':
                # English: only files ending with _en.md
                if not filename.endswith('_en.md'):
                    continue
            elif lang == 'ko':
                # Korean: exclude files ending with _en.md
                if filename.endswith('_en.md'):
                    continue
            
            description = PromptParser.parse_metadata(filepath)
            prompt_files.append((filepath, description))
    
    # Sort: priority files first, then alphabetical / 정렬: 우선순위 파일 먼저, 그 다음 알파벳순
    def sort_key(item):
        filename = item[0].name
        if filename in PRIORITY_PROMPTS:
            return (0, PRIORITY_PROMPTS.index(filename))
        else:
            return (1, filename.lower())
    
    prompt_files.sort(key=sort_key)
    
    return prompt_files


def select_prompt_file(lang: str) -> Path:
    """Interactive prompt file selection / 대화형 프롬프트 파일 선택"""
    loc_strings = STRINGS[lang]
    prompts_dir = Path('prompts')
    
    # Check prompts directory / prompts 디렉토리 확인
    if not prompts_dir.exists() or not prompts_dir.is_dir():
        print(loc_strings["prompts_dir_not_found"])
        sys.exit(1)
    
    # Get prompt files list with language filter / 언어 필터와 함께 프롬프트 파일 목록 가져오기
    prompt_files = get_prompt_files(prompts_dir, lang)
    
    if not prompt_files:
        print(loc_strings["no_prompts_found"])
        print("Switching to custom prompt input mode...")
        filename = input(loc_strings['enter_prompt_filename'])
        return Path('prompts') / filename
    
    # Display menu with better formatting / 더 나은 형식으로 메뉴 표시
    print(f"\n{loc_strings['select_bot']}")
    print("\n" + "=" * 60)
    print(f"{'#':<4} {loc_strings['file_column']:<25} {loc_strings['description_column']}")
    print("=" * 60)
    
    for i, (filepath, description) in enumerate(prompt_files, 1):
        filename = filepath.name
        desc_text = description if description else loc_strings["no_description"]
        # Truncate long descriptions / 긴 설명 자르기
        if len(desc_text) > 50:
            desc_text = desc_text[:47] + "..."
        print(f"{i:<4} {filename:<25} {desc_text}")
    
    print("-" * 60)
    print(f"{'C':<4} {loc_strings['bot_option_custom']:<25} {loc_strings['custom_file_path']}")
    print("=" * 60)
    
    # Handle user input / 사용자 입력 처리
    while True:
        choice = input(loc_strings["select_prompt_message"].format(
            num_options=len(prompt_files)
        )).strip().upper()
        
        if choice == 'C':
            filename = input(loc_strings['enter_prompt_filename'])
            return Path('prompts') / filename
        
        try:
            index = int(choice) - 1
            if 0 <= index < len(prompt_files):
                return prompt_files[index][0]
            else:
                print(loc_strings["invalid_input"])
        except ValueError:
            print(loc_strings["invalid_input"])


async def main() -> None:
    """Main execution function / 메인 실행 함수"""
    args = parse_arguments()
    logger = setup_logger('ai_research_bot')
    
    try:
        lang = args.lang or select_language()
        loc_strings = STRINGS[lang]
        
        if args.prompt:
            prompt_filepath = Path('prompts') / args.prompt
        else:
            prompt_filepath = select_prompt_file(lang)
        
        print(loc_strings["mode_selected"].format(
            lang_upper=lang.upper(),
            prompt_filepath=prompt_filepath
        ))
        
        config = Config(
            language=lang,
            prompt_filepath=prompt_filepath,
            enable_collaboration=not args.no_collaboration,
            pdf_engine=args.pdf_engine
        )
        
        orchestrator = ProjectOrchestrator(config)
        await orchestrator.run()
        
    except ConfigurationError as e:
        logger.error(f"Configuration error: {e}")
        print(f"Error: {e}")
        sys.exit(1)
    except ProjectError as e:
        logger.error(f"Project execution error: {e}")
        print(f"Error: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        logger.info("Execution interrupted by user")
        print("\n실행이 사용자에 의해 중단되었습니다.")
        sys.exit(0)
    except Exception as e:
        logger.exception("Unexpected error occurred")
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())