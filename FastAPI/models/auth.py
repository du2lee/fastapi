from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ["NewUser", "Token", "TokenData"]

class NewUser(BaseModel):
    username: str
    password: str
    createdAt : datetime = datetime.now()
    class Config:
        schema_extra = {
            "example" : {
                "username": "dh151446@gmail.com",
                "password": "password1234!",
            }
        }

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None