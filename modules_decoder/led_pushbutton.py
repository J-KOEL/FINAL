# modules_decoder/led_pushbutton.py
from shared.utils import load_csv_dict

DATA_DIR = "assets/data/"  # Base directory for CSV files

def load_data():
    """
    Loads lookup dictionaries for LED Pushbutton:
    10250T + LightUnit(4) + LensColor(2) + Voltage(2) + '-' + Circuit(...)
    """
    # Note: load_csv_dict automatically maps Code -> Label when those columns exist.
    light_unit_lookup = load_csv_dict(DATA_DIR + "IlluminatedPushbuttonLEDLightUnit.csv", value_col="Label")
    lens_color_lookup = load_csv_dict(DATA_DIR + "IlluminatedPushbuttonLEDlensColorProductNumber.csv")
    voltage_lookup    = load_csv_dict(DATA_DIR + "IlluminatedPushbuttonLEDVoltage.csv", value_col="Label")
    circuit_lookup    = load_csv_dict(DATA_DIR + "Circuit.csv", value_col="Label")
    return light_unit_lookup, lens_color_lookup, voltage_lookup, circuit_lookup


def decode(catalog_number, light_unit_lookup, lens_color_lookup, voltage_lookup, circuit_lookup):
    """
    Decodes a catalog number like: 10250TLLLLCCVV-XXXX...
    Where:
      - LLLL = Light Unit code (4)
      - CC   = Lens Color code (2)
      - VV   = LED Voltage code (2)
      - XXXX... = Circuit code (remaining after optional dash)
    Returns a dict of human-friendly fields or None if it cannot decode.
    """
    if not catalog_number:
        return None

    normalized = str(catalog_number).replace("-", "").strip().upper()

    # Basic format guard
    if not (normalized.startswith("10250T") and len(normalized) > 10):
        return None

    code_part = normalized[6:]
    if len(code_part) < 8:  # need at least 4 + 2 + 2
        return None

    light_unit_code  = code_part[:4]
    lens_color_code  = code_part[4:6]
    voltage_code     = code_part[6:8]
    circuit_code     = code_part[8:]  # whatever remains

    # lens_color_lookup expected to be nested: {Code: {"Color": ..., "PartNumber": ...}}
    lens_info = lens_color_lookup.get(lens_color_code, {}) or {}

    return {
        "Light Unit":        light_unit_lookup.get(light_unit_code, "Unknown Light Unit"),
        "Lens Color":        lens_info.get("Color", "Unknown Lens Color"),
        "LED Voltage":       voltage_lookup.get(voltage_code, "Unknown LED Voltage"),
        "Circuit Type":      circuit_lookup.get(circuit_code, "Unknown Circuit Type"),
        "Light Unit P/N":    f"10250T{light_unit_code}",
        "Lens P/N":          lens_info.get("PartNumber", "Unknown Lens P/N"),
        "Contact Block P/N": f"10250T{circuit_code}",
    }
