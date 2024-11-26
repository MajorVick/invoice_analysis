# app/main.py
from fastapi import FastAPI, UploadFile, File, HTTPException
from app.db.mongodb import connect_to_mongo, close_mongo_connection
from app.services.ocr.ocr_service import OCRService
from app.services.pdf_parsing.pdf_parsing_service import PDFParsingService
from app.services.llm import llm_service
from starlette.response import JSONResponse

app = FastAPI()

ocr_service = OCRService()
pdf_service = PDFParsingService()

@app.on_event("startup")
async def startup():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown():
    await close_mongo_connection()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    if file.content_type.startswith("image/"):
        text = await ocr_service.process_image(content)
        if text is None:
            raise HTTPException(status_code=500, detail="OCR processing failed")
        return JSONResponse(content={"type": "image", "text": text})
    elif file.content_type == "application/pdf":
        text = await pdf_service.parse_pdf(content)
        if text is None:
            raise HTTPException(status_code=500, detail="PDF parsing failed")
        return JSONResponse(content={"type": "pdf", "text": text})
    else:
        raise HTTPException(status_code=400, detail="Unsupported file type")