import requests
import streamlit as st


def render_strategy(api_base_url):
    if (
        "result" in st.session_state
        and st.button("🧠 Generate AI Strategy")
    ):

        result = st.session_state["result"]

        with st.spinner(
            "DropPilot AI is analyzing your wallet..."
        ):

            response = requests.post(
                f"{api_base_url}/strategy",
                json=result
            )

            if response.status_code == 200:

                st.session_state["strategy"] = response.json()

            else:

                st.error(
                    response.text
                )

    if "strategy" in st.session_state:

        st.write("")

        st.subheader("🧠 AI Strategy Report")

        st.markdown(
            '<div class="report-box">',
            unsafe_allow_html=True
        )

        st.markdown(
            st.session_state["strategy"]["strategy"]
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )
