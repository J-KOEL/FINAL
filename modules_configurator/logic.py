def build_catalog_number(product_type, selections):
    if product_type == "Non-Illuminated Pushbuttons":
        return f"10250T{selections['Operator']}{selections['Button Color']}-{selections['Circuit']}"
    elif product_type == "Non-Illuminated Pushpulls":
        return f"10250T{selections['Operator']}{selections['Button']}-{selections['Circuit']}"
    elif product_type == "Illuminated Incandescent Pushpulls":
        return f"10250T{selections['Operator']}{selections['Light Unit']}{selections['Lens']}-{selections['Circuit']}"
    elif product_type == "Illuminated LED Pushpulls":
        return f"10250T{selections['Operator']}{selections['Light Unit']}{selections['Lens']}{selections['Voltage']}-{selections['Circuit']}"
    elif product_type == "Illuminated Incandescent Pushbuttons":
        return f"10250T{selections['Light Unit']}{selections['Lens']}-{selections['Circuit']}"
    elif product_type == "Illuminated LED Pushbuttons":
        return f"10250T{selections['Light Unit']}{selections['Lens']}{selections['Voltage']}-{selections['Circuit']}"
    elif product_type == "Standard Indicating Lights - LED":
        return f"10250T{selections['Light Unit']}{selections['Lens']}{selections['Voltage']}"
    elif product_type == "Standard Indicating Lights - Incandescent":
        return f"10250T{selections['Light Unit']}{selections['Lens']}"
    elif product_type == "PresTest Incandescent":
        return f"10250T{selections['Light Unit']}{selections['Lens']}"
    elif product_type == "PresTest LED":
        return f"10250T{selections['Light Unit']}{selections['Lens']}{selections['Voltage']}"
    elif product_type == "Master Test Incandescent":
        return f"10250T{selections['Light Unit']}{selections['Lens']}"
    else:
        return "Invalid product type"
