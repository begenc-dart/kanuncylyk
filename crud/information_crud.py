from fastapi import Request, Response
from sqlalchemy.orm import Session, joinedload
from fastapi.encoders import jsonable_encoder
from sqlalchemy import and_, or_, desc, asc, func
import models as mod
from returns import Returns


async def create_information(req: mod.DictinoryShemas, db: Session):
    if (req.title_tm == "" and req.title_ru == ""):
        return None
    new_add = mod.Informations(
        title_tm=req.title_tm,
        title_ru=req.title_ru,
        description_tm=req.description_tm,
        description_ru=req.description_ru,

    )
    if new_add:
        db.add(new_add)
        db.commit()
        db.refresh(new_add)
        return new_add
    else:
        return None


async def read_information(db: Session):
    user = db.query(mod.Informations).all()
    if user:
        return user
    else:
        return None
# update admin


async def update_information(id, req: mod.DictinoryShemas, db: Session):
    namalar = (
        db.query(mod.Informations).filter(mod.Informations.id == id).first()
    )
    req_json = jsonable_encoder(req)
    new_update = (
        db.query(mod.Informations)
        .filter(mod.Informations.id == id)
        .update(req_json, synchronize_session=False)
    )
    db.commit()
    if new_update:
        return Returns.update
    else:
        return None
# delete namalar


async def delete_information(id, db: Session):
    new_delete = (
        db.query(mod.Informations)
        .filter(mod.Informations.id == id)
        .delete(synchronize_session=False)
    )
    db.commit()
    if new_delete:
        result = {"msg": "Удалено!"}
        return result
