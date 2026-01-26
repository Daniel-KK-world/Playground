# file: dispenser.py

import random
from typing import Optional

TEMPERATURES = ("hot", "cold", "warm")


def dispense_water(requested: Optional[str] = None) -> str:
    if requested is None:
        return random.choice(TEMPERATURES)

    requested = requested.lower()
    if requested not in TEMPERATURES:
        raise ValueError(f"Invalid temperature: {requested}")

    return requested


if __name__ == "__main__":
    try:
        choice = input("Choose hot, cold, warm, or press Enter for random: ").strip()
        water = dispense_water(choice or None)
        print(f"Dispensing {water} water.")
    except ValueError as error:
        print(error)
