from app.parser.constants import *


import re

def is_medicine_line(text: str):

    text = text.upper()

    return any(
        text.startswith(prefix)
        for prefix in MEDICINE_PREFIXES
    )

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
