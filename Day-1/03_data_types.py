# Python has several built-in data types.

# Numbers: int (integer) and float (floating-point)
integer_number = 10
float_number = 10.5
print(f"Integer: {integer_number}, Type: {type(integer_number)}")
print(f"Float: {float_number}, Type: {type(float_number)}")

# String: a sequence of characters
text = "This is a string"
print(f"String: '{text}', Type: {type(text)}")

# Boolean: represents True or False
is_active = True
print(f"Boolean: {is_active}, Type: {type(is_active)}")

# List: an ordered, mutable collection of items
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Lists are mutable
print(f"List: {fruits}, Type: {type(fruits)}")

# Tuple: an ordered, immutable collection of items
coordinates = (10.0, 20.0)
# coordinates[0] = 5.0  # This would raise a TypeError because tuples are immutable
print(f"Tuple: {coordinates}, Type: {type(coordinates)}")

# Dictionary: an unordered collection of key-value pairs
student = {"name": "Alice", "age": 25, "courses": ["Math", "Science"]}
print(f"Dictionary: {student}, Type: {type(student)}")
print(f"Student's name: {student['name']}")

# Set: an unordered collection of unique items
unique_numbers = {1, 2, 3, 2, 1}
print(f"Set: {unique_numbers}, Type: {type(unique_numbers)}") 