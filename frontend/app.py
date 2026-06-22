import requests
import streamlit as st

from components.dashboard import (
    render_dashboard,
    render_page_styles,
    render_recommendations,
    render_wallet_form,
)
from components.sidebar import render_sidebar
from components.strategy import render_strategy


API_BASE_URL = "http://127.0.0.1:8000"


st.set_page_config(
    page_title="DropPilot AI",
    page_icon="🚀",
    layout="wide"
)

render_page_styles()
render_sidebar()

wallet, analyze_clicked = render_wallet_form()

if analyze_clicked:

    try:

        with st.spinner("Analyzing wallet activity..."):

            response = requests.post(
                f"{API_BASE_URL}/analyze",
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

if "result" in st.session_state:

    render_dashboard(st.session_state["result"])

render_recommendations(API_BASE_URL)
render_strategy(API_BASE_URL)
