import logging
import speech_recognition as sr
from pydub import AudioSegment
from dotenv import load_dotenv
from groq import Groq
import io
import datetime
import os

load_dotenv()

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def record_audio(file_path, timeout=20, phrase_time_limit=None):
    recognizer = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:  # Fixed Microphone instantiation
            logging.info("Adjusting audio for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            # logging.info("Say something!")

            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            # logging.info("Recording completed.")

            # Convert the recorded audio to WAV format
            wav_data = io.BytesIO(audio.get_wav_data())

            # Convert WAV to MP3 using pydub
            audio_segment = AudioSegment.from_file(wav_data, format="wav")
            audio_segment.export(file_path, format="mp3", bitrate="128k")

            # logging.info(f"Audio saved to {file_path}")

    except Exception as e:
        logging.error(f"Error recording audio: {e}")

# Call the function
# audio_file_path=f"./input/voice/patient/patient_voice_{int(datetime.datetime.now().timestamp())}.mp3"
# record_audio(file_path=audio_file_path)


# To convert the MP3 file to text

def transcription_with_groq(stt_model,audio_file_path, GROQ_API_KEY):
    client = Groq(api_key=GROQ_API_KEY)
    audio_file = open(audio_file_path, 'rb')
    transcription = client.audio.transcriptions.create(
        model=stt_model,
        file=audio_file,
        language="en"
    )
    # print(transcription.text)
    return transcription.text




