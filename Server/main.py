import uvicorn
from fastapi import FastAPI
from src.games.router import router as game_router
from src.results.router import router as results_router


app = FastAPI()


app.include_router(game_router)
app.include_router(results_router)


if __name__ == "__main__":
    uvicorn.run(app, port=5000, host='127.0.0.1')