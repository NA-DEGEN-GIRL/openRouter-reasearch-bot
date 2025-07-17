"""
Model data provider service with caching.
캐싱이 있는 모델 데이터 제공 서비스.
"""
import os
import json
import time
from typing import Dict
from pathlib import Path
import aiohttp

from config.constants import *
from utils.logger import get_logger


class ModelDataProvider:
    """
    Fetches and caches model data from OpenRouter.
    OpenRouter에서 모델 데이터를 가져오고 캐싱.
    """
    
    def __init__(self):
        """Initialize model data provider / 모델 데이터 제공자 초기화"""
        self.logger = get_logger(self.__class__.__name__)
        self.cache_file = Path(MODEL_CACHE_FILE)
    
    async def get_model_data(self, loc_strings: Dict[str, str]) -> Dict[str, Dict]:
        """
        Get model data with caching.
        캐싱을 사용하여 모델 데이터 가져오기.
        """
        # Check cache validity / 캐시 유효성 확인
        if self._is_cache_valid():
            try:
                with open(self.cache_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                self.logger.info("Loaded model data from cache")
                return data
            except Exception as e:
                self.logger.warning(f"Failed to load cache: {e}")
        
        # Fetch fresh data / 새 데이터 가져오기
        print(loc_strings["fetching_models"])
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(OPENROUTER_MODELS_ENDPOINT) as response:
                    response.raise_for_status()
                    data = await response.json()
            
            models_raw = data.get('data', [])
            
            model_data = {
                model['id']: {
                    'max_completion_tokens': model.get('top_provider', {}).get('max_completion_tokens')
                }
                for model in models_raw
            }
            
            # Save to cache / 캐시에 저장
            self._save_cache(model_data)
            
            return model_data
            
        except aiohttp.ClientError as e:
            print(f"{loc_strings['fetching_models_failed']} ({e})")
            self.logger.error(f"Failed to fetch model data: {e}")
            return {}
        except Exception as e:
            print(f"{loc_strings['fetching_models_failed']} ({e})")
            self.logger.error(f"Unexpected error fetching model data: {e}")
            return {}
    
    def _is_cache_valid(self) -> bool:
        """Check if cache file exists and is fresh / 캐시 파일이 존재하고 신선한지 확인"""
        if not self.cache_file.exists():
            return False
        
        # Check file age / 파일 나이 확인
        file_age = time.time() - os.path.getmtime(self.cache_file)
        return file_age < MODEL_CACHE_TTL
    
    def _save_cache(self, data: Dict[str, Dict]) -> None:
        """Save data to cache file / 캐시 파일에 데이터 저장"""
        try:
            with open(self.cache_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
            self.logger.info("Model data cached successfully")
        except Exception as e:
            self.logger.error(f"Failed to save cache: {e}")