"""
Prompt file parsing service.
프롬프트 파일 파싱 서비스.
"""
import re
from typing import List, Tuple, Dict
from pathlib import Path

from core.models import Prompt
from core.exceptions import PromptParsingError
from config.constants import *
from utils.logger import get_logger


class PromptParser:
    """
    Parses prompt files and extracts structured data.
    프롬프트 파일을 파싱하고 구조화된 데이터를 추출.
    """
    
    def __init__(self):
        """Initialize prompt parser / 프롬프트 파서 초기화"""
        self.logger = get_logger(self.__class__.__name__)
    
    def parse(self, filepath: Path, loc_strings: Dict[str, str]) -> Tuple[str, str, str, List[Prompt]]:
        """
        Parse prompt file and return project info and prompts.
        프롬프트 파일을 파싱하고 프로젝트 정보와 프롬프트 반환.
        """
        try:
            content = filepath.read_text(encoding='utf-8')
        except FileNotFoundError:
            raise PromptParsingError(
                loc_strings["error_file_not_found"].format(filepath=filepath)
            )
        except Exception as e:
            raise PromptParsingError(f"Error reading prompt file: {e}")
        
        headers, sections = self._extract_sections(content)
        
        if not headers:
            raise PromptParsingError(
                loc_strings["error_no_headers"].format(filepath=filepath)
            )
        
        project_name = None
        system_prompt = None
        context_optional = ""
        prompts = []
        
        for header, text in zip(headers, sections):
            clean_text = text.strip()
            header_lower = header.lower()
            
            if header_lower.startswith(SECTION_HEADERS['DEACTIVE_PREFIX']):
                continue
            
            if header_lower == SECTION_HEADERS['PROJECT_NAME']:
                project_name = clean_text
            elif header_lower == SECTION_HEADERS['CONTEXT_PREFIX']:
                context_optional = clean_text
            elif header_lower == SECTION_HEADERS['SYSTEM_PROMPT']:
                system_prompt = clean_text
            elif header_lower.startswith(SECTION_HEADERS['PROMPT_PREFIX']):
                prompt = self._parse_prompt_section(header, clean_text)
                prompts.append(prompt)
        
        if not project_name:
            raise PromptParsingError(loc_strings["error_no_project_name"])
        
        if not system_prompt:
            raise PromptParsingError(loc_strings["error_no_system_prompt"])
        
        return project_name, context_optional, system_prompt, sorted(prompts, key=lambda x: x.id)
    
    def _extract_sections(self, content: str) -> Tuple[List[str], List[str]]:
        """Extract headers and sections / 헤더와 섹션 추출"""
        headers = re.findall(r"##\s*(.*?)\s*##", content)
        sections = re.split(r"##\s*.*?\s*##", content)[1:]
        return headers, sections
    
    # REFACTORED: Reduced complexity by extracting file parsing
    def _parse_prompt_section(self, header: str, content: str) -> Prompt:
        """Parse single prompt section / 단일 프롬프트 섹션 파싱"""
        id_match = re.search(r'\d+', header)
        if not id_match:
            raise PromptParsingError(f"No ID found in prompt header: {header}")
        
        prompt_id = int(id_match.group())
        
        files = self._extract_file_references(content)
        
        prompt_text = self._remove_file_commands(content)
        
        use_reasoning = REASONING_FLAG.lower() in prompt_text.lower()
        has_other_ai_info = OTHER_AI_INFO_FLAG.lower() in prompt_text.lower()
        
        prompt_text = self._remove_flags(prompt_text)
        
        return Prompt(
            id=prompt_id,
            name=header,
            text=prompt_text,
            use_reasoning=use_reasoning,
            has_other_ai_info=has_other_ai_info,
            **files
        )
    
    def _extract_file_references(self, content: str) -> Dict[str, List[str]]:
        """Extract file references / 파일 참조 추출"""
        files = {
            'img_files': [],
            'pdf_files': [],
            'code_files': [],
            'doc_files': []
        }
        
        for line in content.splitlines():
            for file_type, pattern in FILE_COMMANDS.items():
                match = re.match(pattern, line, re.IGNORECASE)
                if match:
                    file_key = f"{file_type.lower()}_files"
                    files[file_key].append(match.group(1).strip())
                    break
        return files
    
    def _remove_file_commands(self, content: str) -> str:
        """Remove file commands from content / 콘텐츠에서 파일 명령어 제거"""
        lines = []
        for line in content.splitlines():
            if not any(re.match(pattern, line, re.IGNORECASE) for pattern in FILE_COMMANDS.values()):
                lines.append(line)
        return '\n'.join(lines).strip()
    
    def _remove_flags(self, text: str) -> str:
        """Remove special flags from text / 텍스트에서 특별 플래그 제거"""
        return re.sub(
            rf'({re.escape(REASONING_FLAG)}|{re.escape(OTHER_AI_INFO_FLAG)})',
            '',
            text,
            flags=re.IGNORECASE
        ).strip()