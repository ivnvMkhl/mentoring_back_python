from fastapi import APIRouter , Depends
from sqlalchemy import select 
from app.lesson.dao import LessonDAO
from app.lesson.schemas import SLesson, SLessonADD, SLessonUPDATE
from app.lesson.rb import RBLesson

from app.user.models import User
from app.user.base_config import current_active_user

router = APIRouter(prefix="/lesson", tags=["lesson"])

@router.get("/", summary="get all lesson by filter")
async def get_all_lesson(request_body: RBLesson = Depends(),user: User = Depends(current_active_user)) ->list[SLesson]:
    if user:
        return await LessonDAO.find_lessons(**request_body.to_dict())


@router.get("/{id}", summary="get lesson by ID")
async def get_lesson_by_id(lesson_id: int,user: User = Depends(current_active_user)) ->SLesson | dict:
    if user:
        rez = await LessonDAO.find_full_data(lesson_id)
        if rez is None:
            return {'message': f'lesson with ID {lesson_id} is not found'}
        return rez    



@router.post("/add_lesson")
async def add_lesson(lesson: SLessonADD,user: User = Depends(current_active_user)) -> dict:
    if user:
        check = await LessonDAO.add_lesson(**lesson.model_dump())
        if check:
            return {'message': 'lesson add is success', 'lesson': lesson}
        else:
            return{'message' : 'lesson add error'}
    
@router.put("/{lesson_id}")
async def update_lesson(lesson_id: int, lesson: RBLesson = Depends(),user: User = Depends(current_active_user)):
    if user:
        lesson = lesson.to_dict()
        new_values = {k:v for k,v in lesson.items() if v is not None}
        print(new_values)
        check = await LessonDAO.update(filter_by={'id': lesson_id, 'is_delete' : False},
                                       **new_values)
        if check:
            return {'message' : 'lesson update is succes', 'lesson': lesson}
        else:
            return {'message' : 'lesson update error' }
    
@router.delete("/{lesson_id}")
async def delete_lesson(lesson_id: int,user: User = Depends(current_active_user)):
    if user:
        check = await LessonDAO.update(filter_by={'id': lesson_id, 'is_delete' : False},
                                       is_delete = True)
        if check:
            return {'message' : 'lesson delete is succes'}
        else:
            return {'message': 'lesson delete error'}
