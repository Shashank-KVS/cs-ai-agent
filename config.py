# config.py
import os
from dotenv import load_dotenv

load_dotenv()  # loads from .env

# ────────────────────────────────────────────────────────────────────────
# Core Azure OpenAI settings
# ────────────────────────────────────────────────────────────────────────
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_KEY      = os.getenv("AZURE_OPENAI_KEY")

OPENAI_API_TYPE    = "azure"
OPENAI_API_VERSION = "2024-10-21"
# ────────────────────────────────────────────────────────────────────────


# ────────────────────────────────────────────────────────────────────────
# Model deployment names (match exactly what you named them in Azure)
# ────────────────────────────────────────────────────────────────────────
# 1) Standard chat completions (GPT-4)
CHAT_COMPLETION_MODEL    = os.getenv("AZURE_OPENAI_CHAT_MODEL", "gpt4-deployment")

# 2) Omni chat completions (GPT-4o)
OMNI_CHAT_MODEL          = os.getenv("AZURE_OPENAI_OMNI_MODEL", "gpt4o-deployment")

# 3) Text-to-Speech (gpt-4o-mini-tts)
TTS_MODEL                = os.getenv("AZURE_OPENAI_TTS_MODEL", "gpt4o-mini-tts-deployment")

# 4) Speech-to-Text (Whisper)
ASR_MODEL                = os.getenv("AZURE_OPENAI_ASR_MODEL", "whisper-deployment")
