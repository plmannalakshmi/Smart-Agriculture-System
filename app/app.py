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

# Custom app appearance
st.markdown("""
<style>
/* Hide Streamlit menu and footer */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* Hide the top decoration and toolbar */
[data-testid="stDecoration"] {
    display: none;
}

[data-testid="stToolbar"] {
    visibility: hidden;
}

/* Reduce extra space at the top */
.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
    max-width: 1200px;
}

/* Light green background */
.stApp {
    background-color: #f5fbf4;
}

/* Dark green headings */
h1, h2, h3 {
    color: #246b3b;
}

/* Sidebar appearance */
[data-testid="stSidebar"] {
    background-color: #e8f4e5;
}

/* Buttons */
.stButton > button {
    background-color: #246b3b;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 0.5rem 1rem;
}

/* Button hover effect */
.stButton > button:hover {
    background-color: #19532c;
    color: white;
    border: 1px solid #19532c;
}

/* Input fields */
.stTextInput input,
.stTextArea textarea,
.stSelectbox div[data-baseweb="select"] {
    border-radius: 8px;
}

/* Make the layout more phone-friendly */
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


# Footer
st.sidebar.markdown("---")
st.sidebar.caption(
    "Smart Agriculture System | Python + Streamlit"
)
