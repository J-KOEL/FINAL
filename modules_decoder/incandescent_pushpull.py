# modules_decoder/incandescent_pushbutton.py
from shared.utils import load_csv_dict

DATA_DIR = "assets/data/"  # Base directory for CSV files

def load_data():
    """
    Loads lookup dictionaries for Incandescent Pushbutton:
    10250T + LightUnit + LensColor + Circuit
    """
    light_unit_lookup = load_csv_dict(DATA_DIR + "IlluminatedPushbuttonIncandescentLightUnit.csv")
    lens_color_lookup = load_csv_dict(DATA_DIR + "illuminatedPushbuttonIncandescentLensColor.csv")
    circuit_lookup    = load_csv_dict(DATA_DIR + "Circuit.csv")
    return light_unit_lookup, lens_color_lookup, circuit_lookup


def decode(catalog_number, light_unit_lookup, lens_color_lookup, circuit_lookup):
    """
    Decodes a catalog number like: 10250T + LightUnit(3) + LensColor(3) + Circuit(rest)
    Notes:
      - Normalizes by removing '-' and uppercasing (same as incandescent_pushpull.py)
      - Returns None only if the basic format/length check fails
    """
    if not catalog_number:
        return None

    # Match normalization style used in incandescent_pushpull.py
    normalized = str(catalog_number).replace("-", "").strip().upper()

    # Basic format guard (kept consistent with incandescent_pushpull.py style)
    if not (normalized.startswith("10250T") and len(normalized) > 11):
        return None

    code_part = normalized[6:]  # strip '10250T'

    # Fixed-width parsing for this family:
    # LightUnit = 3, LensColor = 3, Circuit = remaining
    if len(code_part) < 7:  # require at least 3 + 3 + 1 for circuit
        return None

    light_unit_code = code_part[:3]
    lens_color_code = code_part[3:6]
    circuit_code    = code_part[6:]  # remainder

    return {
        "Light Unit":        light_unit_lookup.get(light_unit_code, "Unknown Light Unit"),
        "Lens Color":        lens_color_lookup.get(lens_color_code, "Unknown Lens Color"),
        "Circuit Type":      circuit_lookup.get(circuit_code,   "Unknown Circuit Code"),
        "Light Unit P/N":    f"10250T{light_unit_code}",
        "Lens P/N":          f"10250T{lens_color_code}",
        "Contact Block P/N": f"10250T{circuit_code}",
    }

