from typing import List, Optional

from pydantic import BaseModel


class WordCreate(BaseModel):
    en: str
    fr: str
    pl: str


class Word(BaseModel):
    id: int
    en: str
    fr: str
    pl: str

    class Config:
        orm_mode = True
