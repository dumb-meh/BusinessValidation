from pydantic import BaseModel
from typing import List,Dict, Any
class ChatResponse(BaseModel):
    response: str
    
class ChatRequest(BaseModel):
    history: List [Any]
    uploadedfile:str
    user_message: str