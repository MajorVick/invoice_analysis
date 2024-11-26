# app/services/ocr/ocr_service.py
import easyocr
from PIL import Image, ImageEnhance
import io

class OCRService:
    def __init__(self):
        # Initialize EasyOCR Reader with English language
        self.reader = easyocr.Reader(['en'])

    async def process_image(self, image_data):
        try:
            # Open image with Pillow
            image = Image.open(io.BytesIO(image_data))
            
            # Convert to grayscale
            image = image.convert('L')
            
            # Enhance contrast
            enhancer = ImageEnhance.Contrast(image)
            image = enhancer.enhance(2)
            
            # Save enhanced image to bytes
            buffered = io.BytesIO()
            image.save(buffered, format="PNG")
            enhanced_image = buffered.getvalue()
            
            # Read enhanced image data with EasyOCR
            result = self.reader.readtext(enhanced_image, detail=0)
            # Join extracted text
            text = ' '.join(result)
            return text
        except Exception as e:
            print(f"Error processing image: {e}")
            return None