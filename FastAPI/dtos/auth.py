from dtos.baseDto import BaseDtoMixin
from typing import Optional

__all__ = ['UsersDto']

class UsersDto(BaseDtoMixin):
    def __init__(self, **data):
        super().__init__(**data)

    id: str = ...
    name: str = ...
    password: str = ...
