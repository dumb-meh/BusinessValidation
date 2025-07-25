from fastapi import APIRouter, HTTPException
from .chatbot import Chatbot
from .chatbot_schema import ChatRequest, ChatResponse

router = APIRouter()
chatbot = Chatbot()

@router.post("/chatbot/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        response = chatbot.chat(request.dict())
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
