product_configs = {
    "Non-Illuminated Pushbuttons": {
        "fields": ["Operator", "Button Color", "Circuit"],
        "files": {
            "Operator": "NonIlluminatedPushbuttonOperator.csv",
            "Button Color": "NonIlluminatedPushbuttonButtonColor.csv",
            "Circuit": "Circuit.csv",
        },
    },
    "Non-Illuminated Pushpulls": {
        "fields": ["Operator", "Button", "Circuit"],
        "files": {
            "Operator": "PushPullOperator.csv",
            "Button": "NonIlluminatedPushPullButton.csv",
            "Circuit": "Circuit.csv",
        },
    },
    "Illuminated Incandescent Pushpulls": {
        "fields": ["Operator", "Light Unit", "Lens", "Circuit"],
        "files": {
            "Operator": "PushPullOperator.csv",
            "Light Unit": "IlluminatedPushPullIncandescentLightUnit.csv",
            "Lens": "IlluminatedPushPullIncandescentLens.csv",
            "Circuit": "Circuit.csv",
        },
    },
    "Illuminated LED Pushpulls": {
        "fields": ["Operator", "Light Unit", "Lens", "Voltage", "Circuit"],
        "files": {
            "Operator": "PushPullOperator.csv",
            "Light Unit": "IlluminatedPushPullLEDLightUnit.csv",
            "Lens": "IlluminatedPushPullLEDlens.csv",
            "Voltage": "IlluminatedPushPullLLEDVoltage.csv",
            "Circuit": "Circuit.csv",
        },
    },
    "Illuminated Incandescent Pushbuttons": {
        "fields": ["Light Unit", "Lens", "Circuit"],
        "files": {
            "Light Unit": "IlluminatedPushbuttonIncandescentLightUnit.csv",
            "Lens": "illuminatedPushbuttonIncandescentLensColor.csv",
            "Circuit": "Circuit.csv",
        },
    },
    "Illuminated LED Pushbuttons": {
        "fields": ["Light Unit", "Lens", "Voltage", "Circuit"],
        "files": {
            "Light Unit": "IlluminatedPushbuttonLEDLightUnit.csv",
            "Lens": "IlluminatedPushbuttonLEDLensColor.csv",
            "Voltage": "IlluminatedPushbuttonLEDVoltage.csv",
            "Circuit": "Circuit.csv",
        },
    },
    "Standard Indicating Lights - LED": {
        "fields": ["Light Unit", "Lens", "Voltage"],
        "files": {
            "Light Unit": "StandardindicatingLightLEDlightUnit.csv",
            "Lens": "StandardIndicatingLightLEDLens.csv",
            "Voltage": "IndicatinglightLEDvoltage.csv",
        },
    },
    "Standard Indicating Lights - Incandescent": {
        "fields": ["Light Unit", "Lens"],
        "files": {
            "Light Unit": "StandardIndicatingLightIncandescentLightUnit.csv",
            "Lens": "StandardIndicatingIncandescentLens.csv",
        },
    },
    "PresTest Incandescent": {
        "fields": ["Light Unit", "Lens"],
        "files": {
            "Light Unit": "PrestTestIncandescentLightUnit.csv",
            "Lens": "PrestTestIncandescentLens.csv",
        },
    },
    "PresTest LED": {
        "fields": ["Light Unit", "Lens", "Voltage"],
        "files": {
            "Light Unit": "PrestTestLEDLightunit.csv",
            "Lens": "PrestTestLEDLens.csv",
            "Voltage": "IndicatinglightLEDvoltage.csv",
        },
    },
    "Master Test Incandescent": {
        "fields": ["Light Unit", "Lens"],
        "files": {
            "Light Unit": "MasterTestIncandescentLightUnit.csv",
            "Lens": "MasterTestIncandescentLens.csv",
        },
    },
}

