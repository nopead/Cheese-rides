from fastapi import APIRouter
from sqlalchemy import create_engine, insert
from src.games.schemas import Game as game_schema
from src.games.models import GameSetter as game_setter_model
from config import DSN


router = APIRouter(
    prefix="/game",
    tags=["game"]
)


sync_engine = create_engine(
    url=DSN,
    echo=True
)


@router.post("/")
async def append_new_result(game: game_setter_model):
    with sync_engine.connect() as conn:
        stmt = (
            insert(game_schema)
            .values(dict(game))
        )
        conn.execute(stmt)
        conn.commit()
