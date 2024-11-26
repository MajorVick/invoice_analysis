# app/services/ocr/ocr_service.py
import easyocr

class OCRService:
    def __init__(self):
        # Initialize EasyOCR Reader with English language
        self.reader = easyocr.Reader(['en'])

    async def process_image(self, image_data):
        try:
            # Read image data
            result = self.reader.readtext(image_data, detail=0)
            # Join extracted text
            text = ' '.join(result)
            return text
        except Exception as e:
            print(f"Error processing image: {e}")
            return None