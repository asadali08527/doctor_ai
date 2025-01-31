from groq import Groq
from configs.config import Config

class LLMClient:
    def __init__(self):
        self.client = Groq(api_key=Config.GROQ_API_KEY)

    def analyze_image_with_query(self, query: str, model: str, image_encoded: str) -> str:
        """Analyze an image using the Groq API."""
        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": query},
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_encoded}"}},
                ],
            }
        ]

        completion = self.client.chat.completions.create(model=model, messages=messages)
        return completion.choices[0].message.content