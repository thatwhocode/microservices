from pydantic import Field, ConfigDict
from uuid import UUID
from shared_packages.schemas.base import CoreModel
from datetime import datetime
class MessageCreate(CoreModel):
    content: str = Field(..., min_length=5, max_length=500, description="user messages")
class MessageRead(MessageCreate):
    id : UUID
    sender_id : UUID
    created_at : datetime = Field(...)
    model_config = ConfigDict(from_attributes=True)
    