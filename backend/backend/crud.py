import random

from sqlalchemy.orm import Session

from . import models, schemas


def create_word(db: Session, word: schemas.WordCreate):
    db_word = models.Word(**word.dict())
    db.add(db_word)
    db.commit()
    db.refresh(db_word)
    return db_word


def get_word(db: Session, word_id):
    return db.query(models.Word).filter(models.Word.id == word_id).first()


def get_random_word(db: Session):
    a = db.query(models.Word).count()
    word_id = random.randint(1, a)
    return db.query(models.Word).filter(models.Word.id == word_id).first()


def get_words(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Word).offset(skip).limit(limit).all()
