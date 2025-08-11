# modules_decoder/led_pushpull.py
from shared.utils import load_csv_dict

DATA_DIR = "assets/data/"  # Base directory for CSV files

def load_data():
    """
    Loads lookup dictionaries for LED Push-Pull:
    10250T + Operator + LightUnit + Lens + Voltage + Circuit
    """
    operator_lookup   = load_csv_dict(DATA_DIR + "PushPullOperator.csv", value_col="Label")
    light_unit_lookup = load_csv_dict(DATA_DIR + "IlluminatedPushPullLEDLightUnit.csv", value_col="Label")
    lens_lookup       = load_csv_dict(DATA_DIR + "LEDPushPullLens reference.csv")  # Nested: Code, Color, PartNumber
    circuit_lookup    = load_csv_dict(DATA_DIR + "Circuit.csv", value_col="Label")
    voltage_lookup    = load_csv_dict(DATA_DIR + "IlluminatedPushPullLLEDVoltage.csv", value_col="Label")
    return operator_lookup, light_unit_lookup, lens_lookup, circuit_lookup, voltage_lookup


def decode(catalog_number, operator_lookup, light_unit_lookup, lens_lookup, circuit_lookup, voltage_lookup):
    """
    Decodes a catalog number like:
    10250T + Operator + LightUnit + Lens + Voltage + Circuit
    Handles two patterns:
      - If code starts with '1': Operator(2) + LightUnit(3) + Lens(2) + Voltage(2) + Circuit(rest)
      - Else: Operator(1) + LightUnit(3) + Lens(2) + Voltage(2) + Circuit(rest)
    """
    if not catalog_number:
        return None

    normalized = str(catalog_number).replace("-", "").strip().upper()

    # Basic format guard
    if not (normalized.startswith("10250T") and len(normalized) > 12):
        return None

    code_part = normalized[6:]

    # Parse based on first digit
    if code_part.startswith("1"):
        operator_code   = code_part[:2]
        light_unit_code = code_part[2:5]
        lens_code       = code_part[5:7]
        voltage_code    = code_part[7:9]
        circuit_code    = code_part[9:]
    else:
        operator_code   = code_part[:1]
        light_unit_code = code_part[1:4]
        lens_code       = code_part[4:6]
        voltage_code    = code_part[6:8]
        circuit_code    = code_part[8:]

    # lens_lookup expected to be nested: {Code: {"Color": ..., "PartNumber": ...}}
    lens_info = lens_lookup.get(lens_code, {}) or {}

    return {
        "Operator":          operator_lookup.get(operator_code, "Unknown Operator"),
        "Light Unit":        light_unit_lookup.get(light_unit_code, "Unknown Light Unit"),
        "Lens":              lens_info.get("Color", "Unknown Lens"),
        "Voltage":           voltage_lookup.get(voltage_code, "Unknown Voltage"),
        "Circuit":           circuit_lookup.get(circuit_code, "Unknown Circuit"),
        "Operator P/N":      f"10250T{operator_code}",
        "Light Unit P/N":    f"10250T{light_unit_code}",
        "Lens P/N":          lens_info.get("PartNumber", "Unknown Lens P/N"),
        "Contact Block P/N": f"10250T{circuit_code}",
    }
