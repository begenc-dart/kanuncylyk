from fastapi import APIRouter, Depends, Request, status, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from db import get_db
import crud
import models as mod
from typing import List



dictinory_router = APIRouter(tags=['Dictinary'])
@dictinory_router.post('/api/create-dictinary')
async def create_dict(req: mod.DictinoryShemas, db: Session = Depends(get_db)):
    result = await crud.create_dictinary(req=req, db=db,)
    result = jsonable_encoder(result)
    if result == -1:
        return HTTPException(status_code = status.HTTP_401_UNAUTHORIZED)
    elif result:
        result['msg'] = 'Создано!'
        return JSONResponse(content=result, status_code=status.HTTP_201_CREATED)
    else:
        return JSONResponse(content={"status":"some error"}, status_code=status.HTTP_204_NO_CONTENT)

@dictinory_router.put('/api/update-dictinary/{id}')
async def update_dict(id: int, req: mod.DictinoryShemas, db: Session = Depends(get_db)):
    result = await crud.update_dictinary(id=id, req=req, db=db)
    result = jsonable_encoder(result)
    if result:
        result = {'msg': 'Обновлено!'}
        return JSONResponse(content=result, status_code=status.HTTP_200_OK)
    else:
        return JSONResponse(content={"status":"some error"}, status_code=status.HTTP_204_NO_CONTENT)
@dictinory_router.delete('/api/delete-dictinary/{id}')
async def delete_dict(id: int, db: Session = Depends(get_db)):
    result = await crud.delete_dictinary(id, db)
    if result:
        result = jsonable_encoder(result)
        return JSONResponse(content=result, status_code=status.HTTP_200_OK)
    else:
        return HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail='Не удалено!')
@dictinory_router.get('/api/get-dictinary', )
async def get_dict(search : str= None,db: Session = Depends(get_db),  skip: int = 0, limit: int = 10):
    if search:
        # Ensure the string is decoded in case it's not properly decoded
        search = search.encode('utf-8').decode('utf-8')
        
    result = await crud.read_dict(db=db,search=search,skip=skip,limit=limit)
    result = jsonable_encoder(result)
    if result:
        return JSONResponse(content=result, status_code=status.HTTP_200_OK)
    else:
        return JSONResponse(content=jsonable_encoder([]), status_code=status.HTTP_200_OK)
