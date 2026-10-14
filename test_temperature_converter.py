"""
Tests for Temperature Converter
Internship Task: Level 1, Day 14

Uses plain assert statements and Python standard library (math.isclose)
without any external test frameworks.
"""

import math
from temperature_converter import (
    ABSOLUTE_ZERO_CELSIUS,
    ABSOLUTE_ZERO_FAHRENHEIT,
    ABSOLUTE_ZERO_KELVIN,
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    celsius_to_kelvin,
    kelvin_to_celsius,
    fahrenheit_to_kelvin,
    kelvin_to_fahrenheit,
    validate_temperature,
)


def test_known_values():
    """
    Tests exact known conversion checkpoints across all temperature scales:
      - 0 C = 32 F
      - 100 C = 212 F
      - -40 C = -40 F (scale crossover point)
      - 0 C = 273.15 K
      - 0 K = -273.15 C (absolute zero in Celsius)
      - 32 F = 273.15 K (freezing point of water in Kelvin)
    """
    print("Running test_known_values...")

    # Celsius to Fahrenheit & reverse
    assert math.isclose(celsius_to_fahrenheit(0.0), 32.0, abs_tol=1e-5), "0 C should be 32 F"
    assert math.isclose(celsius_to_fahrenheit(100.0), 212.0, abs_tol=1e-5), "100 C should be 212 F"
    assert math.isclose(celsius_to_fahrenheit(-40.0), -40.0, abs_tol=1e-5), "-40 C should be -40 F"
    assert math.isclose(fahrenheit_to_celsius(32.0), 0.0, abs_tol=1e-5), "32 F should be 0 C"
    assert math.isclose(fahrenheit_to_celsius(212.0), 100.0, abs_tol=1e-5), "212 F should be 100 C"
    assert math.isclose(fahrenheit_to_celsius(-40.0), -40.0, abs_tol=1e-5), "-40 F should be -40 C"

    # Celsius to Kelvin & reverse
    assert math.isclose(celsius_to_kelvin(0.0), 273.15, abs_tol=1e-5), "0 C should be 273.15 K"
    assert math.isclose(kelvin_to_celsius(0.0), -273.15, abs_tol=1e-5), "0 K should be -273.15 C"
    assert math.isclose(kelvin_to_celsius(273.15), 0.0, abs_tol=1e-5), "273.15 K should be 0 C"
    assert math.isclose(celsius_to_kelvin(-273.15), 0.0, abs_tol=1e-5), "-273.15 C should be 0 K"

    # Fahrenheit to Kelvin & reverse
    assert math.isclose(fahrenheit_to_kelvin(32.0), 273.15, abs_tol=1e-5), "32 F should be 273.15 K"
    assert math.isclose(kelvin_to_fahrenheit(273.15), 32.0, abs_tol=1e-5), "273.15 K should be 32 F"
    assert math.isclose(fahrenheit_to_kelvin(212.0), 373.15, abs_tol=1e-5), "212 F should be 373.15 K"
    assert math.isclose(kelvin_to_fahrenheit(373.15), 212.0, abs_tol=1e-5), "373.15 K should be 212 F"

    print("  [PASS] test_known_values passed successfully.")


def test_round_trip_conversions():
    """
    Tests round-trip conversions (converting to a target unit and converting back
    must restore the original value within floating-point tolerance).
    """
    print("Running test_round_trip_conversions...")

    test_celsius_temps = [-200.0, -40.0, 0.0, 18.5, 37.0, 100.0, 500.0]
    for c in test_celsius_temps:
        # C -> F -> C
        f = celsius_to_fahrenheit(c)
        c_back = fahrenheit_to_celsius(f)
        assert math.isclose(c, c_back, abs_tol=1e-5), f"C->F->C round-trip failed for {c}"

        # C -> K -> C
        k = celsius_to_kelvin(c)
        c_back_k = kelvin_to_celsius(k)
        assert math.isclose(c, c_back_k, abs_tol=1e-5), f"C->K->C round-trip failed for {c}"

    test_fahrenheit_temps = [-400.0, -40.0, 0.0, 32.0, 72.0, 98.6, 212.0]
    for f in test_fahrenheit_temps:
        # F -> C -> F
        c = fahrenheit_to_celsius(f)
        f_back = celsius_to_fahrenheit(c)
        assert math.isclose(f, f_back, abs_tol=1e-5), f"F->C->F round-trip failed for {f}"

        # F -> K -> F
        k = fahrenheit_to_kelvin(f)
        f_back_k = kelvin_to_fahrenheit(k)
        assert math.isclose(f, f_back_k, abs_tol=1e-5), f"F->K->F round-trip failed for {f}"

    test_kelvin_temps = [0.0, 50.0, 273.15, 300.0, 373.15, 1000.0]
    for k in test_kelvin_temps:
        # K -> C -> K
        c = kelvin_to_celsius(k)
        k_back_c = celsius_to_kelvin(c)
        assert math.isclose(k, k_back_c, abs_tol=1e-5), f"K->C->K round-trip failed for {k}"

        # K -> F -> K
        f = kelvin_to_fahrenheit(k)
        k_back_f = fahrenheit_to_kelvin(f)
        assert math.isclose(k, k_back_f, abs_tol=1e-5), f"K->F->K round-trip failed for {k}"

    print("  [PASS] test_round_trip_conversions passed successfully.")


def test_absolute_zero_rejection():
    """
    Tests that temperatures strictly below absolute zero are rejected (return False),
    and temperatures at or above absolute zero are accepted (return True).
    """
    print("Running test_absolute_zero_rejection...")

    # Rejected values (strictly below absolute zero)
    assert validate_temperature(-273.16, "C") is False, "Should reject Celsius below -273.15"
    assert validate_temperature(-300.0, "C") is False, "Should reject -300 C"
    assert validate_temperature(-459.68, "F") is False, "Should reject Fahrenheit below -459.67"
    assert validate_temperature(-500.0, "F") is False, "Should reject -500 F"
    assert validate_temperature(-0.01, "K") is False, "Should reject negative Kelvin"
    assert validate_temperature(-10.0, "K") is False, "Should reject negative Kelvin"

    # Accepted values (boundary: exact absolute zero)
    assert validate_temperature(ABSOLUTE_ZERO_CELSIUS, "C") is True, "Exact absolute zero in C must be valid"
    assert validate_temperature(ABSOLUTE_ZERO_FAHRENHEIT, "F") is True, "Exact absolute zero in F must be valid"
    assert validate_temperature(ABSOLUTE_ZERO_KELVIN, "K") is True, "Exact absolute zero in K must be valid"

    # Accepted values (typical positive / standard temperatures)
    assert validate_temperature(0.0, "C") is True, "0 C must be valid"
    assert validate_temperature(100.0, "C") is True, "100 C must be valid"
    assert validate_temperature(32.0, "F") is True, "32 F must be valid"
    assert validate_temperature(273.15, "K") is True, "273.15 K must be valid"

    # Invalid unit rejection
    assert validate_temperature(100.0, "X") is False, "Invalid unit should be rejected"

    print("  [PASS] test_absolute_zero_rejection passed successfully.")


def run_all_tests():
    """Runs all test suites and prints a summary."""
    print("=" * 50)
    print("Running Temperature Converter Test Suite...")
    print("=" * 50)
    test_known_values()
    test_round_trip_conversions()
    test_absolute_zero_rejection()
    print("=" * 50)
    print("ALL TESTS PASSED SUCCESSFULLY! (100% assertions verified)")
    print("=" * 50)


if __name__ == "__main__":
    run_all_tests()
