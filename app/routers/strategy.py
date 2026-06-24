from fastapi import APIRouter

from app.services.ai_service import AIStrategy

router = APIRouter()

@router.post("/strategy")
def generate_strategy(data: dict):

    strategy = AIStrategy.generate(data)

    return {
        "strategy": strategy
    }