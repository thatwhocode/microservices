from auth_service.services.auth_service import AuthService
from auth_service.repositories.user_repo import UserRepository
from fastapi.security import OAuth2PasswordBearer
from auth_service.db.database import get_db
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from auth_service.db.models.user import User
oauth_schema = OAuth2PasswordBearer(tokenUrl="auth/token")
class Dependencies:
    def __init__(self, db : AsyncSession =Depends(get_db)):
        self.db = db
        
    @property
    def user_repo(self) -> UserRepository:
        return UserRepository(self.db)
    @property
    def auth_service(self) -> AuthService:
        return AuthService(self.user_repo)

async def get_current_user(token: Annotated[str, Depends(oauth_schema)], deps : Dependencies = Depends(Dependencies)) -> User:
    return await deps.auth_service.get_current_user_from_token(token=token)