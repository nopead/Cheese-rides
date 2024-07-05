from fastapi import APIRouter
from src.games.schemas import Game as game_schema
from src.games.models import GameGetter as game_model
from typing import List
from sqlalchemy import create_engine, select
from config import DSN
from pydantic import TypeAdapter

router = APIRouter(
    prefix="/results",
    tags=["results"]
)

sync_engine = create_engine(
    url=DSN,
    echo=True
)

ta = TypeAdapter(List[game_model])

@router.get("/", response_model=List[game_model])
async def get_results(limit: int = 5, offset: int = 0):
    with sync_engine.connect() as conn:
        stmt = (
            select(game_schema)
            .order_by(game_schema.result.desc())
            .limit(limit)
            .offset(offset)
        )
        result = conn.execute(stmt).mappings().all()
        models = ta.validate_python(result)
        conn.commit()
        return models
