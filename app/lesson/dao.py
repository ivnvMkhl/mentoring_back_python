from sqlalchemy import select, update
from sqlalchemy.orm import joinedload

from app.dao.base import BaseDAO
from app.lesson.models import Lesson
from app.database import async_session_maker
from app.lesson.schemas import SLessonUPDATE, SLessonADD


class LessonDAO(BaseDAO):
    model = Lesson

    @classmethod
    async def find_one_or_none_by_id(cls, lesson_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id = lesson_id, is_delete = False)
            result = await session.execute(query)
            return result.scalar_one_or_none()
    
    @classmethod
    async def find_full_data(cls, lesson_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id = lesson_id, is_delete = False)
            result = await session.execute(query)
            lesson_info = result.scalar_one_or_none()

            if not lesson_info:
                return None
            return lesson_info
        
    @classmethod
    async def find_lessons(cls, **lesson_data):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**lesson_data, is_delete = False)
            result = await session.execute(query)
            lesson_info = result.scalars().all()

            if not lesson_info:
                return None
            return lesson_info
        
    @classmethod
    async def add_lesson(cls, **lesson_data: dict):
        async with async_session_maker() as session:
            async with session.begin():
                new_lesson = cls.model(**lesson_data)
                session.add(new_lesson)
                await session.flush()
                new_lesson_id = new_lesson.id
                await session.commit()
                return new_lesson_id


                

