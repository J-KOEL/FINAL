import streamlit as st
from shared.data_loader import load_mapping
from modules_configurator.logic import build_catalog_number
from modules_configurator.product_configs import product_configs

st.title("🛠 10250T Catalog Number Configurator")

product_type = st.selectbox("Select Product Type", list(product_configs.keys()))

if product_type:
    config = product_configs[product_type]
    selections = {}

    for field in config["fields"]:
        mapping = load_mapping(f"assets/data/{config['files'][field]}")
        choice = st.selectbox(f"Select {field}", list(mapping.keys()))
        selections[field] = mapping[choice]

    if st.button("Generate Catalog Number"):
        catalog_number = build_catalog_number(product_type, selections)
        st.success(f"Catalog Number: {catalog_number}")

