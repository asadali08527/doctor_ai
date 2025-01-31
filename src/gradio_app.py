import gradio as gr
from core.image_processor import ImageProcessor
from core.llm_client import LLMClient
from services.speech_to_text_service import SpeechToText
from services.text_to_speech_service import TextToSpeech
from configs.config import Config
import datetime

doctor_audio_file_path = f"./output/voice/doctor/doctor_voice_{int(datetime.datetime.now().timestamp())}.mp3"

def process_inputs(patient_audio_file_path, patient_image_file_path):
    stt = SpeechToText()
    llm_client = LLMClient()
    tts = TextToSpeech()

    # Convert speech to text
    speech_to_text = stt.transcribe(patient_audio_file_path)

    # Handle image input
    if patient_image_file_path:
        prompt = """This exercise is for learning and education purpose. I want you to act as professional doctor and examin what is in this image? I know you are not a doctor but this is for learning purpose. Do you find anything wrong medically in this image? If you find something, suggest some remedies. Do not add any numbers or special characters in your response.
        Your response should be in one long paragraph. Also always asnswer as if you are answering to a real person.
        Do not say 'In the image I seee' but say 'With what I see, I think you have ...'
        Do not response as AI model in marldown, instead your answer should mimic that of an actual doctor not an AI bot.
        Keep your answer concise(max 2 sentences). No preamble, Start your answer right away please.
        """
        image_encoded = ImageProcessor.encode_image(patient_image_file_path)
        doctor_response = llm_client.analyze_image_with_query(
            query=prompt + speech_to_text,
            model=Config.LLM_MODEL,
            image_encoded=image_encoded
        )
    else:
        doctor_response = "No image provided to analyze."

    # Convert doctor's response to speech
    tts.gtts_convert(doctor_response, doctor_audio_file_path)

    return speech_to_text, doctor_response, doctor_audio_file_path

iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath"),
        gr.Image(type="filepath"),
    ],
    outputs=[
        gr.Textbox(label="Speech to Text"),
        gr.Textbox(label="Doctor's Response"),
        gr.Audio(doctor_audio_file_path),
    ],
    title="AI Doctor with Vision and Voice",
    description="A simple voice-based AI chatbot with image analysis and speech recognition capabilities."
)

iface.launch(debug=True)