from fastapi import APIRouter, HTTPException, UploadFile, File
from pydantic import BaseModel
import PyPDF2
import io
from typing import Optional

# Schema for response
class PDFExtractionResponse(BaseModel):
    filename: str
    text: str
    page_count: int
    success: bool
    message: Optional[str] = None

# PDF Extractor Class
class PDFExtractor:
    def __init__(self):
        pass
    
    def extract_text_from_pdf(self, file_content: bytes, filename: str) -> PDFExtractionResponse:
        try:
            # Create a BytesIO object from the file content
            pdf_file = io.BytesIO(file_content)
            
            # Create PDF reader object
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            
            # Get number of pages
            page_count = len(pdf_reader.pages)
            
            # Extract text from all pages
            extracted_text = ""
            for page_num in range(page_count):
                page = pdf_reader.pages[page_num]
                extracted_text += page.extract_text() + "\n"
            
            return PDFExtractionResponse(
                filename=filename,
                text=extracted_text.strip(),
                page_count=page_count,
                success=True,
                message="PDF text extracted successfully"
            )
            
        except Exception as e:
            return PDFExtractionResponse(
                filename=filename,
                text="",
                page_count=0,
                success=False,
                message=f"Error extracting PDF: {str(e)}"
            )

# FastAPI Router
router = APIRouter()
pdf_extractor = PDFExtractor()

@router.post("/pdf/extract", response_model=PDFExtractionResponse)
async def extract_pdf_text(file: UploadFile = File(...)):
    """
    Extract text from uploaded PDF file
    """
    # Validate file type
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(
            status_code=400, 
            detail="Only PDF files are allowed"
        )
    
    try:
        # Read file content
        file_content = await file.read()
        
        # Extract text using PDFExtractor
        result = pdf_extractor.extract_text_from_pdf(file_content, file.filename)
        
        if not result.success:
            raise HTTPException(status_code=500, detail=result.message)
        
        return result
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Failed to process PDF: {str(e)}"
        )

@router.get("/pdf/health")
async def pdf_service_health():
    """
    Health check endpoint for PDF service
    """
    return {"status": "healthy", "service": "PDF Extractor"}