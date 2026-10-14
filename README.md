# Temperature Converter (Level 1, Day 14 Internship Task)

A clean, beginner-friendly Python console application designed to convert temperatures between **Celsius**, **Fahrenheit**, and **Kelvin**. This project demonstrates essential Python programming concepts, including functions with explicit return statements, arithmetic operations, constant definitions, robust input validation (`try-except`), and basic unit testing using standard Python `assert` statements.

---

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [How to Run](#how-to-run)
  - [Prerequisites](#prerequisites)
  - [Running the Program](#running-the-program)
  - [Running the Tests](#running-the-tests)
- [Conversion Formulas](#conversion-formulas)
- [Sample Outputs](#sample-outputs)
  - [Example 1: Celsius to Fahrenheit](#example-1-celsius-to-fahrenheit-option-1)
  - [Example 2: Fahrenheit to Celsius](#example-2-fahrenheit-to-celsius-option-2)
  - [Example 3: Celsius to Kelvin](#example-3-celsius-to-kelvin-option-3)
  - [Example 4: Fahrenheit to Kelvin](#example-4-fahrenheit-to-kelvin-option-5)
  - [Example 5: Input Validation & Absolute Zero Protection](#example-5-input-validation--absolute-zero-protection)
- [Interview Questions & Answers](#interview-questions--answers)
  - [1. Why use functions for repeated calculations?](#1-why-use-functions-for-repeated-calculations)
  - [2. What is a return statement?](#2-what-is-a-return-statement)
  - [3. What happens when a function does not explicitly return a value?](#3-what-happens-when-a-function-does-not-explicitly-return-a-value)

---

## Features
- **Standard Library Only:** Zero external dependencies or third-party packages required.
- **Six Distinct Conversion Functions:** Dedicated mathematical functions for every pair of temperature units.
- **Physical Limit Validation:** Constants define absolute zero ($-273.15^\circ\text{C}$, $-459.67^\circ\text{F}$, $0.00\text{ K}$). Prevents mathematically valid but physically impossible temperatures.
- **Robust Exception Handling:** Utilizes `try-except` blocks to guard against non-numeric characters (e.g. typing words or letters), ensuring the application never crashes.
- **Continuous Prompt Loop:** Keeps prompting until the user enters valid, physically plausible data.
- **Clean Formatting:** All conversion results are formatted cleanly to two decimal places (e.g., `100.00 C = 212.00 F`).
- **Comprehensive Unit Tests:** Tests known values, round-trip symmetry, and absolute zero boundary rejections using plain `assert` statements.

---

## Project Structure

```text
temperature-converter/
├── temperature_converter.py        # Main console application and conversion logic
├── test_temperature_converter.py   # Test suite using plain assert statements
└── README.md                       # Documentation, formulas, samples, and Q&A
```

---

## How to Run

### Prerequisites
- Python 3.8 or higher installed on your system.

### Running the Program
Open your terminal or command prompt, navigate to the project directory, and execute:

```bash
python temperature_converter.py
```

### Running the Tests
To run the automated tests:

```bash
python test_temperature_converter.py
```

If all tests pass, you will see a confirmation message:
```text
==================================================
Running Temperature Converter Test Suite...
==================================================
Running test_known_values...
  [PASS] test_known_values passed successfully.
Running test_round_trip_conversions...
  [PASS] test_round_trip_conversions passed successfully.
Running test_absolute_zero_rejection...
  [PASS] test_absolute_zero_rejection passed successfully.
==================================================
ALL TESTS PASSED SUCCESSFULLY! (100% assertions verified)
==================================================
```

---

## Conversion Formulas

The program implements 6 core conversion formulas:

1. **Celsius to Fahrenheit:**
   $$F = \left(C \times \frac{9}{5}\right) + 32$$
   *(Python: `(c * 9.0 / 5.0) + 32.0`)*

2. **Fahrenheit to Celsius:**
   $$C = (F - 32) \times \frac{5}{9}$$
   *(Python: `(f - 32.0) * 5.0 / 9.0`)*

3. **Celsius to Kelvin:**
   $$K = C + 273.15$$
   *(Python: `c + 273.15`)*

4. **Kelvin to Celsius:**
   $$C = K - 273.15$$
   *(Python: `k - 273.15`)*

5. **Fahrenheit to Kelvin:**
   $$K = (F - 32) \times \frac{5}{9} + 273.15$$
   *(Python: `fahrenheit_to_celsius(f) + 273.15`)*

6. **Kelvin to Fahrenheit:**
   $$F = (K - 273.15) \times \frac{9}{5} + 32$$
   *(Python: `(k - 273.15) * 9.0 / 5.0 + 32.0`)*

### Absolute Zero Limits:
- **Celsius:** $-273.15^\circ\text{C}$
- **Fahrenheit:** $-459.67^\circ\text{F}$
- **Kelvin:** $0.00\text{ K}$

---

## Sample Outputs

### Example 1: Celsius to Fahrenheit (Option 1)
```text
=============================================
         TEMPERATURE CONVERTER
=============================================
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Celsius to Kelvin
4. Kelvin to Celsius
5. Fahrenheit to Kelvin
6. Kelvin to Fahrenheit
7. Exit
=============================================
Enter your choice (1-7): 1
Enter temperature in Celsius (C): 100

=> Result: 100.00 C = 212.00 F
```

### Example 2: Fahrenheit to Celsius (Option 2)
```text
Enter your choice (1-7): 2
Enter temperature in Fahrenheit (F): 32

=> Result: 32.00 F = 0.00 C
```

### Example 3: Celsius to Kelvin (Option 3)
```text
Enter your choice (1-7): 3
Enter temperature in Celsius (C): 0

=> Result: 0.00 C = 273.15 K
```

### Example 4: Fahrenheit to Kelvin (Option 5)
```text
Enter your choice (1-7): 5
Enter temperature in Fahrenheit (F): -40

=> Result: -40.00 F = 233.15 K
```

### Example 5: Input Validation & Absolute Zero Protection
Demonstrates graceful handling of non-numeric input, values below absolute zero, and invalid menu choices:
```text
Enter your choice (1-7): 1
Enter temperature in Celsius (C): warm

[Invalid Input] Please enter a valid number (e.g., 25, 98.6, -10.5).
Enter temperature in Celsius (C): -300

[Invalid Input] -300.00 C is below absolute zero (-273.15 C). Physical temperatures cannot be lower than absolute zero.
Enter temperature in Celsius (C): 25

=> Result: 25.00 C = 77.00 F

=============================================
         TEMPERATURE CONVERTER
=============================================
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Celsius to Kelvin
4. Kelvin to Celsius
5. Fahrenheit to Kelvin
6. Kelvin to Fahrenheit
7. Exit
=============================================
Enter your choice (1-7): 9

[Invalid Option] Please enter a number from 1 to 7.

Enter your choice (1-7): 7

Thank you for using Temperature Converter. Goodbye!
```

---

## Interview Questions & Answers

### 1. Why use functions for repeated calculations?
Using functions for repeated calculations is a fundamental best practice (following the **DRY - Don't Repeat Yourself** principle) for several key reasons:
- **Code Reusability:** Once written and tested, a function can be invoked anywhere in the project without rewriting the formula.
- **Readability & Maintainability:** Functions give meaningful names to operations (e.g., `celsius_to_fahrenheit`), making the code self-documenting. If a formula needs adjustment, you only update it in one central location.
- **Easier Testing & Debugging:** Isolating logic into self-contained units enables targeted unit testing (as seen in `test_temperature_converter.py`). Bugs are isolated and easy to diagnose.
- **Avoiding Code Duplication:** Copy-pasting formulas introduces subtle human typos and creates maintenance debt.

### 2. What is a return statement?
A `return` statement is a language construct inside a function that:
1. **Terminates the function's execution:** When Python reaches a `return` statement, it immediately exits the function block.
2. **Passes data back to the caller:** It hands the computed value (or object) back to the line of code that invoked the function, allowing the caller to store it in a variable, pass it to another function, or print it.

```python
def square(number: float) -> float:
    return number * number  # Returns the computed square back to the caller

result = square(5)  # 'result' receives 25
```

### 3. What happens when a function does not explicitly return a value?
In Python, if a function reaches the end of its code block without encountering an explicit `return` statement (or executes a bare `return` with no expression), it **implicitly returns `None`**.

`None` is Python's built-in singleton object used to represent the absence of a value.

#### Code Demonstration:
```python
def greet(name: str):
    print(f"Hello, {name}!")
    # Notice: No return statement here

output = greet("Alice")
print(output)         # Prints: None
print(type(output))   # Prints: <class 'NoneType'>
```

If you try to perform arithmetic on the result of a function that does not return a value, Python will raise a `TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'`, which is why explicit return statements are essential for calculation functions.
