import streamlit as st


def show_farmer_chatbot():
    st.title("💬 Farmer Chatbot")

    st.write(
        "Ask a question about plant health, fertilizer, water or crop selection."
    )

    question = st.text_input(
        "Enter your question",
        placeholder="Why are my plant leaves turning yellow?",
        key="farmer_question"
    )

    if st.button("Ask Question"):
        q = question.lower().strip()

        if not q:
            st.warning("Please enter a question.")

        elif any(word in q for word in [
            "hello", "hi", "vanakkam", "வணக்கம்"
        ]):
            st.success(
                "Hello! I can help with general plant care, fertilizer "
                "and crop questions."
            )

        elif any(word in q for word in [
            "yellow", "yellowing", "manjal", "மஞ்சள்"
        ]):
            st.info(
                "Yellow leaves may be related to watering problems, nutrient "
                "deficiency, pests or disease. Check soil moisture and inspect "
                "the leaves before choosing a treatment."
            )

        elif any(word in q for word in [
            "disease", "spot", "fungus", "leaf", "நோய்"
        ]):
            st.info(
                "Check the spots, leaf colour and affected plant parts. "
                "Upload a clear image in Plant Disease Detection. A trained "
                "AI model is required for automated disease prediction."
            )

        elif any(word in q for word in [
            "fertilizer", "fertiliser", "npk", "uram", "உரம்"
        ]):
            st.info(
                "NPK stands for Nitrogen, Phosphorus and Potassium. "
                "Use soil-test results and crop requirements to select "
                "an appropriate fertilizer."
            )

        elif any(word in q for word in [
            "water", "watering", "thanni", "தண்ணீர்"
        ]):
            st.info(
                "Water requirements depend on the crop, soil and weather. "
                "Check soil moisture and avoid waterlogging or overwatering."
            )

        elif any(word in q for word in [
            "crop", "climate", "weather", "payir", "பயிர்"
        ]):
            st.info(
                "Open Crop Selection and choose a climate category "
                "to explore example crops."
            )

        elif any(word in q for word in [
            "nitrogen", "phosphorus", "potassium"
        ]):
            st.info(
                "Nitrogen supports leaf growth, phosphorus contributes to "
                "root development and energy transfer, and potassium helps "
                "regulate plant processes. Actual fertilizer needs vary by crop and soil."
            )

        else:
            st.info(
                "I could not find a matching answer. Ask about plant disease, "
                "yellow leaves, watering, fertilizer or crops."
            )