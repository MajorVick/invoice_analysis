# app/services/pdf_parsing/pdf_parsing_service.py
import PyPDF2

class PDFParsingService:
    async def parse_pdf(self, file):
        try:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
            return text
        except Exception as e:
            print(f"Error parsing PDF: {e}")
            return None