from fastapi import APIRouter, Depends, status
from chat_service.api.deps import get_current_user_id
from chat_service.schemas.message import MessageCreate, MessageRead
from chat_service.db.database import get_db
from chat_service.db.models.message import Message
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
router = APIRouter()

@router.post("/", response_model=MessageRead, status_code=status.HTTP_201_CREATED)
async def create_message(msg: MessageCreate,
                        user_id : Annotated[UUID, Depends(get_current_user_id)],
                          db : AsyncSession = Depends(get_db)):
    new_message = Message(
        sender_id = user_id,
        content = msg.content
    )
    db.add(new_message)
    await db.commit()
    await db.refresh(new_message)
    return new_message