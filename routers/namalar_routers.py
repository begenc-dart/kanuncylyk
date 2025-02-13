from fastapi import APIRouter, Depends, Request, status, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from db import get_db
import crud
import models as mod
from typing import List



namalar_router = APIRouter(tags=['Namalar'])
@namalar_router.post('/api/create-namalar')
async def create_namalar(req: mod.NamalarShema, db: Session = Depends(get_db)):
    result = await crud.create_namalar(req=req, db=db,)
    result = jsonable_encoder(result)
    if result == -1:
        return HTTPException(status_code = status.HTTP_401_UNAUTHORIZED)
    elif result:
        result['msg'] = 'Создано!'
        return JSONResponse(content=result, status_code=status.HTTP_201_CREATED)
    else:
        return JSONResponse(content={"status":"some error"}, status_code=status.HTTP_204_NO_CONTENT)
########################
#      Namalar get     #
########################
@namalar_router.get('/api/get-namalar', )
async def get_namalar(db: Session = Depends(get_db),id:int=None):
    result = await crud.read_namalar(db=db,id=id)
    print(result)
    result = jsonable_encoder(result)
    if result:
        return JSONResponse(content=result, status_code=status.HTTP_200_OK)
    else:
        return JSONResponse(content={"status":"some error"}, status_code=status.HTTP_204_NO_CONTENT)

@namalar_router.put('/api/update-namalar/{id}')
async def update_operator(id: int, req: mod.NamalarShema, db: Session = Depends(get_db)):
    result = await crud.update_namalar(id=id, req=req, db=db)
    result = jsonable_encoder(result)
    if result:
        result = {'msg': 'Обновлено!'}
        return JSONResponse(content=result, status_code=status.HTTP_200_OK)
    else:
        return JSONResponse(content={"status":"some error"}, status_code=status.HTTP_204_NO_CONTENT)
@namalar_router.delete('/api/delete-namalar/{id}')
async def delete_department(id: int, db: Session = Depends(get_db)):
    result = await crud.delete_namalar(id, db)
    if result:
        result = jsonable_encoder(result)
        return JSONResponse(content=result, status_code=status.HTTP_200_OK)
    else:
        return HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail='Не удалено!')
    