import requests
import streamlit as st
import pandas as pd


def render_page_styles():
    st.markdown(
        """
        <style>
            .block-container {
                padding-top: 2rem;
                padding-bottom: 3rem;
            }

            .hero {
                padding: 1.25rem 0 1.75rem;
            }

            .hero h1 {
                margin-bottom: 0.25rem;
            }

            .hero p {
                color: #64748b;
                font-size: 1.05rem;
                margin: 0;
            }

            .metric-card {
                background: #ffffff;
                border: 1px solid #e5e7eb;
                border-radius: 8px;
                box-shadow: 0 1px 2px rgba(15, 23, 42, 0.04);
                padding: 1rem;
            }

            .metric-label {
                color: #64748b;
                font-size: 0.85rem;
                font-weight: 600;
                margin-bottom: 0.35rem;
                text-transform: uppercase;
            }

            .metric-value {
                color: #0f172a;
                font-size: 2rem;
                font-weight: 750;
                line-height: 1;
            }

            .tier-badge {
                border-radius: 999px;
                display: inline-block;
                font-weight: 700;
                margin: 0.35rem 0 0.75rem;
                padding: 0.35rem 0.8rem;
            }

            .tier-legendary,
            .tier-elite {
                background: #dcfce7;
                color: #166534;
            }

            .tier-advanced {
                background: #dbeafe;
                color: #1d4ed8;
            }

            .tier-active {
                background: #fef3c7;
                color: #92400e;
            }

            .tier-beginner {
                background: #fee2e2;
                color: #991b1b;
            }

            .insight-box,
            .project-card,
            .report-box {
                background: #ffffff;
                border: 1px solid #e5e7eb;
                border-radius: 8px;
                padding: 1rem;
            }

            .project-card {
                margin-bottom: 0.75rem;
            }

            .project-name {
                color: #0f172a;
                font-size: 1.05rem;
                font-weight: 700;
            }

            .project-meta {
                color: #64748b;
                font-size: 0.9rem;
                margin-top: 0.2rem;
            }

            .report-box {
                line-height: 1.65;
            }
        </style>
        """,
        unsafe_allow_html=True
    )


def render_metric_card(label, value):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def tier_class(tier):
    return {
        "Legendary Farmer": "tier-legendary",
        "Elite Farmer": "tier-elite",
        "Advanced Farmer": "tier-advanced",
        "Active Farmer": "tier-active",
    }.get(tier, "tier-beginner")


def tier_icon(tier):
    return {
        "Legendary Farmer": "👑",
        "Elite Farmer": "🏆",
        "Advanced Farmer": "🚀",
        "Active Farmer": "⚡",
    }.get(tier, "🌱")


def render_tier_badge(tier):
    st.markdown(
        f"""
        <span class="tier-badge {tier_class(tier)}">
            {tier_icon(tier)} Wallet Tier: {tier}
        </span>
        """,
        unsafe_allow_html=True
    )


def render_wallet_form():
    st.markdown(
        """
        <div class="hero">
            <h1>🚀 DropPilot AI</h1>
            <p>Analyze wallet readiness, prioritize airdrop opportunities, and generate an AI farming strategy.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    wallet_col, button_col = st.columns([4, 1])

    with wallet_col:
        wallet = st.text_input(
            "Wallet Address",
            placeholder="Enter an EVM wallet address"
        )

    with button_col:
        st.write("")
        st.write("")
        analyze_clicked = st.button(
            "Analyze",
            use_container_width=True
        )

    return wallet, analyze_clicked


def render_dashboard(result):
    col1, col2, col3 = st.columns(3)

    with col1:
        render_metric_card(
            "Wallet Score",
            result["wallet_score"]
        )

    with col2:
        render_metric_card(
            "Activity",
            result["activity_score"]
        )

    with col3:
        render_metric_card(
            "Tx Count",
            result["tx_count"]
        )

    st.write("")

    tier = result["wallet_tier"]

    render_tier_badge(tier)

    st.caption(
        f"Sybil Risk: {result['sybil_risk']}"
    )

    st.write("")

    st.subheader("📊 Farming Insights")

    if result["wallet_score"] >= 80:

        insights = [
            "✅ High Airdrop Potential",
            "✅ Low Sybil Risk",
            "✅ Strong Wallet Activity"
        ]

    elif result["wallet_score"] >= 60:

        insights = [
            "⚡ Moderate Airdrop Potential",
            "⚡ Needs More Activity"
        ]

    else:

        insights = [
            "⚠️ Increase Wallet Usage",
            "⚠️ Build More On-chain History"
        ]

    st.markdown(
        f"""
        <div class="insight-box">
            {"<br>".join(insights)}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

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


def render_recommendations(api_base_url):
    st.write("")

    st.subheader("🔥 Recommended Projects")

    try:

        recommendations = requests.get(
            f"{api_base_url}/recommend"
        ).json()

    except Exception as e:

        recommendations = []
        st.error(str(e))

    for project in recommendations:

        difficulty = project.get("difficulty", "Unknown")
        time_required = project.get("time_required", "Unknown")

        st.markdown(
            f"""
            <div class="project-card">
                <div class="project-name">✅ {project['name']}</div>
                <div class="project-meta">
                    Score: {project['score']} · Difficulty: {difficulty} · Time: {time_required}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
