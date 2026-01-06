import uuid
from datetime import datetime
from sqlalchemy import String, Boolean, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from auth_service.db.database import Base

class User(Base):
    __tablename__ = "users"


    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, 
        default=uuid.uuid4
    )


    email: Mapped[str] = mapped_column(String(320), unique=True, index=True, nullable=False)
    
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    

    hashed_password: Mapped[str] = mapped_column(String(1024), nullable=False)

    is_active: Mapped[bool] = mapped_column(default=True, server_default="true")
    is_superuser: Mapped[bool] = mapped_column(default=False, server_default="false")


    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        server_default=func.now(),
        nullable=False
    )