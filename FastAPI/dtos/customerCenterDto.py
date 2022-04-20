from dtos.baseDto import BaseDtoMixin
from typing import Optional
from pydantic import BaseModel, validator, Field
from models.baseModel import PyObjectId
from datetime import date, datetime

__all__ = ['FaqDto', 'NoticeDto']

class FaqDto(BaseDtoMixin):
    def __init__(self, **data):
        super().__init__(**data)
        
    category: str = ...
    title: str = ...
    content: str = ...


class NoticeDto(BaseModel):
    def __init__(self, **data):
        super().__init__(**data)

    title: str = ...
    content: str = ...
    date : datetime = ...