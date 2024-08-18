from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Column, Integer, String, Boolean

from app.database import Base as Base_class


class User(SQLAlchemyBaseUserTable[int], Base_class):
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    user_name = Column(String, nullable=False)
    hashed_password: str = Column(String, nullable=False)
    phone: str = Column(String)
    telegram: str = Column(String)
    refresh_token: str = Column(String)
    confirm_email: bool = Column(Boolean, default=False, nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)
    is_delete: bool = Column(Boolean, default=False, nullable=False)



