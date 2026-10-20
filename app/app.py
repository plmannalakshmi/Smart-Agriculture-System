import streamlit as st
from pathlib import Path

from modules.home import show_home
from modules.disease_detection import show_disease_detection
from modules.disease_treatment import show_disease_treatment
from modules.farmer_chatbot import show_farmer_chatbot
from modules.fertilizer import show_fertilizer
from modules.crop_selection import show_crop_selection



# Page configuration
st.set_page_config(
    page_title="Smart Agriculture System",
    page_icon="🌱",
    layout="wide"
)



st.markdown("""
<style>
.stApp {
    background-color: #F1F8EE;
}
h1, h2, h3 {
    color: #205C35 !important;
}
section[data-testid="stSidebar"] {
    background-color: #E0EEDB;
}
.stButton > button {
    background-color: #2E7D32;
    color: white;
    border-radius: 10px;
    border: none;
}
#MainMenu, footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("🌱 Smart Agriculture")

page = st.sidebar.radio(
    "Select Module",
    [
        "Home",
        "Plant Disease Detection",
        "Disease Treatment",
        "Farmer Chatbot",
        "Fertilizer Recommendation",
        "Crop Selection"
    ]
)

if page == "Home":
    st.title("🌱 Smart Agriculture")
    st.subheader("Plant Health Monitoring System")
    st.markdown("### Welcome, Farmer! 🌿")
    st.write(
        "Monitor plant health and discover suitable disease treatments."
    )

    image_path = Path(__file__).parent / "agriculture.png.png"
    st.image(str(image_path), use_container_width=True)

    st.info(
        "Choose Plant Disease Detection from the sidebar "
        "to check a leaf image."
    )
    st.caption("Smart farming • Healthy crops • Better growth")

elif page == "Plant Disease Detection":
    show_disease_detection()

elif page == "Disease Treatment":
    show_disease_treatment()

elif page == "Farmer Chatbot":
    show_farmer_chatbot()

elif page == "Fertilizer Recommendation":
    show_fertilizer()

elif page == "Crop Selection":
    show_crop_selection()





