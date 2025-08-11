import streamlit as st

def render_dropdown(label, options_dict):
    """Renders a selectbox returning the chosen *label* key."""
    return st.selectbox(label, list(options_dict.keys()))

def render_product_selector():
    """Fixed version of your original list with missing commas + consistent labels."""
    return st.selectbox(
        "Select Product Type",
        [
            "Non-Illuminated Pushbuttons",
            "Non-Illuminated Pushpulls",
            "Illuminated Incandescent Pushpulls",
            "Illuminated LED Pushpulls",
            "Illuminated Incandescent Pushbuttons",
            "Illuminated LED Pushbuttons",
            "Standard Indicating Lights - Incandescent",
            "Standard Indicating Lights - LED",
            "PresTest Incandescent",
            "PresTest LED",
            "Master Test Incandescent",
        ],
    )

