# Text to Speech-TTS-model with gtts 
import os
from gtts import gTTS
import elevenlabs
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv
import datetime
import platform
import subprocess
load_dotenv()

def text_to_speech_with_gtts(text, output_file_path):

    language = "en"

    audio_obj = gTTS(
        text=text, 
        lang=language, 
        slow=False
    )
    audio_obj.save(output_file_path)
    os_name = platform.system()
    try:
        if os_name == "Windows":
            #subprocess.run(["powershell",'-c',f'(New-Object Media.SoundPlayer "{output_file_path}").PlaySync();'])
            os.system(f"start {output_file_path}")
        elif os_name == "Darwin":
            # subprocess.run(["afplay", output_file_path])
            os.system(f"open {output_file_path}")
        else:
            subprocess.run(["afplay", output_file_path])
            os.system(f"xdg-open {output_file_path}")
    except Exception as e:
        print(f"Error opening file: {e}")

# input_text = "This is a test text to test speech recognition with autoplay"
# output_file_path = f"./output/voice/doctor/doctor_voice_{int(datetime.datetime.now().timestamp())}.mp3"
# text_to_speech_with_gtts(input_text, output_file_path)

# Text to Speech-TTS-model with Eleven Labs
ELEVEN_LABS_API_KEY = os.environ.get('ELEVEN_LABS_API_KEY')
def text_to_speech_with_eleven_labs(text,output_file_path):
    client = ElevenLabs(api_key=ELEVEN_LABS_API_KEY)
    audio = client.generate(
        text=text,
        voice="Alice",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )
    elevenlabs.save(audio,output_file_path)
    os_name = platform.system()
    try:
        if os_name == "Windows":
            #subprocess.run(["powershell",'-c',f'(New-Object Media.SoundPlayer "{output_file_path}").PlaySync();'])
            os.system(f"start {output_file_path}")
        elif os_name == "Darwin":
            # subprocess.run(["afplay", output_file_path])
            os.system(f"open {output_file_path}")
        else:
            subprocess.run(["afplay", output_file_path])
            os.system(f"xdg-open {output_file_path}")
    except Exception as e:
        print(f"Error opening file: {e}")

# input_text = "This is a test text to test speech recognition"
# output_file_path = f"./output/voice/doctor/doctor_voice_{int(datetime.datetime.now().timestamp())}.mp3"
# text_to_speech_with_eleven_labs(input_text, output_file_path)

# Use model for text output to voice

