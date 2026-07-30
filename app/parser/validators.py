from app.parser.constants import *


import re

def is_medicine_line(text: str):

    text = text.strip().upper()

    # Existing prefix detection
    if any(text.startswith(prefix) for prefix in MEDICINE_PREFIXES):
        return True

    # Reject obvious non-medicine lines
    if any(item == text for item in IGNORE_LINES):
        return False

    # Ignore advice/instruction lines
    if text.startswith("ADVICE"):
        return False

    if text.startswith("FOLLOW"):
        return False

    if text.startswith("DIAGNOSIS"):
        return False

    # Detect medicine names without prefixes
    if re.match(r"^[A-Z][A-Z0-9/+(). -]{2,}$", text):

        # Exclude common OCR noise
        blacklist = [
            "PATIENT",
            "PRESCRIPTION",
            "CLINICAL",
            "FINDINGS",
            "DATE",
            "WEIGHT",
            "HEIGHT",
            "HEADACHE",
            "FEVER",
            "MALARIA",
            "SUNDAY",
            "TIMING",
        ]

        if not any(word in text for word in blacklist):
            return True

    return False

def clean_name(text: str):

    for prefix in MEDICINE_PREFIXES:

        if text.upper().startswith(prefix):

            return text[len(prefix):].strip()

    return text.strip()


def is_food_instruction(text: str):

    text = text.upper()

    return any(
        item in text
        for item in FOOD_INSTRUCTIONS
    )


def is_ignored_line(text: str):

    text = text.upper()

    return any(
        item == text
        for item in IGNORE_LINES
    )
