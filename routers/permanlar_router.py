from fastapi import APIRouter, Depends, File, Request, UploadFile, status, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from db import get_db
import crud
import models as mod
from typing import List


permanlar_router = APIRouter(tags=['permanlar'])


@permanlar_router.post('/api/create-perman')
async def create_perman(req: mod.PermanlarShema, db: Session = Depends(get_db)):
    result = await crud.create_perman(req=req, db=db,)
    result = jsonable_encoder(result)
    if result == -1:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    elif result:
        result['msg'] = 'Создано!'
        return JSONResponse(content=result, status_code=status.HTTP_201_CREATED)
    else:
        return JSONResponse(content={"status": "some error"}, status_code=status.HTTP_204_NO_CONTENT)
# pdf update


@permanlar_router.put('/api/update-pdf/{id}')
async def update_pdf(id: int,  db: Session = Depends(get_db), file: UploadFile = File(...), file_rus: UploadFile = File(...)):
    result = await crud.update_pdf(id, file,file_rus, "pdf", "pdf_rus",db)
    if result == -1:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    if result:
        result = jsonable_encoder(result)
        return JSONResponse(content=result, status_code=status.HTTP_200_OK)
    else:
        return HTTPException(status_code=status.HTTP_204_NO_CONTENT)
# pdf update


@permanlar_router.put('/api/update-doc/{id}')
async def update_docs(id: int,  db: Session = Depends(get_db), file: UploadFile = File(...),file_rus: UploadFile = File(...),):
    result = await crud.update_pdf(id, file,file_rus, "doc","doc_rus", db)
    if result == -1:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    if result:
        result = jsonable_encoder(result)
        return JSONResponse(content=result, status_code=status.HTTP_200_OK)
    else:
        return HTTPException(status_code=status.HTTP_204_NO_CONTENT)


@permanlar_router.put('/api/update-active/{id}')
async def update_operator(id: int, active: bool, db: Session = Depends(get_db)):
    result = await crud.update_active(id=id, check=active, db=db)
    result = jsonable_encoder(result)
    if result:
        result = {'msg': 'Обновлено!'}
        return JSONResponse(content=result, status_code=status.HTTP_200_OK)
    else:
        return JSONResponse(content={"status": "some error"}, status_code=status.HTTP_204_NO_CONTENT)
# get perman

@permanlar_router.get('/api/get-permanlar/',)
async def get_permanlar(namalar_id: int= None,  skip: int = 0, limit: int = 10,active: bool = None, year: int = None, month: str = None, search: str = None, db: Session = Depends(get_db)):
    if search:
        # Ensure the string is decoded in case it's not properly decoded
        search = search.encode('utf-8').decode('utf-8')
        print(search)
    # print(namalar_id)
    result = await crud.read_permanlar(namalar_id=namalar_id,skip=skip,limit=limit, db=db, active=active, year=year, month=month, search=search)
    result = jsonable_encoder(result)
    if result:
        return JSONResponse(content=result, status_code=status.HTTP_200_OK)
    else:
        return JSONResponse(content=[], status_code=status.HTTP_200_OK)


@permanlar_router.get('/api/perman/get_one/{id}',)
async def get_permanlar(id: int, db: Session = Depends(get_db)):
    result = await crud.read_one(id=id, db=db)
    result = jsonable_encoder(result)
    if result:
        return JSONResponse(content=result, status_code=status.HTTP_200_OK)
    else:
        return JSONResponse(content=jsonable_encoder({"status": "some error"}), status_code=status.HTTP_204_NO_CONTENT)


@permanlar_router.delete('/api/delete-permanlar/{id}')
async def delete_permanlar(id: int, db: Session = Depends(get_db)):
    result = await crud.delete_permanlar(id, db)
    if result:
        result = jsonable_encoder(result)
        return JSONResponse(content=result, status_code=status.HTTP_200_OK)
    else:
        return HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail='Не удалено!')
