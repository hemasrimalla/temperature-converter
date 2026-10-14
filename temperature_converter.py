"""
Temperature Converter
Internship Task: Level 1, Day 14

A beginner-friendly console application to convert temperatures between
Celsius, Fahrenheit, and Kelvin. Demonstrates functions, arithmetic
operations, physical limits validation, and robust input handling.
"""

import math

# ============================================================================
# Physical Constants: Absolute Zero Limits
# ============================================================================
# Absolute zero is the lowest theoretically possible temperature, where particles
# have minimal vibrational motion. No temperature can exist below these limits.
ABSOLUTE_ZERO_CELSIUS = -273.15
ABSOLUTE_ZERO_FAHRENHEIT = -459.67
ABSOLUTE_ZERO_KELVIN = 0.0


# ============================================================================
# Validation Function
# ============================================================================
def validate_temperature(value: float, unit: str) -> bool:
    """
    Validates whether a given temperature is at or above absolute zero.

    Parameters:
        value (float): The numeric temperature reading to validate.
        unit (str): The temperature unit ('C', 'F', or 'K').

    Returns:
        bool: True if the temperature is physically possible, False otherwise.
    """
    unit_upper = unit.upper()

    if unit_upper == "C":
        if value < ABSOLUTE_ZERO_CELSIUS:
            print(
                f"\n[Invalid Input] {value:.2f} C is below absolute zero "
                f"({ABSOLUTE_ZERO_CELSIUS:.2f} C). Physical temperatures cannot be lower than absolute zero."
            )
            return False
    elif unit_upper == "F":
        if value < ABSOLUTE_ZERO_FAHRENHEIT:
            print(
                f"\n[Invalid Input] {value:.2f} F is below absolute zero "
                f"({ABSOLUTE_ZERO_FAHRENHEIT:.2f} F). Physical temperatures cannot be lower than absolute zero."
            )
            return False
    elif unit_upper == "K":
        if value < ABSOLUTE_ZERO_KELVIN:
            print(
                f"\n[Invalid Input] {value:.2f} K is below absolute zero "
                f"({ABSOLUTE_ZERO_KELVIN:.2f} K). Kelvin cannot be negative."
            )
            return False
    else:
        print(f"\n[Invalid Input] Unknown unit '{unit}'. Please use 'C', 'F', or 'K'.")
        return False

    return True


# ============================================================================
# Conversion Functions
# ============================================================================
def celsius_to_fahrenheit(c: float) -> float:
    """
    Convert a temperature from Celsius to Fahrenheit.

    Formula: F = (C * 9/5) + 32

    Parameters:
        c (float): Temperature in degrees Celsius.

    Returns:
        float: Temperature in degrees Fahrenheit.
    """
    return (c * 9.0 / 5.0) + 32.0


def fahrenheit_to_celsius(f: float) -> float:
    """
    Convert a temperature from Fahrenheit to Celsius.

    Formula: C = (F - 32) * 5/9

    Parameters:
        f (float): Temperature in degrees Fahrenheit.

    Returns:
        float: Temperature in degrees Celsius.
    """
    return (f - 32.0) * 5.0 / 9.0


def celsius_to_kelvin(c: float) -> float:
    """
    Convert a temperature from Celsius to Kelvin.

    Formula: K = C + 273.15

    Parameters:
        c (float): Temperature in degrees Celsius.

    Returns:
        float: Temperature in Kelvin.
    """
    return c + 273.15


def kelvin_to_celsius(k: float) -> float:
    """
    Convert a temperature from Kelvin to Celsius.

    Formula: C = K - 273.15

    Parameters:
        k (float): Temperature in Kelvin.

    Returns:
        float: Temperature in degrees Celsius.
    """
    return k - 273.15


def fahrenheit_to_kelvin(f: float) -> float:
    """
    Convert a temperature from Fahrenheit to Kelvin.

    Formula: K = (F - 32) * 5/9 + 273.15

    Parameters:
        f (float): Temperature in degrees Fahrenheit.

    Returns:
        float: Temperature in Kelvin.
    """
    celsius = fahrenheit_to_celsius(f)
    return celsius_to_kelvin(celsius)


def kelvin_to_fahrenheit(k: float) -> float:
    """
    Convert a temperature from Kelvin to Fahrenheit.

    Formula: F = (K - 273.15) * 9/5 + 32

    Parameters:
        k (float): Temperature in Kelvin.

    Returns:
        float: Temperature in degrees Fahrenheit.
    """
    celsius = kelvin_to_celsius(k)
    return celsius_to_fahrenheit(celsius)


# ============================================================================
# Helper Input Function
# ============================================================================
def get_temperature_input(prompt_text: str, unit: str) -> float:
    """
    Prompts the user for a temperature value, handling non-numeric input
    using a try-except block and ensuring the value is at or above absolute zero.
    Repeats the prompt until a valid value is entered.

    Parameters:
        prompt_text (str): The prompt message shown to the user.
        unit (str): The unit of measurement ('C', 'F', or 'K').

    Returns:
        float: A validated numeric temperature value.
    """
    while True:
        raw_input = input(prompt_text).strip()
        try:
            value = float(raw_input)
        except ValueError:
            print("\n[Invalid Input] Please enter a valid number (e.g., 25, 98.6, -10.5).")
            continue

        # Check physical limit (absolute zero)
        if validate_temperature(value, unit):
            return value


# ============================================================================
# Main Menu & Interactive Program Loop
# ============================================================================
def display_menu() -> None:
    """Prints the main interactive menu options."""
    print("\n" + "=" * 45)
    print("         TEMPERATURE CONVERTER")
    print("=" * 45)
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")
    print("=" * 45)


def main() -> None:
    """
    Main program loop providing a menu-driven interface for conversions.
    """
    print("Welcome to the Temperature Converter program!")
    print("Convert temperatures accurately between Celsius, Fahrenheit, and Kelvin.")

    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            c = get_temperature_input("Enter temperature in Celsius (C): ", "C")
            f = celsius_to_fahrenheit(c)
            print(f"\n=> Result: {c:.2f} C = {f:.2f} F")

        elif choice == "2":
            f = get_temperature_input("Enter temperature in Fahrenheit (F): ", "F")
            c = fahrenheit_to_celsius(f)
            print(f"\n=> Result: {f:.2f} F = {c:.2f} C")

        elif choice == "3":
            c = get_temperature_input("Enter temperature in Celsius (C): ", "C")
            k = celsius_to_kelvin(c)
            print(f"\n=> Result: {c:.2f} C = {k:.2f} K")

        elif choice == "4":
            k = get_temperature_input("Enter temperature in Kelvin (K): ", "K")
            c = kelvin_to_celsius(k)
            print(f"\n=> Result: {k:.2f} K = {c:.2f} C")

        elif choice == "5":
            f = get_temperature_input("Enter temperature in Fahrenheit (F): ", "F")
            k = fahrenheit_to_kelvin(f)
            print(f"\n=> Result: {f:.2f} F = {k:.2f} K")

        elif choice == "6":
            k = get_temperature_input("Enter temperature in Kelvin (K): ", "K")
            f = kelvin_to_fahrenheit(k)
            print(f"\n=> Result: {k:.2f} K = {f:.2f} F")

        elif choice == "7":
            print("\nThank you for using Temperature Converter. Goodbye!")
            break

        else:
            print("\n[Invalid Option] Please enter a number from 1 to 7.")


# ============================================================================
# Entry Point Guard
# ============================================================================
if __name__ == "__main__":
    main()
