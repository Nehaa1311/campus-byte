from fastapi import FastAPI
from . import models
from .database import engine

# Create all tables if they don't exist yet
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Campus Byte")


@app.get("/")
def home():
    return {"message": "Campus Byte is running"}