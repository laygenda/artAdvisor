import os
from dotenv import load_dotenv

# Memuat variabel dari file .env
load_dotenv()

class Config:
    """
    Kelas konfigurasi utama untuk Galeria ArtAdvisor Chatbot.
    Mengambil data dari environment variables dan menetapkan parameter default LLM.
    """
    
    # API Keys
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    
    MODEL_NAME = "openai/gpt-oss-20b" 
    
    # set 0.3 agar tidak berhalusinasi
    TEMPERATURE = 0.3
    
    # Maksimal token balasan
    MAX_TOKENS = 1024
    
    # Path direktori penyimpanan (menggunakan absolute path relatif terhadap letak settings.py)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    CONVERSATIONS_DIR = os.path.join(BASE_DIR, "conversations")

# Validasi awal saat aplikasi dijalankan
if not Config.GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY tidak ditemukan! Pastikan file .env sudah dikonfigurasi.")