from typing import Optional
from fastapi_users import schemas
from pydantic import BaseModel, ConfigDict, EmailStr



class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    user_name: str
    phone: str
    telegram: str

class SUserRead(BaseModel):
    id: int
    email: str
    user_name: str
    phone: str
    telegram: str

class UserCreate(schemas.BaseUserCreate):
    user_name: str
    email: str
    password: str
    id: int
    phone: str
    telegram: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False

    model_config = ConfigDict(from_attributes=True)


class UserUpdate(schemas.BaseUserUpdate):
    pass