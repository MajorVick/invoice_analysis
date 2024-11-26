# app/schemas/document_schema.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Document(BaseModel):
    id: Optional[str] = None
    content: str
    processed_text: Optional[str]
    llm_response: Optional[str]
    created_at: datetime = datetime.now()