from pydantic import BaseModel, Field
from typing import Optional


class Message(BaseModel):
    thread_id: Optional[str] = Field(None, description="threa id")
    role: str = Field(..., description="role")
    content: str = Field(..., description="content")
