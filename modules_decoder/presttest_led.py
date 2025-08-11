# modules_decoder/presttest_led.py
from shared.utils import load_csv_dict

DATA_DIR = "assets/data/"  # Base directory for CSV files

def load_data():
    """
    Loads lookup dictionaries for PresTest LED:
    10250T + LightUnit(4) + Lens(2) + Voltage(rest)
    """
    light_unit_lookup = load_csv_dict(DATA_DIR + "PrestTestLEDLightunit.csv")
    lens_lookup       = load_csv_dict(DATA_DIR + "PrestTestLEDLens.csv")
    voltage_lookup    = load_csv_dict(DATA_DIR + "IndicatinglightLEDvoltage.csv")
    return light_unit_lookup, lens_lookup, voltage_lookup


def decode(catalog_number, light_unit_lookup, lens_lookup, voltage_lookup):
    """
    Decodes a catalog number like: 10250TLLLLCCVV...
    Where:
      - LLLL = Light Unit code (4)
      - CC   = Lens code (2)
      - VV.. = Voltage code (remaining)
    Returns a dict of human-friendly fields or None if it cannot decode.
    """
    if not catalog_number:
        return None

    normalized = str(catalog_number).replace("-", "").strip().upper()

    # Basic format guard
    if not (normalized.startswith("10250T") and len(normalized) > 11):
        return None

    code_part = normalized[6:]
    if len(code_part) < 7:  # need at least 4 + 2 + 1
        return None

    light_unit_code = code_part[:4]
    lens_code       = code_part[4:6]
    voltage_code    = code_part[6:]

    return {
        "Light Unit":     light_unit_lookup.get(light_unit_code, "Unknown Light Unit"),
        "Lens Color":     lens_lookup.get(lens_code, "Unknown Lens Color"),
        "Voltage":        voltage_lookup.get(voltage_code, "Unknown Voltage"),
        "Light Unit P/N": f"10250T{light_unit_code}",
        "Lens P/N":       f"10250T{lens_code}",
        "Voltage P/N":    f"10250T{voltage_code}",
    }
