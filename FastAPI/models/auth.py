from typing import Optional
from pydantic import BaseModel, Field

__all__ = ["NewUser", "Token", "TokenData"]

class NewUser(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None