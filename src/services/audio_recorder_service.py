import logging
import speech_recognition as sr
from pydub import AudioSegment
import io

class AudioRecorder:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def record_audio(self, file_path: str, timeout: int = 20, phrase_time_limit: int = None) -> None:
        """Record audio from the microphone and save it as an MP3 file."""
        try:
            with sr.Microphone() as source:
                logging.info("Adjusting audio for ambient noise...")
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)

                # Convert to WAV and then to MP3
                wav_data = io.BytesIO(audio.get_wav_data())
                audio_segment = AudioSegment.from_file(wav_data, format="wav")
                audio_segment.export(file_path, format="mp3", bitrate="128k")
                logging.info(f"Audio saved to {file_path}")

        except Exception as e:
            logging.error(f"Error recording audio: {e}")