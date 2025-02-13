from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from db import engine, Base
from routers import namalar_router, permanlar_router, dictinory_router, kodeks_routers, informations_routers
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]
methods = ["*"]
headers = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=methods,
    allow_headers=headers,
)
app.mount('/uploads', StaticFiles(directory="uploads"), name="uploads")
Base.metadata.create_all(engine)
app.include_router(kodeks_routers)
app.include_router(namalar_router)
app.include_router(permanlar_router)
app.include_router(dictinory_router)
app.include_router(informations_routers)
