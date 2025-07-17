"""
File handling service for processing various file types.
다양한 파일 타입을 처리하는 파일 핸들링 서비스.
"""
import os
import base64
import mimetypes
from typing import List, Dict, Any, Optional
from pathlib import Path

from core.exceptions import FileProcessingError
from config.constants import *
from utils.logger import get_logger


class FileHandler:
    """
    Handles file processing for attachments.
    첨부 파일 처리를 담당.
    """
    
    def __init__(self):
        """Initialize file handler / 파일 핸들러 초기화"""
        self.logger = get_logger(self.__class__.__name__)
    
    def make_message_content(
        self,
        prompt_text: str,
        img_files: Optional[List[str]] = None,
        pdf_files: Optional[List[str]] = None,
        code_files: Optional[List[str]] = None,
        doc_files: Optional[List[str]] = None
    ) -> Any:
        """
        Create message content with file attachments.
        파일 첨부가 있는 메시지 콘텐츠 생성.
        """
        content = []
        
        # Process document files / 문서 파일 처리
        if doc_files:
            for doc_path in doc_files:
                content.extend(self._handle_doc_file(doc_path))
        
        # Process code files / 코드 파일 처리
        if code_files:
            for code_path in code_files:
                content.extend(self._handle_code_file(code_path))
        
        # Add main text / 메인 텍스트 추가
        content.append({"type": "text", "text": prompt_text})
        
        # Process image files / 이미지 파일 처리
        if img_files:
            for img_path in img_files:
                content.extend(self._handle_image_file(img_path))
        
        # Process PDF files / PDF 파일 처리
        if pdf_files:
            for pdf_path in pdf_files:
                content.extend(self._handle_pdf_file(pdf_path))
        
        # Return simple string if only text / 텍스트만 있으면 단순 문자열 반환
        if len(content) == 1 and content[0]["type"] == "text":
            return content[0]["text"]
        
        return content
    
    def _handle_doc_file(self, doc_path: str) -> List[Dict[str, Any]]:
        """Handle document file / 문서 파일 처리"""
        path = Path(doc_path)
        if not path.exists():
            self.logger.error(f"Doc file not found: {doc_path}")
            raise FileProcessingError(f"Doc file not found: {doc_path}")

        if path.suffix.lower() not in SUPPORTED_DOC_EXTENSIONS:
            self.logger.error(f"Unsupported doc file type: {doc_path}")
            raise FileProcessingError(f"Unsupported doc file type: {doc_path}")

        try:
            content = path.read_text(encoding='utf-8')
            return [{
                "type": "text",
                "text": f"[File: {doc_path}]\n```markdown\n{content}\n```"
            }]
        except UnicodeDecodeError as e:
            self.logger.error(f"Error decoding doc file {doc_path}: {e}")
            raise FileProcessingError(f"Error decoding doc file {doc_path}: {e}")
        except Exception as e:
            self.logger.error(f"Error reading doc file {doc_path}: {e}")
            raise FileProcessingError(f"Error reading doc file {doc_path}: {e}")
    
    def _handle_code_file(self, code_path: str) -> List[Dict[str, Any]]:
        """Handle code file / 코드 파일 처리"""
        path = Path(code_path)
        if not path.exists():
            self.logger.error(f"Code file not found: {code_path}")
            raise FileProcessingError(f"Code file not found: {code_path}")

        try:
            content = path.read_text(encoding='utf-8')
            # Detect language from extension / 확장자에서 언어 감지
            ext = path.suffix.lower()
            lang_map = {
                '.py': 'python',
                '.js': 'javascript',
                '.java': 'java',
                '.cpp': 'cpp',
                '.c': 'c',
                '.go': 'go',
                '.rs': 'rust'
            }
            language = lang_map.get(ext, 'text')
            return [{
                "type": "text",
                "text": f"[File: {code_path}]\n```{language}\n{content}\n```"
            }]
        except UnicodeDecodeError as e:
            self.logger.error(f"Error decoding code file {code_path}: {e}")
            raise FileProcessingError(f"Error decoding code file {code_path}: {e}")
        except Exception as e:
            self.logger.error(f"Error reading code file {code_path}: {e}")
            raise FileProcessingError(f"Error reading code file {code_path}: {e}")
    
    def _handle_image_file(self, img_path: str) -> List[Dict[str, Any]]:
        """Handle image file / 이미지 파일 처리"""
        # Handle URL images / URL 이미지 처리
        if img_path.startswith("http"):
            return [{
                "type": "image_url",
                "image_url": {"url": img_path}
            }]
        
        # Handle local images / 로컬 이미지 처리
        path = Path(img_path)
        if not path.exists():
            self.logger.error(f"Image file not found: {img_path}")
            raise FileProcessingError(f"Image file not found: {img_path}")

        if path.suffix.lower() not in SUPPORTED_IMAGE_EXTENSIONS:
            self.logger.error(f"Unsupported image file type: {img_path}")
            raise FileProcessingError(f"Unsupported image file type: {img_path}")

        try:
            mime_type, _ = mimetypes.guess_type(img_path)
            if not mime_type:
                mime_type = "image/jpeg"
            with open(path, 'rb') as f:
                image_data = f.read()
            b64_data = base64.b64encode(image_data).decode('utf-8')
            data_url = f"data:{mime_type};base64,{b64_data}"
            return [{
                "type": "image_url",
                "image_url": {"url": data_url}
            }]
        except Exception as e:
            self.logger.error(f"Error processing image file {img_path}: {e}")
            raise FileProcessingError(f"Error processing image file {img_path}: {e}")
    
    def _handle_pdf_file(self, pdf_path: str) -> List[Dict[str, Any]]:
        """Handle PDF file / PDF 파일 처리"""
        path = Path(pdf_path)
        if not path.exists():
            self.logger.error(f"PDF file not found: {pdf_path}")
            raise FileProcessingError(f"PDF file not found: {pdf_path}")

        try:
            with open(path, 'rb') as f:
                pdf_data = f.read()
            b64_data = base64.b64encode(pdf_data).decode('utf-8')
            data_url = f"data:application/pdf;base64,{b64_data}"
            return [{
                "type": "file",
                "file": {
                    "filename": path.name,
                    "file_data": data_url
                }
            }]
        except Exception as e:
            self.logger.error(f"Error processing PDF file {pdf_path}: {e}")
            raise FileProcessingError(f"Error processing PDF file {pdf_path}: {e}")

