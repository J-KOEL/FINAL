# modules_decoder/mastertest_incandescent.py
from shared.utils import load_csv_dict

DATA_DIR = "assets/data/"  # Base directory for CSV files

def load_data():
    """
    Loads lookup dictionaries for Master Test Incandescent:
    10250T + LightUnit(4) + Lens(rest)
    """
    light_unit_lookup = load_csv_dict(DATA_DIR + "MasterTestIncandescentLightUnit.csv")
    lens_lookup       = load_csv_dict(DATA_DIR + "MasterTestIncandescentLens.csv")
    return light_unit_lookup, lens_lookup


def decode(catalog_number, light_unit_lookup, lens_lookup):
    """
    Decodes a catalog number like: 10250TLLLLXXXX
    Where:
      - LLLL = Light Unit code (4)
      - XXXX = Lens code (remaining)
    Returns a dict of human-friendly fields or None if it cannot decode.
    """
    if not catalog_number:
        return None

    normalized = str(catalog_number).replace("-", "").strip().upper()

    # Basic format guard
    if not (normalized.startswith("10250T") and len(normalized) > 9):
        return None

    code_part = normalized[6:]
    if len(code_part) < 5:  # need at least 4 for light unit + 1 for lens
        return None

    light_unit_code = code_part[:4]
    lens_code       = code_part[4:]

    return {
        "Light Unit":     light_unit_lookup.get(light_unit_code, "Unknown Light Unit"),
        "Lens Color":     lens_lookup.get(lens_code, "Unknown Lens Color"),
        "Light Unit P/N": f"10250T{light_unit_code}",
        "Lens P/N":       f"10250T{lens_code}",
    }
