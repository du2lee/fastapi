from dtos.baseDto import BaseDtoMixin
from typing import Optional

__all__ = ['UsersDto', 'ApiKeys']

class UsersDto(BaseDtoMixin):
    def __init__(self, **data):
        super().__init__(**data)

    # status = Column(Enum("active", "deleted", "blocked"), default="active")
    email: Optional[str] = ...
    pw = Optional[str] = ...
    name = Optional[str] = ...
    phone_number = Column(String(length=20), nullable=True, unique=True)
    profile_img = Optional[str] = ...
    # sns_type = Column(Enum("FB", "G", "K"), nullable=True)
    marketing_agree = Optional[bool] = ...
    # keys = relationship("ApiKeys", back_populates="users")

class ApiKeys(BaseDtoMixin):
    def __init__(self, **data):
        super().__init__(**data)

    access_key = Column(String(length=64), nullable=False, index=True)
    secret_key = Column(String(length=64), nullable=False)
    user_memo: Optional[str] = ...
    status = Column(Enum("active", "stopped", "deleted"), default="active")
    is_whitelisted = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    whitelist = relationship("ApiWhiteLists", backref="api_keys")
    users = relationship("Users", back_populates="keys")