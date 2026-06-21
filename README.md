# DropPilot AI

DropPilot AI is an AI-powered dashboard for airdrop hunters and testnet farmers. It analyzes a wallet profile, estimates farming readiness, recommends high-value ecosystems, and generates a concise action plan using an AI strategy agent.

Built for the **0G Labs Vibe Coding Tournament**.

## Problem

Airdrop hunters often waste time farming low-signal projects, repeating generic tasks, and guessing which ecosystems deserve attention. It is difficult to quickly understand whether a wallet looks active, trustworthy, and ready for potential future reward campaigns.

## Solution

DropPilot AI turns wallet activity into a simple farming intelligence report. The app scores the wallet, assigns a farmer tier, highlights Sybil-risk signals, recommends projects, and generates a weekly AI strategy so users can focus their time on better opportunities.

## Features

- **Wallet Analyzer**: Scores wallet readiness using activity, wallet age, and transaction count signals.
- **Wallet Tier System**: Classifies users as Beginner, Active, Advanced, Elite, or Legendary farmers.
- **Sybil Risk Indicator**: Gives a quick view of wallet quality and risk level.
- **Growth Projection**: Visualizes wallet score progression in a simple dashboard chart.
- **Project Recommendations**: Ranks recommended ecosystems by opportunity score.
- **AI Strategy Generator**: Produces a markdown strategy report with wallet assessment, top opportunities, weekly actions, airdrop outlook, and risk analysis.
- **Streamlit Dashboard**: Provides a lightweight and judge-friendly user interface for the hackathon demo.

## Architecture

```text
User
  |
  v
Streamlit Frontend
  |
  v
FastAPI Backend
  |
  +--> Wallet Analyzer Service
  |
  +--> Recommendation Service
  |
  +--> AI Strategy Service
            |
            v
        Gemini AI
```

## AI Workflow

1. The user enters a wallet address in the Streamlit dashboard.
2. The frontend sends the wallet to the FastAPI `/analyze` endpoint.
3. The backend generates a wallet profile with score, tier, transaction count, activity score, wallet age, and Sybil risk.
4. The dashboard displays the analysis and fetches recommended projects from `/recommend`.
5. When the user clicks **Generate AI Strategy**, the frontend sends the wallet analysis to `/strategy`.
6. The AI service sends a structured prompt to Gemini.
7. Gemini returns a concise farming strategy report for the user.

## Screenshots

Add screenshots or demo GIFs here before submitting:

- Dashboard overview
- Wallet analysis cards
- Recommended projects
- AI strategy report

```text
docs/screenshots/dashboard.png
docs/screenshots/strategy-report.png
```

## Tech Stack

- **Frontend**: Streamlit
- **Backend**: FastAPI
- **AI Model**: Gemini
- **Data**: JSON project dataset
- **Language**: Python
- **Visualization**: Pandas + Streamlit charts

## Installation

Clone the project:

```bash
git clone <your-repo-url>
cd drop-pilot-ai
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Start the FastAPI backend:

```bash
uvicorn app.main:app --reload
```

In a second terminal, start the Streamlit frontend:

```bash
streamlit run frontend/app.py
```

Open the app:

```text
http://localhost:8501
```

## Demo

1. Start the FastAPI backend.
2. Start the Streamlit dashboard.
3. Enter a wallet address.
4. Click **Analyze** to generate the wallet score, tier, risk indicator, insights, and growth projection.
5. Review the recommended projects.
6. Click **Generate AI Strategy** to produce the AI-powered farming plan.

The current MVP uses simulated wallet scoring logic for fast hackathon demonstration while keeping the service boundaries ready for real on-chain integrations.

## Future Roadmap

- Integrate real on-chain wallet activity from block explorers and RPC providers.
- Add multi-chain wallet analysis across 0G, EVM testnets, and emerging ecosystems.
- Build a personalized daily farming planner.
- Add task completion tracking and wallet progress history.
- Improve Sybil-risk detection with behavioral heuristics.
- Add project-specific checklists for testnet campaigns.
- Support user accounts and saved wallet profiles.
- Deploy the backend and frontend for public demo access.
- Expand the recommendation engine with live ecosystem data.
- Add deeper 0G ecosystem analysis and opportunity scoring.

## Status

Hackathon MVP built for the **0G Labs Vibe Coding Tournament**.
