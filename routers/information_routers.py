from fastapi import APIRouter, Depends, Request, status, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from db import get_db
import crud
import models as mod
from typing import List


informations_routers = APIRouter(tags=['Information'])


@informations_routers.post('/api/create-informations')
async def create_kodeks(req: mod.DictinoryShemas, db: Session = Depends(get_db)):
    result = await crud.create_information(req, db)
    result = jsonable_encoder(result)
    if result == -1:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    elif result:
        result['msg'] = 'Создано!'
        return JSONResponse(content=result, status_code=status.HTTP_201_CREATED)
    else:
        return JSONResponse(content={"status": "some error"}, status_code=status.HTTP_204_NO_CONTENT)
########################
#      Namalar get     #
########################


@informations_routers.get('/api/get-information', )
async def get_namalar(db: Session = Depends(get_db),):
    result = await crud.read_information(db)
    print(result)
    result = jsonable_encoder(result)
    if result:
        return JSONResponse(content=result, status_code=status.HTTP_200_OK)
    else:
        return JSONResponse(content={"status": "some error"}, status_code=status.HTTP_204_NO_CONTENT)


@informations_routers.put('/api/update-information/{id}')
async def update_information(id: int, req: mod.DictinoryShemas, db: Session = Depends(get_db)):
    result = await crud.update_information(id=id, req=req, db=db)
    result = jsonable_encoder(result)
    if result:
        result = {'msg': 'Обновлено!'}
        return JSONResponse(content=result, status_code=status.HTTP_200_OK)
    else:
        return JSONResponse(content={"status": "some error"}, status_code=status.HTTP_204_NO_CONTENT)


@informations_routers.delete('/api/delete-information/{id}')
async def delete_information(id: int, db: Session = Depends(get_db)):
    result = await crud.delete_information(id, db)
    if result:
        result = jsonable_encoder(result)
        return JSONResponse(content=result, status_code=status.HTTP_200_OK)
    else:
        return HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail='Не удалено!')
