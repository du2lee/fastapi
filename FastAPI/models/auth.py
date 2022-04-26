from pydantic import BaseModel, Field
from typing import Optional
from models.baseModel import PyObjectId

__all__ = ["User", "Login","Token","TokenData"]

class User(BaseModel):
    _id: Optional[PyObjectId] = Field(alias="_id")
    username: str = Field(...)
    company: str = Field(...)
    password: str = Field(...)

class Login(BaseModel):
    username: str = Field(...)
    password: str = Field(...)
    
class Token(BaseModel):
    access_token: str = Field(...)
    token_type: str = Field(...)

class TokenData(BaseModel):
    username: Optional[str] = None