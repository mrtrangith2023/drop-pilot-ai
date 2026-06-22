# 🚀 DropPilot AI

## AI-Powered Airdrop Intelligence for Smarter Farming

DropPilot AI is an AI-powered assistant designed for airdrop hunters and testnet farmers.

Instead of blindly farming dozens of ecosystems, users can analyze wallet quality, evaluate farming readiness, discover high-potential opportunities, and receive AI-generated action plans tailored to their activity.

Built for the **0G Labs Vibe Coding Tournament**.

---

## 🎯 Problem

Airdrop farming has become increasingly complex.

Users spend hours navigating wallets, dashboards, quests, Discord communities, and testnet campaigns without knowing:

* Is my wallet strong enough for future rewards?
* Am I wasting time on low-value opportunities?
* Which ecosystems deserve my attention?
* What actions should I take next?

Most users rely on guesswork rather than data-driven decisions.

---

## 💡 Solution

DropPilot AI transforms wallet activity into actionable farming intelligence.

The platform analyzes wallet behavior, evaluates farming readiness, identifies potential risks, recommends promising ecosystems, and generates personalized AI strategies using Gemini.

Instead of manually researching every project, users receive a structured plan that helps them focus on higher-value opportunities.

---

## ✨ Key Features

### 🔍 Wallet Analyzer

Analyze wallet activity and estimate farming readiness using:

* Activity Score
* Transaction Count
* Wallet Age
* Wallet Score
* Sybil Risk Assessment

---

### 🏆 Wallet Tier System

Classify wallets into farming tiers:

* Beginner Farmer
* Active Farmer
* Advanced Farmer
* Elite Farmer
* Legendary Farmer

This helps users quickly understand their current farming profile.

---

### 📊 Farming Insights

Convert raw blockchain metrics into easy-to-understand insights:

* High Airdrop Potential
* Moderate Airdrop Potential
* Wallet Improvement Suggestions
* Farming Readiness Evaluation

---

### 📈 Wallet Growth Projection

Visualize wallet score progression using dashboard charts.

Provides a simple representation of wallet growth and readiness.

---

### 🔥 Opportunity Recommendations

Recommend promising ecosystems based on farming opportunities.

Current recommendations include:

* Arc
* 0G
* Monad

Each project includes:

* Opportunity Score
* Difficulty Level
* Time Commitment

---

### 🤖 Gemini AI Strategy Engine

Generate a personalized farming strategy using Gemini AI.

The report includes:

* Wallet Assessment
* Top Opportunities
* Weekly Action Plan
* Potential Airdrop Outlook
* Risk Analysis

---

### 🖥 Streamlit Dashboard

Simple and intuitive interface designed for:

* Hackathon judges
* Airdrop hunters
* Testnet farmers

---

## 🏗 Architecture

```text
User
  │
  ▼
Streamlit Frontend
  │
  ▼
FastAPI Backend
  │
  ├── Wallet Analyzer Service
  │
  ├── Recommendation Service
  │
  └── AI Strategy Service
            │
            ▼
         Gemini AI
```

---

## 🔄 AI Workflow

### Step 1

User enters a wallet address.

### Step 2

The Streamlit dashboard sends the wallet to the FastAPI backend.

### Step 3

The Wallet Analyzer generates:

* Wallet Score
* Activity Score
* Transaction Count
* Wallet Tier
* Sybil Risk

### Step 4

The Recommendation Engine returns suggested ecosystems.

### Step 5

The AI Strategy Engine sends wallet context to Gemini.

### Step 6

Gemini generates a personalized farming report.

### Step 7

Results are displayed in the dashboard.

---

## 📸 Screenshots

### Dashboard Overview

![Dashboard](docs/screenshots/dashboard.png)

### Wallet Analysis

![Wallet Analysis](docs/screenshots/wallet-analysis.png)

### Recommended Projects

![Recommendations](docs/screenshots/recommendations.png)

### AI Strategy Report

![Strategy Report](docs/screenshots/strategy-report.png)

---

## 🎬 Demo Video

Demo Video:

```text
https://youtu.be/YOUR_VIDEO_LINK
```

Replace the link above after uploading the demo video.

---

## 🛠 Tech Stack

### Frontend

* Streamlit

### Backend

* FastAPI

### AI

* Gemini AI

### Data

* JSON Dataset

### Language

* Python

### Visualization

* Pandas
* Streamlit Charts

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/drop-pilot-ai.git

cd drop-pilot-ai
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Configure Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key
```

---

### Start Backend

```bash
uvicorn app.main:app --reload
```

---

### Start Frontend

```bash
streamlit run frontend/app.py
```

---

### Open Dashboard

```text
http://localhost:8501
```

---

## 🎮 Demo Flow

1. Enter a wallet address.
2. Click Analyze.
3. Review Wallet Score and Wallet Tier.
4. Explore Farming Insights.
5. Review Recommended Projects.
6. Click Generate AI Strategy.
7. Receive a personalized farming report generated by Gemini AI.

---

## 🗺 Future Roadmap

### Phase 1

* Real wallet activity integration
* Multi-chain support
* Historical wallet tracking

### Phase 2

* Daily farming planner
* Wallet watchlists
* User accounts

### Phase 3

* Advanced Sybil detection
* Live ecosystem scoring
* Personalized opportunity engine

### Phase 4

* 0G ecosystem integrations
* Public deployment
* Community leaderboards

---

## 🏁 Hackathon Submission

### Project

DropPilot AI

### Category

AI-Powered Web3 Assistant

### Built For

0G Labs Vibe Coding Tournament

### Core Value

Help users spend less time guessing and more time focusing on high-value opportunities through AI-powered farming intelligence.

---

## 📄 License

MIT License