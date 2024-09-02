from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache
from app.menti.dao import MentiDAO
from app.menti.schemas import SMentiAdd, SMenti
from app.menti.rb import RBMenti
from sqlalchemy import update
from app.database import async_session_maker

from sqlalchemy.exc import SQLAlchemyError

router = APIRouter(
    prefix="/menti",
    tags= ['menti']
)

@router.get("/{menti_id}")
@cache(expire=60)
async def get_menti_by_id(menti_id: int) -> SMenti | dict:
    result = await MentiDAO.find_full_data(menti_id)
    if result is None:
        return {'message' : f'menti with ID {menti_id} is not found'}
    return result


@router.get("/", summary="get all menti by filter")
@cache(expire=60)
async def get_all_lesson(request_body: RBMenti = Depends()) ->list[SMenti]:
    try:
        result = await MentiDAO.find_mentis(**request_body.to_dict())
    except SQLAlchemyError as e:
            raise e    
            return {'message' : f'menti with this parametr is not found'}
    return result



@router.post("/add_menti")
@cache(expire=60)
async def add_menti(menti: SMentiAdd) -> dict:
    check = await MentiDAO.add(**menti.model_dump())
    if check:
        return {'message': 'menti add is success', 'menti': menti}
    else:
        return{'message' : 'menti add error'}
    


@router.put("/{menti_id}")
async def menti_update(menti_id : int,  menti: RBMenti = Depends()):
    menti = menti.to_dict()
    new_values = {k:v for k,v in menti.items() if v is not None}
    print(new_values)
    check = await MentiDAO.update(
        filter_by={'id': menti_id, 'is_delete' : False},**new_values)
    if check:
        return {'message' : 'menti update succes', 'menti': menti}
    else:
        return {'message' : 'menti update error'}
    

@router.delete("/{menti_id}")
async def delete_menti(menti_id: int):
    check = await MentiDAO.update(filter_by={'id': menti_id, 'is_delete' : False},
                                   is_delete = True)
    if check:
        return {'message' : 'lesson delete is succes'}
    else:
        return {'message': 'lesson delete error'}


    