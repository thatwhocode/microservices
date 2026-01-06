from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from auth_service.db.models.user  import User
from auth_service.schemas.user import UserBase
class UserRepository():
    def __init__(self, session:AsyncSession ) -> User | None:
        self.session = session

    async def find_user_email(self, user_email: str):
        query = select(User).where(User.email == user_email)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()
    
    async def find_username(self, username : str)-> User | None:
        query = select(User).where(User.username == username)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()
    
    async def create_user(self, user_data : UserBase, hashed_password: str) -> User | None:
        new_user = User(
            email = user_data.email,
            username = user_data.username,
            hashed_password= hashed_password
        )
        self.session.add(new_user)
        await self.session.commit()
        await self.session.refresh(new_user)
        return new_user