import requests
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="DropPilot AI",
    page_icon="🚀",
    layout="wide"
)

# =====================
# SIDEBAR
# =====================

with st.sidebar:

    st.title("🚀 DropPilot AI")

    st.markdown("---")

    st.subheader("About")

    st.write(
        "AI-powered assistant for airdrop hunters and testnet farmers."
    )

    st.markdown("---")

    st.subheader("Features")

    st.success("Wallet Analyzer")

    st.success("Wallet Tier System")

    st.success("AI Strategy Generator")

    st.success("Project Recommendations")

    st.markdown("---")

    st.caption(
        "Built for 0G Labs Vibe Coding Tournament 2026"
    )

    st.markdown("---")

    st.subheader("Architecture")

    st.code("""
    User
    ↓
    Streamlit
    ↓
    FastAPI
    ↓
    Wallet Analyzer
    ↓
    Gemini AI
    ↓
    Strategy Report
    """)

# =====================
# MAIN PAGE
# =====================

st.title("🚀 DropPilot AI")

wallet = st.text_input(
    "Wallet Address"
)

# =====================
# ANALYZE
# =====================

if st.button("Analyze"):

    try:

        response = requests.post(
            "http://127.0.0.1:8000/analyze",
            json={"wallet": wallet}
        )

        if response.status_code == 200:

            st.session_state["result"] = (
                response.json()
            )

        else:

            st.error(
                f"API Error: {response.text}"
            )

    except Exception as e:

        st.error(str(e))

# =====================
# SHOW RESULT
# =====================

if "result" in st.session_state:

    result = st.session_state["result"]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Wallet Score",
            result["wallet_score"]
        )

    with col2:
        st.metric(
            "Activity",
            result["activity_score"]
        )

    with col3:
        st.metric(
            "Tx Count",
            result["tx_count"]
        )

    st.write(
        f"Sybil Risk: {result['sybil_risk']}"
    )

    st.markdown("---")

    tier = result["wallet_tier"]

    if tier == "Legendary Farmer":

        st.success(
            f"👑 Wallet Tier: {tier}"
        )

    elif tier == "Elite Farmer":

        st.success(
            f"🏆 Wallet Tier: {tier}"
        )

    elif tier == "Advanced Farmer":

        st.info(
            f"🚀 Wallet Tier: {tier}"
        )

    elif tier == "Active Farmer":

        st.warning(
            f"⚡ Wallet Tier: {tier}"
        )

    else:

        st.error(
            f"🌱 Wallet Tier: {tier}"
        )

    st.subheader("📊 Farming Insights")

    if result["wallet_score"] >= 80:

        st.write("✅ High Airdrop Potential")
        st.write("✅ Low Sybil Risk")
        st.write("✅ Strong Wallet Activity")

    elif result["wallet_score"] >= 60:

        st.write("⚡ Moderate Airdrop Potential")
        st.write("⚡ Needs More Activity")

    else:

        st.write("⚠️ Increase Wallet Usage")
        st.write("⚠️ Build More On-chain History")

    st.subheader("📈 Wallet Growth Projection")

    chart_data = pd.DataFrame(
        {
            "Wallet Score": [
                max(result["wallet_score"] - 30, 10),
                max(result["wallet_score"] - 20, 20),
                max(result["wallet_score"] - 10, 30),
                result["wallet_score"]
            ]
        },
        index=[
            "Week 1",
            "Week 2",
            "Week 3",
            "Current"
        ]
    )

    st.line_chart(chart_data)

# =====================
# PROJECTS
# =====================

st.subheader("🔥 Recommended Projects")

recommendations = requests.get(
    "http://127.0.0.1:8000/recommend"
).json()

for project in recommendations:

    st.write(
        f"✅ {project['name']} "
        f"(Score: {project['score']})"
    )

# =====================
# AI STRATEGY
# =====================

if (
    "result" in st.session_state
    and st.button("🧠 Generate AI Strategy")
):

    result = st.session_state["result"]

    with st.spinner(
        "DropPilot AI is analyzing your wallet..."
    ):

        response = requests.post(
            "http://127.0.0.1:8000/strategy",
            json=result
        )

        if response.status_code == 200:

            st.session_state["strategy"] = response.json()

            if "strategy" in st.session_state:

                st.subheader("🧠 AI Strategy Report")

                st.markdown(
                    st.session_state["strategy"]["strategy"]
                )

        else:

            st.error(
                response.text
            )