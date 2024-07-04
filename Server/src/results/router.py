from fastapi import APIRouter
from src.games.models import GameGetter
from typing import List

router = APIRouter(
    prefix="/results",
    tags=["results"]
)

fake_results = [
    {"id": 1, "nickname": "vova", "date": "2024-07-01", "score": 120},
    {"id": 2, "nickname": "vasya", "date": "2024-07-01", "score": 80},
    {"id": 3, "nickname": "petya", "date": "2024-07-01", "score": 50},
    {"id": 4, "nickname": "vova", "date": "2024-07-01", "score": 40},
    {"id": 5, "nickname": "vova", "date": "2024-07-01", "score": 200},
]

@router.get("/", response_model=List[GameGetter])
async def get_results(limit: int = 5, offset: int = 0):
    return fake_results