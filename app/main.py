from fastapi import FastAPI

from app.routers.player_game import router as player_game_router


app = FastAPI(
    title="Le Secret du Laboratoire 404",
    version="1.0.0"
)


app.include_router(player_game_router)


@app.get("/health")
def health():
    return {
        "status": "online",
        "game_title": "Le Secret du Laboratoire 404",
        "engine_version": "1.0.0"
    }