import streamlit as st

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


# Sidebar navigation
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


# Display the selected module
if page == "Home":
    show_home()

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


# Footer
st.sidebar.markdown("---")
st.sidebar.caption(
    "Smart Agriculture System | Python + Streamlit"
)