#!/usr/bin/env python3
"""
Main entry point for the AI research bot.
AI 연구 봇의 메인 진입점.
"""
import sys
import asyncio
import argparse
from pathlib import Path
from typing import Optional

from config.config import Config
from core.orchestrator import ProjectOrchestrator
from core.exceptions import ConfigurationError, ProjectError
from utils.logger import setup_logger
from localization import STRINGS


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


def select_prompt_file(lang: str) -> Path:
    """Interactive prompt file selection / 대화형 프롬프트 파일 선택"""
    loc_strings = STRINGS[lang]
    print(loc_strings["select_bot"])
    print(f"  {loc_strings['bot_option_research']}")
    print(f"  {loc_strings['bot_option_custom']}")
    
    while True:
        choice = input(f"\n번호를 입력하세요 (1-2): ")
        if choice == '1':
            filename = 'research_en.md' if lang == 'en' else 'research.md'
            return Path('prompts') / filename
        elif choice == '2':
            filename = input(loc_strings['enter_prompt_filename'])
            return Path('prompts') / filename
        else:
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