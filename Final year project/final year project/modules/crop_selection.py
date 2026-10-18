import streamlit as st


def show_crop_selection():
    st.title("🌱 Crop Selection")

    st.write("Choose a climate category to see example crops.")

    climate = st.selectbox(
        "Select Climate",
        [
            "Hot and Dry",
            "Hot and Humid",
            "Moderate",
            "Cool"
        ]
    )

    crops = {
        "Hot and Dry": [
            "Pearl Millet",
            "Sorghum",
            "Cowpea"
        ],
        "Hot and Humid": [
            "Rice",
            "Sugarcane",
            "Banana"
        ],
        "Moderate": [
            "Maize",
            "Groundnut",
            "Pulses"
        ],
        "Cool": [
            "Peas",
            "Cabbage",
            "Carrot"
        ]
    }

    st.subheader("Example Crops")

    for crop in crops[climate]:
        st.write(f"🌾 {crop}")

    st.caption(
        "These are general examples, not location-specific recommendations. "
        "Choose crops based on local rainfall, soil, season and irrigation."
    )