from jwt import decode
from jwt.exceptions import InvalidTokenError, ExpiredSignatureError
from shared_packages.schemas.token import TokenPayload
from typing import Any
class Verifier():
    def __init__(self, secret_key : str, algorithm: str):
        self. secret_key = secret_key
        self.algorithm = algorithm
    def verify_token(self, token : str) -> TokenPayload:
        try:
            payload : dict[str, Any] = decode(token, self.secret_key,
                                              algorithms=[self.algorithm])
            token_data = TokenPayload(
            user_id = payload.get("sub"),
            username=payload.get("username")
            )
            return token_data
        except ExpiredSignatureError:
            raise ValueError("Token expired")
        except InvalidTokenError:
            raise ValueError("Invalid token")