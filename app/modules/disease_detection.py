import streamlit as st
import numpy as np
from PIL import Image
from disease_data import DISEASE_INFO, predict_disease


def show_disease_detection():
    st.title("🦠 Plant Disease Detection")
    st.write("Upload a clear image of a plant leaf.")

    uploaded_file = st.file_uploader(
        "Upload Leaf Image",
        type=["jpg", "jpeg", "png"],
        key="leaf_upload"
    )

    if uploaded_file is None:
        return

    try:
        image = Image.open(uploaded_file).convert("RGB")

        st.image(
            image,
            caption="Uploaded Leaf Image",
            width=350
        )

        rgb_array = np.asarray(image, dtype=np.float32)
        avg_rgb = np.mean(rgb_array, axis=(0, 1))

        st.subheader("RGB Colour Analysis")

        col1, col2, col3 = st.columns(3)
        col1.metric("Average Red", round(float(avg_rgb[0]), 2))
        col2.metric("Average Green", round(float(avg_rgb[1]), 2))
        col3.metric("Average Blue", round(float(avg_rgb[2]), 2))

        st.caption(
            "RGB values describe image colours; they do not confirm a disease."
        )

        if st.button("Analyze Leaf Image"):
            with st.spinner("Analyzing image..."):
                disease, confidence = predict_disease(image)

            if disease is None:
                st.warning(
                    "AI model is unavailable or could not analyze this image. "
                    "Check that a compatible trained model is installed."
                )
                return

            if confidence < 0.70:
                st.warning(
                    "The model prediction has low confidence. "
                    "Upload a clearer image or seek expert advice."
                )
                st.write(f"Model confidence: {confidence * 100:.1f}%")
                return

            info = DISEASE_INFO.get(disease)

            if info is None:
                st.warning("No disease information is configured for this class.")
                return

            st.success(f"Predicted Class: {info['name']}")
            st.write(f"Model confidence: {confidence * 100:.1f}%")

            st.subheader("Disease Symptoms")
            st.write(info["symptoms"])

            st.subheader("Treatment Recommendation")
            st.write(info["treatment"])

            st.subheader("Prevention")
            st.write(info["prevention"])

    except Exception:
        st.error("Unable to read this image. Please upload a valid JPG or PNG.")