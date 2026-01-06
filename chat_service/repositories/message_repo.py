from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from chat_service.db.models.message import Message

class MessageRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
    async def create(self, user_id : UUID, content : str)-> Message:
        new_message = Message(
            sender_id = user_id,
            content = content 
        )
        self.session.add(new_message)
        await self.session.commit()
        await self.session.refresh(new_message)
        return new_message