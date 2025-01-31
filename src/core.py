import os
from dotenv import load_dotenv
import base64
from groq import Groq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Encode Image


def encode_image(image_path):
    image_file = open(image_path,"rb")
    image_encoded = base64.b64encode(image_file.read()).decode("utf-8")
    return image_encoded



# Setup Multimodal LLM
# query = "What is wrong with my face"
# model = "llama-3.2-90b-vision-preview"

def analyze_image_with_query(query, model, image_encoded):
    client = Groq()
    messages= [
        {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": query
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/png;base64,{image_encoded}"
                }
            }
        ]
        }]

    completion = client.chat.completions.create(
        model= model,
        messages=messages
    )
    # print(completion.choices[0].message.content)
    return completion.choices[0].message.content

