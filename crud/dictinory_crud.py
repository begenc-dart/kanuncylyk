from fastapi import Request, Response
from sqlalchemy.orm import Session, joinedload
from fastapi.encoders import jsonable_encoder
from sqlalchemy import and_, or_, desc, asc, func
import models as mod
from returns import Returns



async def create_dictinary(req: mod.DictinoryShemas, db: Session):
    
    new_add = mod.Dictinory(
        title_tm=req.title_tm,
        title_ru = req.title_ru,
        description_tm = req.description_tm,
        description_ru = req.description_ru
                            )
    if new_add:
        db.add(new_add)
        db.commit()
        db.refresh(new_add)
        return new_add
    else:
        return None
# update dict
async def update_dictinary(id, req: mod.DictinoryShemas, db: Session):
    namalar = (
        db.query(mod.Dictinory).filter(mod.Dictinory.id==id).first()
    )
    if not namalar:
        return None
    # print(namalar.title)
    req_json = jsonable_encoder(req)
    new_update = (
        db.query(mod.Dictinory)
        .filter(mod.Dictinory.id == id)
        .update(req_json, synchronize_session=False)
    )
    db.commit()
    if new_update:
        return Returns.update
    else:
        return None
#delete dict
async def delete_dictinary(id, db: Session):
    new_delete = (
        db.query(mod.Dictinory)
        .filter(mod.Dictinory.id == id)
        .delete(synchronize_session=False)
    )
    db.commit()
    if new_delete:
        result = {"msg": "Удалено!"}
        return result
async def read_dict(db: Session,search : str = None,):
    print(search)
    query= db.query(mod.Dictinory)
    if search:
        query = query.filter(
            or_(
                mod.Dictinory.title_tm.ilike(f"%{search}%"),
                mod.Dictinory.title_ru.ilike(f"%{search}%"),
              
            )
        )
    sozluk = query.all()
    if sozluk:
        return sozluk
    else:
        return []