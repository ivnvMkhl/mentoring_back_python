from fastapi import APIRouter , Depends
from fastapi_cache.decorator import cache
from sqlalchemy import select 
from app.lesson.dao import LessonDAO
from app.lesson.schemas import SLesson, SLessonADD, SLessonUPDATE
from app.lesson.rb import RBLesson

router = APIRouter(prefix="/lesson", tags=["lesson"])

@router.get("/", summary="get all lesson by filter")
@cache(expire=60)
async def get_all_lesson(request_body: RBLesson = Depends()) ->list[SLesson]:
    return await LessonDAO.find_lessons(**request_body.to_dict())


@router.get("/{id}", summary="get lesson by ID")
@cache(expire=60)
async def get_lesson_by_id(lesson_id: int) ->SLesson | dict:
    rez = await LessonDAO.find_full_data(lesson_id)
    if rez is None:
        return {'message': f'lesson with ID {lesson_id} is not found'}
    return rez    



@router.post("/add_lesson")
@cache(expire=60)
async def add_lesson(lesson: SLessonADD) -> dict:
    check = await LessonDAO.add_lesson(**lesson.model_dump())
    if check:
        return {'message': 'lesson add is success', 'lesson': lesson}
    else:
        return{'message' : 'lesson add error'}
    
@router.put("/{lesson_id}")
async def update_lesson(lesson_id: int, lesson: RBLesson = Depends()):
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
async def delete_lesson(lesson_id: int):
    check = await LessonDAO.update(filter_by={'id': lesson_id, 'is_delete' : False},
                                   is_delete = True)
    if check:
        return {'message' : 'lesson delete is succes'}
    else:
        return {'message': 'lesson delete error'}