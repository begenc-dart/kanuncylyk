from fastapi import Request, Response
from sqlalchemy.orm import Session, joinedload
from fastapi.encoders import jsonable_encoder
from sqlalchemy import and_, or_, desc, asc, func
import models as mod
from returns import Returns



async def create_kodeks(req: mod.KodeksShema, db: Session):
    if (req.title_tm == "" and req.title_ru == ""):
        return None
    new_add = mod.Kodeks(
        title_tm = req.title_tm,
        title_ru =req.title_ru
        )
    if new_add:
        db.add(new_add)
        db.commit()
        db.refresh(new_add)
        return new_add
    else:
        return None
async def read_kodeks(db: Session):
    user = db.query(mod.Kodeks).all()
    if user:
        return user
    else:
        return None
# update admin
async def update_kodeks(id, req: mod.KodeksShema, db: Session):
    namalar = (
        db.query(mod.Kodeks).filter(mod.Kodeks.id==id).first()
    )
    req_json = jsonable_encoder(req)
    new_update = (
        db.query(mod.Kodeks)
        .filter(mod.Kodeks.id == id)
        .update(req_json, synchronize_session=False)
    )
    db.commit()
    if new_update:
        return Returns.update
    else:
        return None
#delete namalar
async def delete_kodeks(id, db: Session):
    new_delete = (
        db.query(mod.Kodeks)
        .filter(mod.Kodeks.id == id)
        .delete(synchronize_session=False)
    )
    db.commit()
    if new_delete:
        result = {"msg": "Удалено!"}
        return result

