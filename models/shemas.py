from pydantic import BaseModel

class KodeksShema(BaseModel):
    title_tm : str
    title_ru : str
class NamalarShema(BaseModel):
    title_tm:str
    title_ru:str
    kodeks_id:int
class PermanlarShema(BaseModel):
    title_tm : str
    title_ru : str
    month : str
    month_ru : str
    year : int = 0
    number : str 
    namalar_id : int = 0
class DictinoryShemas(BaseModel):
    title_tm : str
    title_ru : str
    description_tm : str
    description_ru : str
