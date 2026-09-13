from groq import Groq, GroqError
from config.settings import Config

class ArtAdvisorClient:
    def __init__(self):
        if not Config.GROQ_API_KEY:
            raise ValueError("API Key Groq tidak ditemukan. Periksa file .env Anda.")
        
        self.client = Groq(api_key=Config.GROQ_API_KEY)
        self.model = Config.MODEL_NAME
        self.temperature = Config.TEMPERATURE
        self.max_tokens = Config.MAX_TOKENS

    def generate_stream(self, messages):
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                stream=True
            )
            
            for chunk in response:
                content = chunk.choices[0].delta.content
                if content:
                    yield content
                    
        except GroqError as e:
            yield f"\n[System Error]: Terjadi gangguan pada koneksi API Groq. Detail: {str(e)}"
        except Exception as e:
            yield f"\n[System Error]: Terjadi kesalahan internal pada sistem. Detail: {str(e)}"