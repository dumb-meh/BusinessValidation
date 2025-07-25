import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.services.chatbot.chatbot_route import router as chatbot_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include chatbot router
app.include_router(chatbot_router)

# Try to include PDF router if it exists
try:
    from app.services.chatbot.pdf_extractor import router as pdf_router
    app.include_router(pdf_router)
    print("✅ PDF extractor router loaded successfully")
except ImportError as e:
    print(f"⚠️  PDF extractor not available: {e}")
    print("   Create app/services/chatbot/pdf_extractor.py to enable PDF functionality")

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI application!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.1.0", port=8091, reload=True)