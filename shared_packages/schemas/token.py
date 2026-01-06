from shared_packages.schemas.base import CoreModel
from uuid import UUID
class Token(CoreModel):
    access_token : str
    token_type : str
class TokenPayload(Token):
    username : str | None = None
    user_id  : UUID | None = None