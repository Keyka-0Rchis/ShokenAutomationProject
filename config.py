# config.py
import os
from dataclasses import dataclass
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # .env を読み込む

# 任意: プリセット名→実モデルの別名解決
MODEL_PRESETS = {
    "smart": os.getenv("OPENAI_MODEL_CHAT", os.getenv("OPENAI_MODEL", "gpt-4o")),
    "fast":  os.getenv("OPENAI_MODEL_FAST", "gpt-4o-mini"),
    "vision":os.getenv("OPENAI_MODEL_VISION", "gpt-4o-mini"),
}

@dataclass(frozen=True)
class Settings:
    api_key: str = os.getenv("OPENAI_API_KEY", "")
    base_url: str | None = os.getenv("OPENAI_BASE_URL") or None
    # 既定モデル（なければ smart を採用）
    model_default: str = os.getenv("OPENAI_MODEL", MODEL_PRESETS["smart"])
    temperature: float = float(os.getenv("OPENAI_TEMPERATURE", "0.7"))

settings = Settings()

if not settings.api_key:
    raise RuntimeError("OPENAI_API_KEY が未設定")

# クライアント生成（base_url を使う場合にも対応）
client = OpenAI(api_key=settings.api_key, base_url=settings.base_url) if settings.base_url \
         else OpenAI(api_key=settings.api_key)

def resolve_model(key: str | None = None) -> str:
    """'smart' / 'fast' / 'vision' / 実モデル名を受け取って最終モデル名を返す"""
    if not key:
        return settings.model_default
    return MODEL_PRESETS.get(key, key)  # プリセット名なら置換、そうでなければそのまま
