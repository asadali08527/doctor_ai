from gtts import gTTS
import elevenlabs
from elevenlabs.client import ElevenLabs
from configs.config import Config
import platform
import subprocess
import os

class TextToSpeech:
    def __init__(self):
        self.eleven_labs_client = ElevenLabs(api_key=Config.ELEVEN_LABS_API_KEY)

    def gtts_convert(self, text: str, output_file_path: str) -> None:
        """Convert text to speech using gTTS."""
        tts = gTTS(text=text, lang="en", slow=False)
        tts.save(output_file_path)
        self._play_audio(output_file_path)

    def eleven_labs_convert(self, text: str, output_file_path: str) -> None:
        """Convert text to speech using Eleven Labs."""
        audio = self.eleven_labs_client.generate(
            text=text,
            voice="Alice",
            output_format="mp3_22050_32",
            model="eleven_turbo_v2"
        )
        elevenlabs.save(audio, output_file_path)
        self._play_audio(output_file_path)

    def _play_audio(self, file_path: str) -> None:
        """Play audio file based on the operating system."""
        os_name = platform.system()
        try:
            if os_name == "Windows":
                os.system(f"start {file_path}")
            elif os_name == "Darwin":
                os.system(f"open {file_path}")
            else:
                os.system(f"xdg-open {file_path}")
        except Exception as e:
            print(f"Error opening file: {e}")