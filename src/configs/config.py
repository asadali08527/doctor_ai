import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    ELEVEN_LABS_API_KEY = os.getenv("ELEVEN_LABS_API_KEY")
    STT_MODEL = "whisper-large-v3"
    LLM_MODEL = "llama-3.2-90b-vision-preview"