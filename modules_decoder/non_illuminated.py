# modules_decoder/non_illuminated.py
from shared.utils import load_csv_dict, load_alternate_map

DATA_DIR = "assets/data/"  # Base directory for CSV files

def load_data():
    """
    Loads lookup dictionaries for Non-Illuminated Pushbutton:
    10250T + Operator(2) + Color(1) + Circuit(rest)
    Includes alternate catalog number mapping.
    """
    operator_lookup = load_csv_dict(DATA_DIR + "NonIlluminatedPushbuttonOperator.csv")
    color_lookup    = load_csv_dict(DATA_DIR + "NonIlluminatedPushbuttonButtonColor.csv")
    circuit_lookup  = load_csv_dict(DATA_DIR + "Circuit.csv")
    alt_map         = load_alternate_map(DATA_DIR + "AlternateCatalogNumbers.csv")
    return operator_lookup, color_lookup, circuit_lookup, alt_map


def decode(catalog_number, operator_lookup, color_lookup, circuit_lookup, alt_map):
    """
    Decodes a catalog number like: 10250T + Operator(2) + Color(1) + Circuit(rest)
    Handles alternate catalog numbers via alt_map.
    """
    if not catalog_number:
        return None

    # Normalize and map alternate codes
    normalized = str(catalog_number).replace("-", "").strip().upper()
    normalized = alt_map.get(normalized, normalized)

    if not (normalized.startswith("10250T") and len(normalized) > 7):
        return None

    code_part = normalized[6:]
    if len(code_part) < 4:  # Need at least 2 + 1 + 1
        return None

    operator_code = code_part[:2]
    color_code    = code_part[2]
    circuit_code  = code_part[5:]

    return {
        "Operator Type":      operator_lookup.get(operator_code, "Unknown Operator Code"),
        "Button Color":       color_lookup.get(color_code, "Unknown Color Code"),
        "Circuit Type":       circuit_lookup.get(circuit_code, "Unknown Circuit Code"),
        "Operator P/N":       f"10250T{operator_code}{color_code}",
        "Contact Block P/N":  f"10250T{circuit_code}",
    }
