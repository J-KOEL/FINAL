# modules_decoder/incandescent_pushpull.py
from shared.utils import load_csv_dict

DATA_DIR = "assets/data/"  # Base directory for CSV files

def load_data():
    """
    Loads lookup dictionaries for Incandescent Push-Pull:
    10250T + Operator + LightUnit + Lens + Circuit
    """
    operator_lookup = load_csv_dict(DATA_DIR + "PushPullOperator.csv")
    light_unit_lookup = load_csv_dict(DATA_DIR + "IlluminatedPushPullIncandescentLightUnit.csv")
    lens_lookup = load_csv_dict(DATA_DIR + "IlluminatedPushPullIncandescentLens.csv")
    circuit_lookup = load_csv_dict(DATA_DIR + "Circuit.csv")
    return operator_lookup, light_unit_lookup, lens_lookup, circuit_lookup


def decode(catalog_number, operator_lookup, light_unit_lookup, lens_lookup, circuit_lookup):
    """
    Decodes a catalog number like: 10250T + Operator + LightUnit + Lens + Circuit
    Handles two patterns:
      - If code starts with '1': Operator(2) + LightUnit(2) + Lens(3) + Circuit(rest)
      - Else: Operator(1) + LightUnit(2) + Lens(3) + Circuit(rest)
    """
    if not catalog_number:
        return None

    normalized = str(catalog_number).replace("-", "").strip().upper()

    # Basic format guard
    if not (normalized.startswith("10250T") and len(normalized) > 11):
        return None

    code_part = normalized[6:]

    # Parse based on first digit
    if code_part.startswith("1"):
        operator_code = code_part[:2]
        light_unit_code = code_part[2:4]
        lens_code = code_part[4:7]
        circuit_code = code_part[7:]
    else:
        operator_code = code_part[:1]
        light_unit_code = code_part[1:3]
        lens_code = code_part[3:6]
        circuit_code = code_part[6:]

    return {
        "Operator Type": operator_lookup.get(operator_code, "Unknown Operator Code"),
        "Light Unit": light_unit_lookup.get(light_unit_code, "Unknown Light Unit"),
        "Lens": lens_lookup.get(lens_code, "Unknown Lens Code"),
        "Circuit Type": circuit_lookup.get(circuit_code, "Unknown Circuit Code"),
        "Operator P/N": f"10250T{operator_code}",
        "Light Unit P/N": f"10250T{light_unit_code}",
        "Lens P/N": f"10250T{lens_code}",
        "Contact Block P/N": f"10250T{circuit_code}",
    }
