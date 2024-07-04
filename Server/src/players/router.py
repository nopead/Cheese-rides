from fastapi import APIRouter

router = APIRouter(
    prefix="/players",
    tags=["players"]
)

#Endpoint для получения игроков
@router.get("/")
async def get_players():
    pass