import streamlit as st


def render_sidebar():
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
