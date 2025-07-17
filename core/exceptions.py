"""
Custom exception definitions.
커스텀 예외 정의.
"""


class ProjectError(Exception):
    """Base exception for project-related errors / 프로젝트 관련 오류의 기본 예외"""
    pass


class ConfigurationError(ProjectError):
    """Configuration-related errors / 설정 관련 오류"""
    pass


class FileProcessingError(ProjectError):
    """File processing errors / 파일 처리 오류"""
    pass


class APIError(ProjectError):
    """API interaction errors / API 상호작용 오류"""
    pass


class PromptParsingError(ProjectError):
    """Prompt file parsing errors / 프롬프트 파일 파싱 오류"""
    pass