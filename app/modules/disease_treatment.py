import streamlit as st
from disease_data import DISEASE_INFO


def show_disease_treatment():
    st.title("💊 Disease Treatment and Prevention")

    st.write(
        "Select a supported disease to view general management information."
    )

    disease_options = {
        info["name"]: key
        for key, info in DISEASE_INFO.items()
    }

    selected_name = st.selectbox(
        "Select Disease",
        list(disease_options.keys())
    )

    info = DISEASE_INFO[disease_options[selected_name]]

    st.subheader("Disease Name")
    st.write(info["name"])

    st.subheader("Symptoms")
    st.write(info["symptoms"])

    st.subheader("Treatment")
    st.write(info["treatment"])

    st.subheader("Prevention")
    st.write(info["prevention"])

    st.warning(
        "These are general educational suggestions. Confirm the diagnosis "
        "with a qualified agricultural expert before treating crops."
    )