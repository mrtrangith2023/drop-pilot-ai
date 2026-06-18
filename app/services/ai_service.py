import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


class AIStrategy:

    @staticmethod
    def generate(data):

        prompt = f"""
You are DropPilot AI.

An AI-powered crypto opportunity analyst.

Analyze:

Wallet Score: {data['wallet_score']}
Activity Score: {data['activity_score']}
Transaction Count: {data['tx_count']}
Sybil Risk: {data['sybil_risk']}
Wallet Tier: {data['wallet_tier']}

Target Ecosystems:
Arc
0G
Monad

Generate:

# Wallet Assessment

# Top Opportunities

# Weekly Action Plan

# Potential Airdrop Outlook

# Risk Analysis

Keep under 300 words.
Use markdown formatting.
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text