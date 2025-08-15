# modules_decoder/incandescent_pushbutton.py
from shared.utils import load_csv_dict

DATA_DIR = "assets/data/"  # relative to your repo root

def load_data():
    """
    Loads lookup dictionaries for Incandescent Pushbutton:
    10250T + LightUnit(3) + LensColor(3) + '-' + Circuit(...)
    """
    # Note: load_csv_dict automatically maps Code -> Label when those columns exist.
    light_unit_lookup = load_csv_dict(DATA_DIR + "IlluminatedPushbuttonIncandescentLightUnit.csv")
    lens_color_lookup = load_csv_dict(DATA_DIR + "illuminatedPushbuttonIncandescentLensColor.csv")
    circuit_lookup = load_csv_dict(DATA_DIR + "Circuit.csv")
    return light_unit_lookup, lens_color_lookup, circuit_lookup


def decode(catalog_number, light_unit_lookup, lens_color_lookup, circuit_lookup):
    """
    Decodes a catalog number like: 10250TxxxYYY-ZZZ...
    Where:
      - xxx = Light Unit code (3)
      - YYY = Lens Color code (3)
      - ZZZ... = Circuit code (remaining after optional dash)
    Returns a dict of human-friendly fields or None if it cannot decode.
    """
    if not catalog_number:
        return None

    normalized = str(catalog_number).replace("-", "").strip().upper()

    # Basic format guard
    if not (normalized.startswith("10250T") and len(normalized) > 9):
        return None

    # Strip the 10250T prefix and parse the rest
    code_part = normalized[6:]
    if len(code_part) < 9:
        # We expect at least 3 + 3 + 3 characters
        return None

    light_unit_code = code_part[:3]
    lens_color_code = code_part[3:6]
    circuit_code    = code_part[6:]  # whatever remains

    return {
        "Light Unit":        light_unit_lookup.get(light_unit_code, "Unknown Light Unit"),
        "Lens Color":        lens_color_lookup.get(lens_color_code, "Unknown Lens Color"),
        "Circuit Type":      circuit_lookup.get(circuit_code,   "Unknown Circuit Type"),
        "Light Unit P/N":    f"10250T{light_unit_code}",
        "Lens P/N":          f"10250T{lens_color_code}",
        "Contact Block P/N": f"10250T{circuit_code}",
    }
