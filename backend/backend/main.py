from typing import List
import random

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from fastapi_crudrouter import SQLAlchemyCRUDRouter

from . import models, schemas
from .database import SessionLocal, engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db = SessionLocal()
if db.query(models.Word).count() == 0:
    with open("words2.txt", "r") as f:
        for line in f:
            en, fr, pl = line.strip().split(",")
            en, fr, pl = en.capitalize(), fr.capitalize(), pl.capitalize()
            word = models.Word(**{"en": en, "fr": fr, "pl": pl})
            db.add(word)
            db.commit()
            db.refresh(word)


@app.get("/random_word/", response_model=schemas.Word)
def get_random_word(db: Session = Depends(get_db)):
    a = db.query(models.Word).count()
    word_id = random.randint(1, a)
    return db.query(models.Word).filter(models.Word.id == word_id).first()


word_router = SQLAlchemyCRUDRouter(
    schema=schemas.Word,
    create_schema=schemas.WordCreate,
    db_model=models.Word,
    db=get_db,
    prefix="word",
    delete_all_route=False,
)
app.include_router(word_router)
