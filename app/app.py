
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
st.image("agriculture.png.png", use_container_width=True)

# Modern green agriculture design
st.markdown("""
<style>
/* Main background and readable text */
.stApp {
    background-color: #f5faf4;
    color: #24352a;
}

/* Page spacing */
.block-container {
    max-width: 1200px;
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

/* Headings */
h1, h2, h3, h4, h5, h6 {
    color: #1b5e20 !important;
}

/* Normal text */
.stApp p,
.stApp label,
.stApp li {
    color: #24352a;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #e5f2e3;
}

[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label {
    color: #1b5e20 !important;
}

/* Buttons */
.stButton > button,
.stDownloadButton > button {
    background-color: #2e7d32;
    color: white !important;
    border: none;
    border-radius: 10px;
    padding: 0.55rem 1rem;
}

.stButton > button:hover,
.stDownloadButton > button:hover {
    background-color: #1b5e20;
    color: white !important;
}

/* Input fields */
.stTextInput input,
.stNumberInput input,
.stTextArea textarea {
    background-color: white;
    color: #24352a !important;
    border: 1px solid #b7cdb6;
    border-radius: 8px;
}

/* Hide menu and footer */
#MainMenu,
footer {
    visibility: hidden;
}

/* Mobile layout */
@media (max-width: 768px) {
    .block-container {
        padding: 1rem 0.8rem;
    }

    h1 {
        font-size: 1.7rem;
    }

    h2 {
        font-size: 1.4rem;
    }
}
</style>
""", unsafe_allow_html=True)


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


# Sidebar footer
st.sidebar.markdown("---")
st.sidebar.caption("Smart Agriculture System | Python + Streamlit")
