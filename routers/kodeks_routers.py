from fastapi import APIRouter, Depends, Request, status, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from db import get_db
import crud
import models as mod
from typing import List



kodeks_routers = APIRouter(tags=['Kodekslar'])
@kodeks_routers.post('/api/create-kodeks')
async def create_kodeks(req: mod.KodeksShema, db: Session = Depends(get_db)):
    result = await crud.create_kodeks(req=req, db=db,)
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
@kodeks_routers.get('/api/get-kodeks', )
async def get_namalar(db: Session = Depends(get_db),):
    result = await crud.read_kodeks(db=db)
    print(result)
    result = jsonable_encoder(result)
    if result:
        return JSONResponse(content=result, status_code=status.HTTP_200_OK)
    else:
        return JSONResponse(content={"status":"some error"}, status_code=status.HTTP_204_NO_CONTENT)

@kodeks_routers.put('/api/update-kodeks/{id}')
async def update_operator(id: int, req: mod.KodeksShema, db: Session = Depends(get_db)):
    result = await crud.update_kodeks(id=id, req=req, db=db)
    result = jsonable_encoder(result)
    if result:
        result = {'msg': 'Обновлено!'}
        return JSONResponse(content=result, status_code=status.HTTP_200_OK)
    else:
        return JSONResponse(content={"status":"some error"}, status_code=status.HTTP_204_NO_CONTENT)
@kodeks_routers.delete('/api/delete-kodeks/{id}')
async def delete_department(id: int, db: Session = Depends(get_db)):
    result = await crud.delete_kodeks(id, db)
    if result:
        result = jsonable_encoder(result)
        return JSONResponse(content=result, status_code=status.HTTP_200_OK)
    else:
        return HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail='Не удалено!')
    