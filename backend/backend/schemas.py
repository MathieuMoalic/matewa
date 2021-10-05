from typing import List, Optional

from pydantic import BaseModel


class WordBase(BaseModel):
    en: str
    fr: str
    pl: str


class WordCreate(WordBase):
    pass


class Word(WordBase):
    id: int

    class Config:
        orm_mode = True
