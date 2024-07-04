from fastapi import APIRouter

router = APIRouter(
    prefix="/players",
    tags=["players"]
)

@router.get("/")
async def get_players():
    pass