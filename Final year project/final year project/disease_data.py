import streamlit as st
import numpy as np
from pathlib import Path

try:
    import tensorflow as tf
    TF_AVAILABLE = True
except ImportError:
    tf = None
    TF_AVAILABLE = False


DISEASE_INFO = {
    "Tomato___Early_blight": {
        "name": "Tomato Early Blight",
        "symptoms": "Older leaves may develop brown spots with concentric rings.",
        "treatment": "Remove severely affected leaves. Improve airflow and avoid watering directly onto foliage. Seek local agricultural advice before choosing a registered fungicide.",
        "prevention": "Rotate crops, maintain spacing and keep foliage as dry as practical."
    },
    "Tomato___Late_blight": {
        "name": "Tomato Late Blight",
        "symptoms": "Dark, water-soaked leaf patches may spread quickly in humid weather.",
        "treatment": "Obtain prompt agricultural advice because this disease can spread rapidly. Follow local plant protection recommendations.",
        "prevention": "Avoid prolonged leaf wetness and inspect plants regularly."
    },
    "Tomato___Leaf_Mold": {
        "name": "Tomato Leaf Mold",
        "symptoms": "Pale yellow patches may appear on upper leaf surfaces, with olive-coloured growth underneath.",
        "treatment": "Improve ventilation, avoid overhead watering and remove badly affected leaves.",
        "prevention": "Reduce excessive humidity and provide adequate plant spacing."
    },
    "Tomato___Septoria_leaf_spot": {
        "name": "Tomato Septoria Leaf Spot",
        "symptoms": "Small circular spots with pale centres and dark borders may appear.",
        "treatment": "Remove infected lower leaves, avoid splashing soil onto foliage and seek local advice.",
        "prevention": "Rotate crops, manage weeds and avoid working with wet plants."
    },
    "Tomato___healthy": {
        "name": "Tomato Healthy",
        "symptoms": "The model classifies the image as a healthy tomato leaf.",
        "treatment": "No disease-specific treatment is indicated by this prediction.",
        "prevention": "Continue regular monitoring and appropriate watering."
    },
    "Potato___Early_blight": {
        "name": "Potato Early Blight",
        "symptoms": "Brown leaf spots may develop concentric rings.",
        "treatment": "Remove affected foliage where appropriate and seek local advice.",
        "prevention": "Rotate crops and maintain good field hygiene."
    },
    "Potato___Late_blight": {
        "name": "Potato Late Blight",
        "symptoms": "Dark, spreading leaf lesions may develop in cool, wet weather.",
        "treatment": "Obtain prompt agricultural advice because this disease can spread rapidly.",
        "prevention": "Inspect crops frequently and avoid prolonged leaf wetness."
    },
    "Potato___healthy": {
        "name": "Potato Healthy",
        "symptoms": "The model classifies the image as a healthy potato leaf.",
        "treatment": "No disease-specific treatment is indicated by this prediction.",
        "prevention": "Continue routine crop monitoring."
    },
    "Pepper,_bell___Bacterial_spot": {
        "name": "Bell Pepper Bacterial Spot",
        "symptoms": "Small dark lesions may develop on leaves and fruit.",
        "treatment": "Avoid handling wet plants and consult a local agricultural expert.",
        "prevention": "Use healthy planting material and reduce leaf wetness."
    },
    "Pepper,_bell___healthy": {
        "name": "Bell Pepper Healthy",
        "symptoms": "The model classifies the image as a healthy bell pepper leaf.",
        "treatment": "No disease-specific treatment is indicated by this prediction.",
        "prevention": "Maintain suitable watering and inspect plants regularly."
    }
}


MODEL_CLASSES = [
    "Pepper,_bell___Bacterial_spot",
    "Pepper,_bell___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold",
    "Tomato___Septoria_leaf_spot",
    "Tomato___healthy"
]


MODEL_PATH = Path(__file__).resolve().parent / "plant_disease_model.keras"


@st.cache_resource
def load_model():
    if not TF_AVAILABLE or not MODEL_PATH.exists():
        return None

    try:
        return tf.keras.models.load_model(MODEL_PATH)
    except Exception:
        return None


def predict_disease(image):
    model = load_model()

    if model is None:
        return None, None

    try:
        resized = image.convert("RGB").resize((224, 224))
        array = np.asarray(resized, dtype=np.float32)
        array = np.expand_dims(array, axis=0)
        array = array / 255.0

        prediction = model.predict(array, verbose=0)[0]

        if len(prediction) != len(MODEL_CLASSES):
            return None, None

        index = int(np.argmax(prediction))
        confidence = float(prediction[index])

        return MODEL_CLASSES[index], confidence

    except Exception:
        return None, None