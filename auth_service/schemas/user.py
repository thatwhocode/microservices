from pydantic import BaseModel, ConfigDict,  EmailStr, Field
from uuid import UUID
from shared_packages.schemas.base import CoreModel

class UserBase(CoreModel):
    email:  EmailStr
    username: str = Field(..., min_length=3, max_length=50, examples=['cool_user_123'])

class UserCreate(UserBase):
    password: str = Field(..., min_length=8, description="Password must be 8 charactes long")

class UserRead(UserBase):
    id: UUID
    is_active: bool =True
class UserLogin(CoreModel):
    email: EmailStr
    password: str