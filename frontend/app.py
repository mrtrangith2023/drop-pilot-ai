import streamlit as st

st.title("🚀 DropPilot AI")

wallet = st.text_input(
    "Enter Wallet Address"
)

if st.button("Analyze"):
    st.success(
        f"Analyzing {wallet}"
    )