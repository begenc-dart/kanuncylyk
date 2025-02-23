from fastapi import Request, Response
from sqlalchemy.orm import Session, joinedload
from fastapi.encoders import jsonable_encoder
from sqlalchemy import and_, or_, desc, asc, func
import models as mod
from returns import Returns



async def create_namalar(req: mod.NamalarShema, db: Session):
    if (req.title_tm == "" and req.title_ru == ""):
        return None
    new_add = mod.Namalar(title_tm = req.title_tm,
                          title_ru = req.title_ru,
                            kodeks_id = req.kodeks_id)
    if new_add:
        db.add(new_add)
        db.commit()
        db.refresh(new_add)
        return new_add
    else:
        return None
async def read_namalar(db: Session,id:int=None,  skip: int = 0, limit: int = 10):
    kodeks = db.query(mod.Namalar)
    if id:
        kodeks = kodeks.filter(mod.Namalar.kodeks_id==id)
    kanunlar=kodeks.offset(skip).limit(limit).all()
    if kanunlar:
        return kanunlar
    else:
        return []
# update admin
async def update_namalar(id, req: mod.NamalarShema, db: Session):
    namalar = (
        db.query(mod.Namalar).filter(mod.Namalar.id==id).first()
    )
   
    req_json = jsonable_encoder(req)
    new_update = (
        db.query(mod.Namalar)
        .filter(mod.Namalar.id == id)
        .update(req_json, synchronize_session=False)
    )
    db.commit()
    if new_update:
        return Returns.update
    else:
        return None
#delete namalar
async def delete_namalar(id, db: Session):
    new_delete = (
        db.query(mod.Namalar)
        .filter(mod.Namalar.id == id)
        .delete(synchronize_session=False)
    )
    db.commit()
    if new_delete:
        result = {"msg": "Удалено!"}
        return result

