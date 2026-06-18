import random


class WalletAnalyzer:

    @staticmethod
    def analyze(wallet_address: str):

        activity_score = random.randint(50, 100)

        wallet_age = random.randint(30, 100)

        tx_count = random.randint(10, 500)

        wallet_score = int(
            (activity_score + wallet_age) / 2
        )

        if wallet_score >= 90:

            wallet_tier = "Legendary Farmer"

        elif wallet_score >= 80:

            wallet_tier = "Elite Farmer"

        elif wallet_score >= 70:

            wallet_tier = "Advanced Farmer"

        elif wallet_score >= 60:

            wallet_tier = "Active Farmer"

        else:

            wallet_tier = "Beginner Farmer"

        sybil_risk = (
            "Low"
            if wallet_score > 70
            else "Medium"
        )

        return {
            "wallet": wallet_address,
            "wallet_score": wallet_score,
            "wallet_tier": wallet_tier,
            "activity_score": activity_score,
            "wallet_age": wallet_age,
            "tx_count": tx_count,
            "sybil_risk": sybil_risk,
        }