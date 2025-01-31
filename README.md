# AI Doctor Chatbot

The AI Doctor Chatbot is a voice and image-based AI application that allows users to interact with an AI doctor. The chatbot can analyze images and respond to voice inputs, providing medical insights (for learning purposes only). The application is built using Python, Gradio for the UI, and leverages APIs like Groq for LLM and Eleven Labs for text-to-speech.

---

## Features

- **Voice Input**: Users can speak to the AI doctor, and their speech is converted to text for processing.
- **Image Analysis**: Users can upload images, and the AI doctor will analyze them to provide insights.
- **Voice Response**: The AI doctor responds with both text and synthesized speech.
- **Multimodal LLM**: Uses Groq's LLM for text and image analysis.
- **Text-to-Speech**: Supports both gTTS and Eleven Labs for voice synthesis.

---

## Project Structure

    src/
    │
    ├── core/
    │   ├── __init__.py
    │   ├── image_processor.py
    │   ├── llm_client.py
    │
    ├── doctor/
    │   ├── __init__.py
    │   ├── tts.py
    │
    ├── patient/
    │   ├── __init__.py
    │   ├── audio_recorder.py
    │   ├── speech_to_text.py
    │
    ├── utils/
    │   ├── __init__.py
    │   ├── file_utils.py
    │
    ├── gradio_app.py
    └── config.py


---

## Installation

1. **Clone the Repository**:
   ```bash
    https://github.com/asadali08527/doctor_ai.git
    cd ai-doctor-chatbot
    ```
2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3. **Set Up Environment Variables**:

    - Create a .env file in the root directory.
    - Add the following variables:

    ```bash
    GROQ_API_KEY=your_groq_api_key
    ELEVEN_LABS_API_KEY=your_eleven_labs_api_key
    ```
4. **Run the aplication**:
    ```bash
    python src/gradio_app.py
    ```



