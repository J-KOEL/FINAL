# modules_decoder/incandescent_pushbutton.py
import re
from shared.utils import load_csv_dict

DATA_DIR = "assets/data/"  # keep as-is if this path works in your app

def _norm(s: str) -> str:
    # Keep only A–Z and 0–9; removes spaces, hyphens, en-dashes, slashes, etc.
    return re.sub(r'[^A-Z0-9]', '', str(s).upper())

def load_data():
    """
    Loads lookup dictionaries for Incandescent Pushbutton:
    10250T + LightUnit(3) + LensColor(3) + '-' + Circuit(...)
    """
    light_unit_lookup = load_csv_dict(
        DATA_DIR + "IlluminatedPushbuttonIncandescentLightUnit.csv"
    )
    lens_color_lookup = load_csv_dict(
        DATA_DIR + "IlluminatedPushbuttonIncandescentLensColor.csv"
    )
    circuit_lookup = load_csv_dict(
        DATA_DIR + "Circuit.csv"  # keep whatever filename you actually use
    )
    return light_unit_lookup, lens_color_lookup, circuit_lookup


def decode(catalog_number, light_unit_lookup, lens_color_lookup, circuit_lookup):
    """
    Decodes: 10250T + LightUnit(3) + LensColor(3) + Circuit(>=1)
    Returns a dict on success, or None if the *format* is invalid.
    """
    if not catalog_number:
        return None

    s = _norm(catalog_number)

    # Minimal length: 6 (prefix) + 3 + 3 + 1 (min circuit) = 13
    if not (s.startswith("10250T") and len(s) >= 13):
        return None

    code_part = s[6:]
    if len(code_part) < 7:  # 3 + 3 + at least 1 for circuit
        return None

    light_unit_code = code_part[:3]
    lens_color_code = code_part[3:6]
    circuit_code    = code_part[6:]  # remaining chars

    return {
        "Light Unit":        light_unit_lookup.get(light_unit_code, "Unknown Light Unit"),
        "Lens Color":        lens_color_lookup.get(lens_color_code, "Unknown Lens Color"),
        "Circuit Type":      circuit_lookup.get(circuit_code,   "Unknown Circuit Type"),
        "Light Unit P/N":    f"10250T{light_unit_code}",
        "Lens P/N":          f"10250T{lens_color_code}",
        "Contact Block P/N": f"10250T{circuit_code}",
    }
