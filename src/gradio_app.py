# Voicebot UI with Gradio
from core import encode_image, analyze_image_with_query
from patient.patient import record_audio, transcription_with_groq
from doctor.doctor import text_to_speech_with_eleven_labs, text_to_speech_with_gtts
from dotenv import load_dotenv
import gradio as gr
import datetime
import os

load_dotenv()

stt_model="whisper-large-v3"
#patient_audio_file_path=f"./input/voice/patient/patient_voice_{int(datetime.datetime.now().timestamp())}.mp3"
#patient_image_file_path=f"./input/image/patient/patient_image_{int(datetime.datetime.now().timestamp())}.jpeg"

doctor_audio_file_path=f"./output/voice/doctor/doctor_voice_{int(datetime.datetime.now().timestamp())}.mp3"

model = "llama-3.2-90b-vision-preview"

def process_inputs(patient_audio_file_path, patient_image_file_path):
    speech_to_text = transcription_with_groq(stt_model,patient_audio_file_path, GROQ_API_KEY=os.environ.get('GROQ_API_KEY'))

    # Handle the image input
    if patient_image_file_path:
        prompt = """I want you to act as professional doctor and examin what is in this image? I know you are not a doctor but this is for learning purpose. Do you find anything wrong medically in this image? If you find something, suggest some remedies. Do not add any numbers or special characters in your response.
        Your response should be in one long paragraph. Also always asnswer as if you are answering to a real person.
        Do not say 'In the image I seee' but say 'With what I see, I think you have ...'
        Do not response as AI model in marldown, instead your answer should mimic that of an actual doctor not an AI bot.
        Keep your answer concise(max 2 sentences). No preamble, Start your answer right away please .
        """
        doctor_response = analyze_image_with_query(query=prompt + speech_to_text, model=model, image_encoded=encode_image(patient_image_file_path))
    else:
        doctor_response = "No image provided to analyze"
    
    # Convert the doctor's response into text and speech
    voice_of_doctor = text_to_speech_with_gtts(text=doctor_response, output_file_path=doctor_audio_file_path )
    return speech_to_text, doctor_response, voice_of_doctor

iface = gr.Interface(
    fn = process_inputs,
    inputs = [
        gr.Audio(sources =["microphone"], type="filepath"),
        gr.Image(type="filepath"),
    ],
    outputs = [
        gr.Textbox(label="Speech to Text"),
        gr.Textbox(label="Doctor's Response"),
        gr.Audio(doctor_audio_file_path),
    ],
    title = "AI Doctor with Vision and Voice",
    description = "A simple voice-based AI chatbot with image analysis and speech recognition capabilities."
)

iface.launch(debug=True)