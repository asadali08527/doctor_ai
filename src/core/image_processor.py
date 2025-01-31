import base64

class ImageProcessor:
    @staticmethod
    def encode_image(image_path: str) -> str:
        """Encode an image file to a base64 string."""
        with open(image_path, "rb") as image_file:
            image_encoded = base64.b64encode(image_file.read()).decode("utf-8")
        return image_encoded