from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from auth_service.schemas.user import UserBase, UserCreate, UserLogin, UserRead
from auth_service.db.models.user import User
from shared_packages.schemas.token import Token, TokenPayload
from typing import Annotated
from auth_service.api.deps import Dependencies, get_current_user
router = APIRouter()
oauth_schema = OAuth2PasswordBearer(tokenUrl="auth/token")

@router.post("/register",  response_model = UserRead)
async def register(user_data : UserCreate, deps : Dependencies =  Depends(Dependencies)):
    result = await deps.auth_service.register_user(user_data=user_data)
    return result

@router.post("/token", response_model=TokenPayload)
async def login_for_access_token(form_data : Annotated[OAuth2PasswordRequestForm, Depends()], deps : Dependencies = Depends(Dependencies)):
    result = await deps.auth_service.login(
        username=form_data.username,
         password=form_data.password)
    return result

        
@router.get("/me", response_model=UserRead)
async def get_current_user(current_user: User = Depends(get_current_user)) -> User:
    return current_user