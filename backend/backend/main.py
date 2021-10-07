from typing import List
import random

from fastapi import Depends, FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from fastapi_crudrouter import SQLAlchemyCRUDRouter

from . import models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = SQLAlchemyCRUDRouter(
    schema=schemas.Word,
    create_schema=schemas.WordCreate,
    db_model=models.Word,
    db=get_db,
    prefix="word",
    delete_all_route=False,
)


@app.get("/random_word/", response_model=schemas.Word)
def get_random_word(db: Session = Depends(get_db)):
    a = db.query(models.Word).count()
    word_id = random.randint(1, a)
    return db.query(models.Word).filter(models.Word.id == word_id).first()


app.include_router(router)
