from groq import Groq
from configs.config import Config

class SpeechToText:
    def __init__(self):
        self.client = Groq(api_key=Config.GROQ_API_KEY)

    def transcribe(self, audio_file_path: str) -> str:
        """Convert speech from an audio file to text using Groq API."""
        with open(audio_file_path, "rb") as audio_file:
            transcription = self.client.audio.transcriptions.create(
                model=Config.STT_MODEL,
                file=audio_file,
                language="en"
            )
        return transcription.text