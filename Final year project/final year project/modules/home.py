import streamlit as st


def show_home():
    st.title("🌱Plant Disease Analysis and Smart Farming Assistance ")

    st.subheader(
        "Smart Agriculture System"
    )

    st.write(
        "This project helps farmers explore plant disease information, "
        "fertilizer guidance, crop suggestions and farming questions."
    )

    st.info(
        "Automated disease prediction requires a compatible trained "
        "AI model. RGB colour analysis alone cannot diagnose disease."
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("Main Modules", "6")
    col2.metric("Interface", "Streamlit")
    col3.metric("Language", "Python")

    st.markdown("### Available Features")

    st.markdown("""
    - 🦠 Plant Disease Detection
    - 💊 Disease Treatment and Prevention
    - 💬 Farmer Chatbot
    - 🧪 Fertilizer Recommendation
    - 🌱 Crop Selection
    """)