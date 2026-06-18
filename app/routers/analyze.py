from fastapi import APIRouter

from app.services.wallet_service import (
    WalletAnalyzer,
)

router = APIRouter()


@router.post("/analyze")
def analyze_wallet(data: dict):

    wallet = data.get("wallet")

    return WalletAnalyzer.analyze(wallet)