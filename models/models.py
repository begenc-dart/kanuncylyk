from sqlalchemy import Column, String, Integer, DateTime, Float, Boolean, ForeignKey, Date, Time
from datetime import datetime
from sqlalchemy.orm import relationship
from db import Base
from fastapi_storages import FileSystemStorage
from fastapi_storages.integrations.sqlalchemy import FileType

class Kodeks(Base):
    __tablename__="kodekslar"
    id = Column(Integer, primary_key=True, index=True)
    title_tm = Column(String)
    title_ru= Column(String)
    
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    namalar      = relationship('Namalar' , back_populates='kodks')

class Namalar(Base):
    __tablename__="namalar"
    id = Column(Integer, primary_key=True, index=True)
    title_tm = Column(String)
    title_ru = Column(String)
    count = Column(Integer,default=0)
    kodeks_id = Column(Integer, ForeignKey('kodekslar.id', ondelete='CASCADE'))
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    perman      = relationship('Permanlar' , back_populates='namalar')
    kodks      = relationship('Kodeks' , back_populates='namalar')

class Permanlar(Base):
    __tablename__="permanlar"
    id = Column(Integer, primary_key=True, index=True)
    title_tm = Column(String)
    title_ru = Column(String)
    month = Column(String)
    month_ru = Column(String)
    year = Column(Integer)
    number = Column(String)
    namalar_id = Column(Integer, ForeignKey('namalar.id', ondelete='CASCADE'))
    pdf = Column(String)
    pdf_rus = Column(String)
    doc = Column(String)
    doc_rus = Column(String)
    is_active = Column(Boolean,default=False)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    namalar = relationship('Namalar' , back_populates='perman')

class Dictinory(Base):
    __tablename__="dictinory"
    id = Column(Integer, primary_key=True, index=True)
    title_tm = Column(String)
    title_ru = Column(String)
    description_tm = Column(String)
    description_ru = Column(String)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

class Informations(Base):
    __tablename__ = "informations"
    id = Column(Integer, primary_key=True, index=True)
    title_tm = Column(String)
    title_ru = Column(String)
    description_tm = Column(String)
    description_ru = Column(String)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)