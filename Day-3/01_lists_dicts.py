if __name__ == "__main__":
    # Lists
    fruits = ["apple", "banana", "cherry"]
    fruits.append("orange")
    print("Fruits list:", fruits)
    for fruit in fruits:
        if fruit.startswith("a"):
            print(f"Fruit starting with 'a': {fruit}")

    # Dicts
    student = {"name": "Alice", "age": 22, "courses": ["Math", "Science"]}
    print("Student dict:", student)
    for key in student.keys():
        print(f"Key: {key}, Value: {student[key]}") 