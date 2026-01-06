import uuid
from datetime import datetime
from sqlalchemy import String, Boolean, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from chat_service.db.database import Base

class Message(Base):
    __tablename__ = "messages"
    id : Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4
    )

    sender_id : Mapped[uuid.UUID] = mapped_column(
        primary_key=False,
        default=None
    )
    content: Mapped[str] = mapped_column(
        String(500),
        nullable=False
    )
    created_at : Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable= False
    )