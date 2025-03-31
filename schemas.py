from pydantic import BaseModel
from typing import List

# Define the data model for messages
class Message(BaseModel):
    role: str
    content: str

# Define the conversation request model
class ConversationRequest(BaseModel):
    messages: List[Message]