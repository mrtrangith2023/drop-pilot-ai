from fastapi import APIRouter

from app.services.recommend_service import (
    RecommendService
)

router = APIRouter()


@router.get("/recommend")
def recommend():

    return RecommendService.get_recommendations()