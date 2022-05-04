from dtos.baseDto import BaseDtoMixin
from typing import Optional

__all__ = ['UsersDto', 'ApiKeys']

class UsersDto(BaseDtoMixin):
    def __init__(self, **data):
        super().__init__(**data)
    
    username: str = ...
    password: str = ...
    disabled: Optional[bool] = False