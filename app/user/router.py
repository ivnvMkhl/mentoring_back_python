from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import APIRouter, Depends
from sqlalchemy import update

from app.database import get_async_session
from app.user.models import User
from app.user.dao import UserDAO
from app.user.rb import RBUser
from app.user.schemas import UserRead,SUserRead

from app.user.models import User
from app.user.base_config import current_active_user


router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/{user_id}")
async def get_user_by_id(user_id: int, user_is_auth: User = Depends(current_active_user)) -> SUserRead | dict:
    if user_is_auth:
        result = await UserDAO.find_on_or_none_by_id(user_id)
        if result is None:
            return {'message' : f'user with ID {user_id} is not found'}
        return result

@router.put('/{user_id}')
async def user_update(user_id : int,  user: RBUser = Depends(), user_is_auth: User = Depends(current_active_user)):
    if user_is_auth:
        user = user.to_dict()
        new_values = {k:v for k,v in user.items() if v is not None}
        print(new_values)
        check = await UserDAO.update(
            filter_by={'id': user_id, 'is_active' : True},**new_values)
        if check:
            return {'message' : 'user update succes', 'user': user}
        else:
            return {'message' : 'user update error'}



@router.delete('/{user_id}')
async def delete_user(user_id: int, session: AsyncSession = Depends(get_async_session), user_is_auth: User = Depends(current_active_user)):
    if user_is_auth:
        stmt = update(User).where(User.id == user_id).values(is_active = False)
        await session.execute(stmt)
        await session.commit()
        return {'message': f"user with ID {user_id} is delete"}
