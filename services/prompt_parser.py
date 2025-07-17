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
    
    def parse(self, filepath: Path, loc_strings: Dict[str, str]) -> Tuple[str, str, List[Prompt]]:
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
        
        # Extract headers and content / 헤더와 콘텐츠 추출
        headers, sections = self._extract_sections(content)
        
        if not headers:
            raise PromptParsingError(
                loc_strings["error_no_headers"].format(filepath=filepath)
            )
        
        # Parse sections / 섹션 파싱
        project_name = None
        system_prompt = None
        context_optional = None
        prompts = []
        
        for header, text in zip(headers, sections):
            clean_text = text.strip()
            header_lower = header.lower()
            
            # Skip deactivated sections / 비활성화된 섹션 건너뛰기
            if header_lower.startswith(SECTION_HEADERS['DEACTIVE_PREFIX']):
                continue
            
            # Parse project name / 프로젝트 이름 파싱
            if header_lower == SECTION_HEADERS['PROJECT_NAME']:
                project_name = clean_text
            
            if header_lower == SECTION_HEADERS['CONTEXT_PREFIX']:
                context_optional = clean_text

            # Parse system prompt / 시스템 프롬프트 파싱
            elif header_lower == SECTION_HEADERS['SYSTEM_PROMPT']:
                system_prompt = clean_text
            
            # Parse prompts / 프롬프트 파싱
            elif header_lower.startswith(SECTION_HEADERS['PROMPT_PREFIX']):
                prompt = self._parse_prompt_section(header, clean_text)
                prompts.append(prompt)
        
        # Validate parsed data / 파싱된 데이터 검증
        if not project_name:
            raise PromptParsingError(loc_strings["error_no_project_name"])
        
        if not system_prompt:
            raise PromptParsingError(loc_strings["error_no_system_prompt"])
        
        return project_name, context_optional ,system_prompt, sorted(prompts, key=lambda x: x.id)
    
    def _extract_sections(self, content: str) -> Tuple[List[str], List[str]]:
        """Extract headers and their content sections / 헤더와 콘텐츠 섹션 추출"""
        headers = re.findall(r"##\s*(.*?)\s*##", content)
        sections = re.split(r"##\s*.*?\s*##", content)[1:]
        
        return headers, sections
    
    def _parse_prompt_section(self, header: str, content: str) -> Prompt:
        """Parse a single prompt section / 단일 프롬프트 섹션 파싱"""
        # Extract prompt ID / 프롬프트 ID 추출
        id_match = re.search(r'\d+', header)
        if not id_match:
            raise PromptParsingError(f"No ID found in prompt header: {header}")
        
        prompt_id = int(id_match.group())
        
        # Parse file attachments and flags / 파일 첨부와 플래그 파싱
        img_files = []
        pdf_files = []
        code_files = []
        doc_files = []
        new_lines = []
        
        for line in content.splitlines():
            # Check for file commands / 파일 명령어 확인
            img_match = re.match(FILE_COMMANDS['IMAGE'], line, re.IGNORECASE)
            pdf_match = re.match(FILE_COMMANDS['PDF'], line, re.IGNORECASE)
            code_match = re.match(FILE_COMMANDS['CODE'], line, re.IGNORECASE)
            doc_match = re.match(FILE_COMMANDS['DOC'], line, re.IGNORECASE)
            
            if img_match:
                img_files.append(img_match.group(1).strip())
            elif pdf_match:
                pdf_files.append(pdf_match.group(1).strip())
            elif code_match:
                code_files.append(code_match.group(1).strip())
            elif doc_match:
                doc_files.append(doc_match.group(1).strip())
            else:
                new_lines.append(line)
        
        prompt_text = '\n'.join(new_lines).strip()
        
        # Check for special flags / 특별 플래그 확인
        use_reasoning = REASONING_FLAG.lower() in prompt_text.lower()
        has_other_ai_info = OTHER_AI_INFO_FLAG.lower() in prompt_text.lower()
        
        # Remove flags from prompt text / 프롬프트 텍스트에서 플래그 제거
        prompt_text = re.sub(
            rf'({re.escape(REASONING_FLAG)}|{re.escape(OTHER_AI_INFO_FLAG)})',
            '',
            prompt_text,
            flags=re.IGNORECASE
        ).strip()
        
        return Prompt(
            id=prompt_id,
            name=header,
            text=prompt_text,
            use_reasoning=use_reasoning,
            has_other_ai_info=has_other_ai_info,
            img_files=img_files,
            pdf_files=pdf_files,
            code_files=code_files,
            doc_files=doc_files
        )