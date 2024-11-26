# app/services/pdf_parsing/pdf_parsing_service.py
import PyPDF2

class PDFParsingService:
    async def parse_pdf(self, file):
        try:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                extracted_text = page.extract_text()
                if extracted_text:
                    text += extracted_text
                else:
                    # Handle pages with images or no extractable text
                    text += "[No text found on this page]"
            return text
        except Exception as e:
            print(f"Error parsing PDF: {e}")
            return None