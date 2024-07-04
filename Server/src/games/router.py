from fastapi import APIRouter
from src.games.models import GameGetter, GameSetter
from typing import List

router = APIRouter(
    prefix="/game",
    tags=["game"]
)


@router.post("/", response_model=int)
async def append_new_result(game: GameSetter):
    pass