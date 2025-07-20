"""
Application constants and magic strings.
애플리케이션 상수와 매직 문자열.
"""

# API Configuration / API 설정
DEFAULT_MAX_TOKENS = 65536
API_TIMEOUT = 1200
RETRY_ATTEMPTS = 2
RETRY_WAIT_SECONDS = 5

# History Management / 히스토리 관리
TRIMMED_HISTORY_COUNT = 25

# File Processing / 파일 처리
SUPPORTED_IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.webp'}
SUPPORTED_CODE_EXTENSIONS = {'.py', '.js', '.java', '.cpp', '.c', '.go', '.rs'}
SUPPORTED_DOC_EXTENSIONS = {'.md', '.txt', '.rst', '.json'}

# Prompt Parsing / 프롬프트 파싱
SECTION_HEADERS = {
    'PROJECT_NAME': 'project name',
    'SYSTEM_PROMPT': 'system prompt',
    'PROMPT_PREFIX': 'prompt',
    'DEACTIVE_PREFIX': 'deactive',
    'CONTEXT_PREFIX': 'context',
}

# File Commands in Prompts / 프롬프트 내 파일 명령어
FILE_COMMANDS = {
    'IMG': r"#\s*img\s+(.+)",
    'PDF': r"#\s*pdf\s+(.+)",
    'CODE': r"#\s*code\s+(.+)",
    'DOC': r"#\s*doc\s+(.+)"
}

# Special Prompt Flags / 특별 프롬프트 플래그
REASONING_FLAG = '# reasoning'
OTHER_AI_INFO_FLAG = '# other_ai_info'

# Output Paths / 출력 경로
OUTPUT_DIR_PREFIX = "projects"
LIVE_LOG_DIR_NAME = "live_logs"

# REFACTORED: Centralized file names
AI_MODELS_FILE = "ai_models.txt"
MODEL_CACHE_FILE = "model_cache.json"
MODEL_CACHE_TTL = 86400

# OpenRouter API / OpenRouter API
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
OPENROUTER_MODELS_ENDPOINT = "https://openrouter.ai/api/v1/models"

# Logging / 로깅
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# UI Constants / UI 상수
DIVIDER_LENGTH = 80
DIVIDER_CHAR = "="
PROMPT_DIVIDER_CHAR = "*"