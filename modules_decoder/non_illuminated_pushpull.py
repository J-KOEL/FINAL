# modules_decoder/non_illuminated_pushpull.py
from shared.utils import load_csv_dict

DATA_DIR = "assets/data/"  # Base directory for CSV files

def load_data():
    """
    Loads lookup dictionaries for Non-Illuminated Push-Pull:
    10250T + Operator + Button + Circuit
    """
    operator_lookup = load_csv_dict(DATA_DIR + "PushPullOperator.csv")
    button_lookup   = load_csv_dict(DATA_DIR + "NonIlluminatedPushPullButton.csv")
    circuit_lookup  = load_csv_dict(DATA_DIR + "Circuit.csv")
    return operator_lookup, button_lookup, circuit_lookup


def decode(catalog_number, operator_lookup, button_lookup, circuit_lookup):
    """
    Decodes a catalog number like:
    10250T + Operator + Button + Circuit
    Handles two patterns:
      - If code starts with '1': Operator(2) + Button(3) + Circuit(2)
      - Else: Operator(1) + Button(3) + Circuit(2)
    """
    if not catalog_number:
        return None

    normalized = str(catalog_number).replace("-", "").strip().upper()

    # Basic format guard
    if not (normalized.startswith("10250T") and len(normalized) > 9):
        return None

    code_part = normalized[6:]

    # Parse based on first digit
    if code_part.startswith("1"):
        operator_code = code_part[:2]
        button_code   = code_part[2:5]
        circuit_code  = code_part[5:7]
    else:
        operator_code = code_part[:1]
        button_code   = code_part[1:4]
        circuit_code  = code_part[4:6]

    return {
        "Operator":          operator_lookup.get(operator_code, "Unknown Operator"),
        "Button":            button_lookup.get(button_code, "Unknown Button"),
        "Circuit":           circuit_lookup.get(circuit_code, "Unknown Circuit"),
        "Operator P/N":      f"10250T{operator_code}",
        "Button P/N":        f"10250T{button_code}",
        "Contact Block P/N": f"10250T{circuit_code}",
    }
