from pydantic import BaseModel, Field
from enum import Enum


__all__ = ["UserRegister", "SnsType", "Token", "UserToken"]

class UserRegister(BaseModel):
    # pip install 'pydantic[email]'
    email: str = None
    pw: str = None


class SnsType(str, Enum):
    email: str = "email"
    facebook: str = "facebook"
    google: str = "google"
    kakao: str = "kakao"


class Token(BaseModel):
    Authorization: str = None


class UserToken(BaseModel):
    id: int
    email: str = None
    name: str = None
    phone_number: str = None
    profile_img: str = None
    sns_type: str = None

    class Config:
        orm_mode = True