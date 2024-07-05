from pydantic import BaseModel

class GameSetter(BaseModel):
    player: str
    result: int


class GameGetter(BaseModel):
    id: int
    player: str
    date: str
    result: int
