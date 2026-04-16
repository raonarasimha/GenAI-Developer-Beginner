# 🕒 Hour 1: Python Basics + Workspace Setup

🏁 **Goal**: Understand core Python syntax and set up a working Python project.

---

### ✅ 1. Workspace Setup (15 mins)

*   **Topics**:
    *   Create a virtual environment with `venv`
    *   Activate it and install packages with `pip`
    *   Set up basic project structure
*   **Summary**: Learn how to isolate your Python project using `venv` and install libraries with `pip`.
*   **Prompt**: "Always use a virtual environment to avoid polluting global Python packages."
*   **Example**: [See `01_workspace_setup.md`](./01_workspace_setup.md)
![Workspace Setup Pyramid](./assets/Workspace%20Setup.svg)

---

### ✅ 2. Python Syntax & Variables (10 mins)

*   **Topics**:
    *   `print()`
    *   Variable assignment
    *   Single-line and inline comments
*   **Summary**: Understand Python’s clean syntax, print statements, and how to assign variables.
*   **Prompt**: "Python uses indentation, not braces. Keep it clean and readable."
*   **Example**: [Run `python 02_python_syntax_variables.py`](./02_python_syntax_variables.py)
![Python Syntax & Variables](./assets/Python%20Syntax%20Topics.svg)

---

### ✅ 3. Data Types (10 mins)

*   **Topics**:
    *   `int`, `float`, `str`, `bool`
    *   `list`, `tuple`, `dict`, `set`
    *   Using `type()`
*   **Summary**: Explore Python’s built-in types: strings, numbers, booleans, lists, dicts, sets, and tuples.

| Category         | Type        | Description                          | Example                  | Mutable | Ordered |
|------------------|------------|--------------------------------------|--------------------------|---------|---------|
| Numeric Types    | int        | Integer numbers                      | 42, -5, 0                | ❌      | ❌      |
|                  | float      | Decimal numbers                      | 3.14, -0.01              | ❌      | ❌      |
|                  | complex    | Complex numbers                      | 2 + 3j                   | ❌      | ❌      |
| Boolean Type     | bool       | True or False                        | True, False              | ❌      | ❌      |
| Text Type        | str        | String of characters                 | "hello"                  | ❌      | ✅      |
| Sequence Types   | list       | Ordered, mutable sequence            | [1, 2, 3]                | ✅      | ✅      |
|                  | tuple      | Ordered, immutable sequence          | (1, 2, 3)                | ❌      | ✅      |
|                  | range      | Immutable numeric sequence           | range(5)                 | ❌      | ✅      |
| Set Types        | set        | Unordered collection of unique values| {1, 2, 3}                | ✅      | ❌      |
|                  | frozenset  | Immutable version of set             | frozenset([1, 2, 3])     | ❌      | ❌      |
| Mapping Type     | dict       | Key-value pairs                      | {"a": 1, "b": 2}         | ✅      | ❌      |
| Binary Types     | bytes      | Immutable bytes                      | b"hello"                 | ❌      | ✅      |
|                  | bytearray  | Mutable bytes                        | bytearray([65, 66])      | ✅      | ✅      |
|                  | memoryview | View over binary data                | memoryview(b"abc")       | ✅      | ✅      |
| None Type        | NoneType   | Represents absence of a value        | None                     | ❌      | ❌      |
| User-Defined Types | Custom class | Types created by defining a class | class Person: ...        | Depends | Depends |

*   **Prompt**: "Everything in Python is an object with a type. Learn to recognize and use them."
*   **Example**: [Run `python 03_data_types.py`](./03_data_types.py)
![Python Data Types](./assets/Data%20Types.svg)

---

### ✅ 4. Operators & Expressions (5 mins)

*   **Topics**:
    *   Arithmetic: `+`, `-`, `*`, `/`, `%`, `**`
    *   Comparison: `==`, `!=`, `>`, `<`
    *   Logical: `and`, `or`, `not`
    *   Membership: `in`, `not in`
*   **Summary**: Use arithmetic and comparison operators to build logic and evaluate conditions.
*   **Prompt**: "Operators help you calculate values and compare results in your programs."
*   **Example**: [Run `python 04_operators_expressions.py`](./04_operators_expressions.py)
![Operators & Expressions](./assets/Operators%20&%20Expressions.svg)

---

### ✅ 5. Control Flow (10 mins)

*   **Topics**:
    *   `if`, `elif`, `else`
    *   `for` and `while` loops
    *   `range()`, `break`, `continue`
*   **Summary**: Use `if`, `for`, and `while` to control how code executes based on conditions.
*   **Prompt**: "Use control flow to make decisions or repeat actions in your code."
*   **Example**: [Run `python 05_control_flow.py`](./05_control_flow.py)
![Control Flow](./assets/Control%20Flow%20in%20Python.svg)

---

### ✅ 6. Functions (10 mins)

*   **Topics**:
    *   `def` syntax
    *   Parameters and `return` values
    *   Default arguments
    *   `*args`, `**kwargs` (awareness only)
*   **Summary**: Write reusable blocks of code with functions using `def`, `return` values, and parameters.
*   **Prompt**: "Functions make your code reusable, readable, and testable."
*   **Example**: [Run `python 06_functions.py`](./06_functions.py)
![Functions](./assets/Foundations%20of%20Python%20Functions.svg)