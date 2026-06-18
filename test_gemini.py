from app.services.ai_service import AIStrategy

result = AIStrategy.generate(
    {
        "wallet_score": 85,
        "activity_score": 95,
        "tx_count": 280,
        "sybil_risk": "Low"
    }
)

print(result)