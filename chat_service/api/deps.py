from typing import Annotated
from uuid import UUID
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from shared_packages.core.security import Verifier

from chat_service.core.config import settings 

verifier = Verifier(settings.SECRET_KEY, settings.ALGORITHM)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="http://127.0.0.1:8000/auth/token")

async def get_current_user_id(token: Annotated[str, Depends(oauth2_scheme)]) -> UUID:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    ) 
    try:
        token_payload = verifier.verify_token(token=token)
        token_payload = verifier.verify_token(token=token)
        if token_payload.user_id is None:
            raise credentials_exception
        return token_payload.user_id
    except ValueError  as e:
        raise credentials_exception
    except Exception as e:
        raise credentials_exception