from dtos.baseDto import BaseDtoMixin
from typing import Optional
from datetime import datetime

__all__ = ['FaqDto', 'NoticeDto']

class FaqDto(BaseDtoMixin):
    def __init__(self, **data):
        super().__init__(**data)
        
    category: str = ...
    title: str = ...
    content: str = ...


class NoticeDto(BaseDtoMixin):
    def __init__(self, **data):
        super().__init__(**data)

    title: str = ...
    content: str = ...
    date : datetime = ...