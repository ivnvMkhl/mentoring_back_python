from fastapi import APIRouter, Depends
from app.menti.dao import MentiDAO
from app.menti.schemas import SMentiAdd, SMenti
from app.menti.rb import RBMenti
from sqlalchemy import update
from app.database import async_session_maker

from sqlalchemy.exc import SQLAlchemyError

from app.user.models import User
from app.user.base_config import current_active_user, current_user

router = APIRouter(
    prefix="/menti",
    tags= ['menti']
)

@router.get("/{menti_id}")
async def get_menti_by_id(menti_id: int,user: User = Depends(current_active_user)) -> SMenti | dict:
    if user:    
        result = await MentiDAO.find_full_data(menti_id)
        return result  
    if result is None:
        return {'message' : f'menti with ID {menti_id} is not found'}
    


@router.get("/", summary="get all menti by filter")
async def get_all_menti(request_body: RBMenti = Depends(),
                        user: User = Depends(current_active_user)) ->list[SMenti]:
    if user:
        try:
            result = await MentiDAO.find_mentis(**request_body.to_dict())
            return result
        except SQLAlchemyError as e:
            raise e    
            return {'message' : f'menti with this parametr is not found'}
        



@router.post("/add_menti")
async def add_menti(menti: SMentiAdd, user: User = Depends(current_active_user)) -> dict:
    if user:
        check = await MentiDAO.add(**menti.model_dump())
        if check:
            return {'message': 'menti add is success', 'menti': menti}
        else:
            return{'message' : 'menti add error'}
    


@router.put("/{menti_id}")
async def menti_update(menti_id : int,
                       menti: RBMenti = Depends(),
                       user: User = Depends(current_active_user)):
    if user:
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
async def delete_menti(menti_id: int, user: User = Depends(current_active_user)):
    if user:
        check = await MentiDAO.update(filter_by={'id': menti_id, 'is_delete' : False},
                                       is_delete = True)
        if check:
            return {'message' : 'lesson delete is succes'}
        else:
            return {'message': 'lesson delete error'}


    