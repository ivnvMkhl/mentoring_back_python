from fastapi import Depends
from sqlalchemy import select, update as sqlalchemy_update, delete as sqlalchemy_delete
from sqlalchemy.exc import SQLAlchemyError
from fastapi_users import FastAPIUsers

from app.database import async_session_maker
from app.user.base_config import *

class BaseDAO:
    model = None

    @classmethod
    async def get_all(cls, **filter_by):  
        async with async_session_maker() as session:
            query = select(cls.model).filter(is_delete = False, **filter_by)
            result = await session.execute(query)
            return result.scalars().all()
        
    @classmethod
    async def find_on_or_none_by_id(cls, data_id: int):
        """
        Асинхронно находит и возвращает один экземпляр модели по id или None.

        Аргументы:
            data_id: Критерии фильтрации в виде идентификатора записи.

        Возвращает:
            Экземпляр модели или None, если ничего не найдено.
        """
        
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(is_delete = False, id = data_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()
        
        
    @classmethod
    async def find_one_or_none(cls, **filter):
        """
        Асинхронно находит и возвращает один экземпляр модели по указанным критериям или None.

        Аргументы:
            **filter_by: Критерии фильтрации в виде именованных параметров.

        Возвращает:
            Экземпляр модели или None, если ничего не найдено.
        """
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(is_delete = False, **filter)
            result = await session.execute(query)
            print(result)
            return result.scalar_one_or_none()
        
    @classmethod
    async def add(cls, **values):
        """
        Асинхронно создает новый экземпляр модели с указанными значениями.

        Аргументы:
            **values: Именованные параметры для создания нового экземпляра модели.

        Возвращает:
            Созданный экземпляр модели.
        """
        async with async_session_maker() as session:
            async with session.begin():
                new_instance = cls.model(**values)
                session.add(new_instance)
                try:
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()
                    raise e
                return new_instance
            
    @classmethod
    async def update(cls, filter_by, **values):
        """
        Асинхронно обновляет экземпляры модели, удовлетворяющие критериям фильтрации, указанным в filter_by,
        новыми значениями, указанными в values.

        Аргументы:
            filter_by: Критерии фильтрации в виде именованных параметров.
            **values: Именованные параметры для обновления значений экземпляров модели.

        Возвращает:
            Количество обновленных экземпляров модели.
        """
        async with async_session_maker() as session:
            async with session.begin():
                query = (
                    sqlalchemy_update(cls.model)
                    .where(*[getattr(cls.model, k) == v for k, v in filter_by.items()])
                    .values(**values)
                    .execution_options(synchronize_session="fetch")
                )
                result = await session.execute(query)
                try:
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()
                    raise e
                return result.rowcount
