from auth_service.repositories.user_repo import UserRepository
from auth_service.schemas.user import UserCreate
from fastapi import HTTPException, status
from auth_service.core.security import get_password_hash
from auth_service.db.models.user import User
from shared_packages.schemas.token import Token
from jwt import decode
from jwt.exceptions import InvalidTokenError
from auth_service.core.security import verify_password, create_access_token
from auth_service.core.security import settings
class AuthService:
    def __init__(self, userRepo: UserRepository):
        self.user_repo = userRepo

    async def register_user(self, user_data: UserCreate):
        email =  await self.user_repo.find_user_email(user_data.email)
        if email :
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                                detail="this email already in use")
    
        username =  await self.user_repo.find_username(user_data.username)
        if username:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                     detail="this username already exist")
        password = get_password_hash(user_data.password)
        return await self.user_repo.create_user(user_data=user_data, hashed_password=password)
    
    async def login(self, username : str, password : str) -> Token:
        user  = await self.user_repo.find_username(username=username)
        if not user or not verify_password(password, user.hashed_password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                 detail="wrong login or password")
        access_token = create_access_token(data={"sub": str(user.id)})
        return {"access_token": access_token, "token_type" : "bearer", "username": user.username, "user_id":str(user.id) }
    
    async def get_current_user_from_token(self, token:str) -> User:
        credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                               detail="Couldn`t verify credentials",
                                               headers={"WWW-Authenticate: Bearer"})
        try:
            payload = decode(
                token,
                settings.SECRET_KEY,
                algorithms=[settings.ALGORITHM]
            )
            user_id : str = payload.get("sub")
        except InvalidTokenError:
            raise credentials_exception
        user = await self.user_repo.find_user_by_id(user_id)
        if user is None:
            raise credentials_exception
        return user

