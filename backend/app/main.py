from fastapi import FastAPI
from . import models
from .database import engine
from .routers import auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Campus Byte")

app.include_router(auth.router)


@app.get("/")
def home():
    return {"message": "Campus Byte is running"}