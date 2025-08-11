import streamlit as st
import importlib

st.title("🔍 10250T Catalog Number Decoder")

# Try to import modules; if not present, skip that product type gracefully
def safe_import(module_path):
    try:
        return importlib.import_module(module_path)
    except Exception:
        return None

modules = {
    "Non-Illuminated Pushbutton": safe_import("modules_decoder.non_illuminated"),
    "LED Pushbutton": safe_import("modules_decoder.led_pushbutton"),
    "Incandescent Pushbutton": safe_import("modules_decoder.incandescent_pushbutton"),
    "Incandescent Push-Pull": safe_import("modules_decoder.incandescent_pushpull"),
    "Non-Illuminated Push-Pull": safe_import("modules_decoder.non_illuminated_pushpull"),
    "LED Push-Pull": safe_import("modules_decoder.led_pushpull"),
    "Standard Indicating Light Incandescent": safe_import("modules_decoder.standard_indicating_incandescent"),
    "Standard Indicating Light LED": safe_import("modules_decoder.standard_indicating_led"),
    "PresTest Incandescent": safe_import("modules_decoder.presttest_incandescent"),
    "PresTest LED": safe_import("modules_decoder.presttest_led"),
    "Master Test Incandescent": safe_import("modules_decoder.mastertest_incandescent"),
}

available_product_types = [name for name, mod in modules.items() if mod is not None]

if not available_product_types:
    st.info(
        "No decoder modules found yet. "
        "Copy your existing product decoder files into `modules_decoder/` and reload."
    )

product_type = st.selectbox("Select product type:", available_product_types)

catalog_input = st.text_input("Enter a 10250T catalog number:")

if catalog_input and product_type:
    mod = modules[product_type]

    try:
        # Every module is expected to provide load_data() and decode()
        result = None
        if product_type == "Non-Illuminated Pushbutton":
            operator_lookup, color_lookup, circuit_lookup, alt_map = mod.load_data()
            result = mod.decode(catalog_input, operator_lookup, color_lookup, circuit_lookup, alt_map)
        elif product_type == "LED Pushbutton":
            light_unit_lookup, lens_color_lookup, voltage_lookup, circuit_lookup = mod.load_data()
            result = mod.decode(catalog_input, light_unit_lookup, lens_color_lookup, voltage_lookup, circuit_lookup)
        elif product_type == "Incandescent Pushbutton":
            light_unit_lookup, lens_color_lookup, circuit_lookup = mod.load_data()
            result = mod.decode(catalog_input, light_unit_lookup, lens_color_lookup, circuit_lookup)
        elif product_type == "Incandescent Push-Pull":
            operator_lookup, light_unit_lookup, lens_lookup, circuit_lookup = mod.load_data()
            result = mod.decode(catalog_input, operator_lookup, light_unit_lookup, lens_lookup, circuit_lookup)
        elif product_type == "Non-Illuminated Push-Pull":
            operator_lookup, button_lookup, circuit_lookup = mod.load_data()
            result = mod.decode(catalog_input, operator_lookup, button_lookup, circuit_lookup)
        elif product_type == "LED Push-Pull":
            operator_lookup, light_unit_lookup, lens_lookup, circuit_lookup, voltage_lookup = mod.load_data()
            result = mod.decode(catalog_input, operator_lookup, light_unit_lookup, lens_lookup, circuit_lookup, voltage_lookup)
        elif product_type == "Standard Indicating Light Incandescent":
            light_unit_lookup, lens_lookup = mod.load_data()
            result = mod.decode(catalog_input, light_unit_lookup, lens_lookup)
        elif product_type == "Standard Indicating Light LED":
            light_unit_lookup, lens_lookup, voltage_lookup = mod.load_data()
            result = mod.decode(catalog_input, light_unit_lookup, lens_lookup, voltage_lookup)
        elif product_type == "PresTest Incandescent":
            light_unit_lookup, lens_lookup = mod.load_data()
            result = mod.decode(catalog_input, light_unit_lookup, lens_lookup)
        elif product_type == "PresTest LED":
            light_unit_lookup, lens_lookup, voltage_lookup = mod.load_data()
            result = mod.decode(catalog_input, light_unit_lookup, lens_lookup, voltage_lookup)
        elif product_type == "Master Test Incandescent":
            light_unit_lookup, lens_lookup = mod.load_data()
            result = mod.decode(catalog_input, light_unit_lookup, lens_lookup)
        else:
            result = None

        if result:
            st.markdown("### ✅ Decoded Result")
            for key, value in result.items():
                st.write(f"**{key}**: {value}")
        else:
            st.error("Catalog number could not be decoded. Please check the format.")

    except AttributeError:
        st.error(f"`{product_type}` module is missing required functions (`load_data`, `decode`).")
    except Exception as e:
        st.exception(e)

