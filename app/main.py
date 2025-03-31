from fastapi import FastAPI, HTTPException
from ollama import Client
from schemas import Message, ConversationRequest

app = FastAPI()
model: str = "gemma3:4b"

    
@app.post("/chat")
async def chat(request: ConversationRequest):
    try:
        # Initialize Ollama client
        client = Client()
        
        # Convert Pydantic models to dictionaries for Ollama
        messagesDict = [{"role": msg.role, "content": msg.content} for msg in request.messages]
        
        # Call Ollama with the conversation history
        response = client.chat(
            model=model,
            messages=messagesDict
        )
        
        return response["message"]["content"]
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error communicating with Ollama: {str(e)}")

