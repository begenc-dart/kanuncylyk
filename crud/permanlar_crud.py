from fastapi import Request, Response
from sqlalchemy.orm import Session, joinedload
from fastapi.encoders import jsonable_encoder
from sqlalchemy import and_, or_, desc, asc, func
import models as mod
from returns import Returns
import upload_depends


async def create_perman(req: mod.PermanlarShema, db: Session):
    if (req.title_tm == "" and req.month == "" and req.number == "" and req.title_ru == ""):
        return None
    new_add = mod.Permanlar(
        title_tm=req.title_tm,
        title_ru=req.title_ru,
        month=req.month,
        month_ru=req.month_ru,
        year=req.year,
        number=req.number,
        namalar_id=req.namalar_id
    )
    if new_add:
        db.add(new_add)
        db.commit()
        db.refresh(new_add)
        return new_add
    else:
        return None


async def read_permanlar(namalar_id: int, db: Session, active: bool = None, year: int = None, month: str = None, search: str = None):
    query = db.query(mod.Permanlar).filter(
        mod.Permanlar.namalar_id == namalar_id)
    if year is not None:
        query = query.filter(mod.Permanlar.year == year)
    if active is not None:
        query = query.filter(mod.Permanlar.is_active == active)
    if month is not None:
        query = query.filter(mod.Permanlar.month == month)
    if search:

        query = query.filter(
            or_(
                mod.Permanlar.title_tm.ilike(f"%{search}%"),
                mod.Permanlar.title_ru.ilike(f"%{search}%"),
            )
        )
    perman = query.all()
    if perman:
        return perman
    else:
        return []


async def read_one(id: int, db: Session):
    user = db.query(mod.Permanlar).filter(mod.Permanlar.id == id).first()
    if user:
        return user
    else:
        return None
# update pdf


async def update_pdf(id, file, file_rus, link: str, link_rus: str, db: Session):
    pdf = upload_depends.upload_image(directory=link, file=file)
    pdf_rus = upload_depends.upload_image(directory=link, file=file_rus)
    req_json = jsonable_encoder({
        link: pdf,
        link_rus: pdf_rus,
    })
    new_update = (
        db.query(mod.Permanlar)
        .filter(mod.Permanlar.id == id)
        .update(req_json, synchronize_session=False)
    )
    db.commit()
    if new_update:
        return Returns.update
    else:
        return None


async def update_active(id, check: bool, db: Session):

    req_json = jsonable_encoder({
        "is_active": check
    })
    new_update = (
        db.query(mod.Permanlar)
        .filter(mod.Permanlar.id == id)
        .update(req_json, synchronize_session=False)
    )
    db.commit()
    if new_update:
        return Returns.update
    else:
        return None


async def delete_permanlar(id, db: Session):
    new_delete = (
        db.query(mod.Permanlar)
        .filter(mod.Permanlar.id == id)
        .delete(synchronize_session=False)
    )
    db.commit()
    if new_delete:
        result = {"msg": "Удалено!"}
        return result
