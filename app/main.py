from fastapi import FastAPI

from app.routers.analyze import router as analyze_router
from app.routers.recommend import (
    router as recommend_router
)
from app.routers.strategy import router as strategy_router

app = FastAPI(
    title="DropPilot AI"
)

app.include_router(
    analyze_router
)


@app.get("/")
def home():
    return {
        "project": "DropPilot AI"
    }


app.include_router(recommend_router)
app.include_router(strategy_router)