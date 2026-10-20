import streamlit as st


def show_fertilizer():
    st.title("🧪 Fertilizer Recommendation")

    st.write("Enter NPK values from your soil test.")

    nitrogen = st.number_input(
        "Nitrogen (N)",
        min_value=0.0,
        max_value=1000.0,
        value=20.0,
        key="nitrogen"
    )

    phosphorus = st.number_input(
        "Phosphorus (P)",
        min_value=0.0,
        max_value=1000.0,
        value=15.0,
        key="phosphorus"
    )

    potassium = st.number_input(
        "Potassium (K)",
        min_value=0.0,
        max_value=1000.0,
        value=10.0,
        key="potassium"
    )

    if st.button("Get Recommendation"):
        st.subheader("Entered Values")

        st.write(f"Nitrogen: {nitrogen}")
        st.write(f"Phosphorus: {phosphorus}")
        st.write(f"Potassium: {potassium}")

        st.subheader("Educational Guidance")

        st.write(
            "These values alone cannot determine the correct fertilizer dose. "
            "Interpret them using the soil-test report, crop, soil type and "
            "local agricultural recommendations."
        )

        st.info(
            "Consult your local agricultural department for an actual "
            "fertilizer recommendation based on your soil and crop."
        )