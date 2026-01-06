from uuid import UUID
from chat_service.schemas.message import MessageCreate
from chat_service.db.models.message import Message
from chat_service.repositories.message_repo import MessageRepository

class ChatService:
    def __init__(self, message_repo : MessageRepository):
        self.message_repo = message_repo
    async def send_message(self, user_id: UUID, msg_data : MessageCreate)-> Message:
        
        return await self.message_repo.create(sender_id = user_id, 
                                              content=msg_data)
