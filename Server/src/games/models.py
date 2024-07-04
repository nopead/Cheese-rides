from pydantic import BaseModel
from datetime import datetime


class GameSetter(BaseModel):
    player_id: int
    result: int


class GameGetter(BaseModel):
    id: int
    nickname: str
    date: str
    score: int