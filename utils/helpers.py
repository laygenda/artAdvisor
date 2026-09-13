import re
from datetime import datetime

def get_dynamic_greeting() -> str:
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "Selamat pagi"
    elif 12 <= hour < 15:
        return "Selamat siang"
    elif 15 <= hour < 18:
        return "Selamat sore"
    else:
        return "Selamat malam"

def validate_groq_key(api_key: str) -> bool:
    if not api_key or not isinstance(api_key, str):
        return False
    return api_key.startswith("gsk_")

def clean_llm_output(text: str) -> str:
    if not text:
        return ""
    cleaned_text = re.sub(r'\n{3,}', '\n\n', text)
    return cleaned_text.strip()