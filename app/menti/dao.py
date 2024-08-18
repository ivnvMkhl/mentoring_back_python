from sqlalchemy import select
from app.dao.base import BaseDAO
from app.menti.models import Menti
from app.database import async_session_maker


class MentiDAO(BaseDAO):
    model = Menti

    @classmethod
    async def find_full_data(cls, menti_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id = menti_id, is_delete = False)
            result = await session.execute(query)
            return result.scalar_one_or_none()
        
    @classmethod
    async def find_mentis(cls, **menti_data):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**menti_data, is_delete = False)
            result = await session.execute(query)
            menti_info = result.scalars().all()

            if not menti_info:
                return None
            return menti_info
        
        
    @classmethod
    async def find_full_data_not_scalar(cls, menti_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id = menti_id, is_delete = False)
            result = await session.execute(query)
            return result
