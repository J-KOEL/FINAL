# modules_decoder/non_illuminated.py
from shared.utils import load_csv_dict, load_alternate_map

DATA_DIR = "assets/data/"

def load_data():
    operator_lookup = load_csv_dict(DATA_DIR + "NonIlluminatedPushbuttonOperator.csv")
    color_lookup    = load_csv_dict(DATA_DIR + "NonIlluminatedPushbuttonButtonColor.csv")
    circuit_lookup  = load_csv_dict(DATA_DIR + "Circuit.csv")
    alt_map         = load_alternate_map(DATA_DIR + "AlternateToStandard.csv")  # <-- if you have one
    return operator_lookup, color_lookup, circuit_lookup, alt_map

def decode(catalog_number, operator_lookup, color_lookup, circuit_lookup, alt_map):
    normalized = str(catalog_number).replace("-", "").strip().upper()

    # Translate alternate to standard if present
    normalized = alt_map.get(normalized, normalized)

    if not (normalized.startswith("10250T") and len(normalized) > 8):
        return None

    code_part = normalized[6:]
    # Example: 10250T + Operator(2) + Color(1) + '-' + Circuit
    if len(code_part) < 3:
        return None

    operator_code = code_part[:2]
    color_code    = code_part[2:3]
    circuit_code  = code_part[3:]

    return {
        "Operator":          operator_lookup.get(operator_code, "Unknown Operator"),
        "Button Color":      color_lookup.get(color_code, "Unknown Button Color"),
        "Circuit Type":      circuit_lookup.get(circuit_code, "Unknown Circuit Type"),
        "Operator P/N":      f"10250T{operator_code}",
        "Color P/N":         f"10250T{color_code}",
        "Contact Block P/N": f"10250T{circuit_code}",
    }
