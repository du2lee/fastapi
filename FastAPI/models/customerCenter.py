from datetime import datetime
from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, Field
from models.baseModel import PyObjectId

__all__ = ["Faq", "UpdateFaq","Notice","UpdateNotice"]

# Faq 모델 입니다.
class Faq(BaseModel):
    _id: Optional[PyObjectId] = Field(alias="_id")
    category: str = Field(...)
    title: str = Field(...)
    content: str = Field(...)
    createdAt : datetime = datetime.now()

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example" : {
                "category": "유형을 입력하세요",
                "title": "제목을 입력하세요",
                "content": "내용을 입력하세요"
            }
        }

# Faq 수정 시 사용하는 모델 입니다.
class UpdateFaq(BaseModel):
    category: Optional[str] = None
    title: Optional[str] = None
    content: Optional[str] = None

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example" : {
                "category": "수정할 유형을 입력하세요",
                "title": "수정할 제목을 입력하세요",
                "content": "수정할 내용을 입력하세요"
            }
        }
        

# Notice 모델 입니다.
class Notice(BaseModel):
    _id: Optional[PyObjectId] = Field(alias="_id")
    title: str = Field(...)
    content: str = Field(...)
    date : datetime = datetime.now()

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example" : {
                "title": "제목을 입력하세요",
                "content": "내용을 입력하세요"
            }
        }

# Faq 수정 시 사용하는 모델 입니다.
class UpdateNotice(BaseModel):
    title: Optional[str] = None
    date: Optional[datetime] = None
    content: Optional[str] = None

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example" : {
                "title": "제목을 입력하세요",
                "content": "내용을 입력하세요"
            }
        }