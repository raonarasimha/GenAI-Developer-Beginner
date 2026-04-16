# 1. Basic function definition and calling
def greet():
    """This is a docstring. It explains what the function does."""
    print("Hello from a function!")

greet()  # Calling the function

print("-" * 20)

# 2. Function with parameters
def greet_person(name):
    """Greets a person by their name."""
    print(f"Hello, {name}!")

greet_person("Alice")
greet_person("Bob")

print("-" * 20)

# 3. Function with a return value
def add_numbers(a, b):
    """Adds two numbers and returns the result."""
    return a + b

sum_result = add_numbers(5, 3)
print(f"The sum is: {sum_result}")
print(f"Directly printing the result: {add_numbers(10, 15)}")

print("-" * 20)

# 4. Function with default arguments
def say_hello(name="Guest"):
    """Greets a person, or a guest if no name is provided."""
    print(f"Hello, {name}!")

say_hello("Charlie")  # Uses the provided argument
say_hello()           # Uses the default argument

print("-" * 20)

# 5. Awareness of *args and **kwargs (for future reference)
# *args allows a function to accept a variable number of positional arguments.
def print_args(*args):
    print("Arguments passed with *args:")
    for arg in args:
        print(arg)

print_args(1, "apple", True)

# **kwargs allows a function to accept a variable number of keyword arguments.
def print_kwargs(**kwargs):
    print("\nArguments passed with **kwargs:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="David", age=30, city="New York") 