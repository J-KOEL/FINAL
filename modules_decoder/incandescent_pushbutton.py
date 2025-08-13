# modules_decoder/incandescent_pushbutton.py
from pathlib import Path
import streamlit as st
from shared.utils import load_csv_dict

DATA_DIR = Path(__file__).resolve().parents[1] / "assets" / "data"

def norm(s: str) -> str:
    return str(s).strip().upper().replace("-", "").replace(" ", "").replace("_", "")

def normalize_keys(d: dict) -> dict:
    return {norm(k): v for k, v in d.items()}

@st.cache_data(show_spinner=False)
def load_data():
    # Use the EXACT filenames present in assets/data
    lu = load_csv_dict(DATA_DIR / "IlluminatedPushbuttonIncandescentLightUnit.csv")
    lc = load_csv_dict(DATA_DIR / "IlluminatedPushbuttonIncandescentLensColor.csv")
    ci = load_csv_dict(DATA_DIR / "Circuit 19.csv")  # or "Circuit.csv" if that's the real file
    # Normalize keys to match input normalization
    return normalize_keys(lu), normalize_keys(lc), normalize_keys(ci)

def decode(catalog_number, light_unit_lookup, lens_color_lookup, circuit_lookup):
    """
    Decodes: 10250T + LightUnit(3) + LensColor(3) + optional '-' + Circuit(...)
    """
    if not catalog_number:
        return None

    s = norm(catalog_number)

    # Minimal length: 6 prefix + 3 + 3 + 3 = 15
    if not (s.startswith("10250T") and len(s) >= 15):
        return None

    code_part = s[6:]
    light_unit_code = code_part[:3]
    lens_color_code = code_part[3:6]
    circuit_code    = code_part[6:]  # remaining chars (we removed '-' in norm)

    return {
        "Light Unit":        light_unit_lookup.get(light_unit_code, "Unknown Light Unit"),
        "Lens Color":        lens_color_lookup.get(lens_color_code, "Unknown Lens Color"),
        "Circuit Type":      circuit_lookup.get(circuit_code,   "Unknown Circuit Type"),
        "Light Unit P/N":    f"10250T{light_unit_code}",
        "Lens P/N":          f"10250T{lens_color_code}",
        "Contact Block P/N": f"10250T{circuit_code}",
    }
