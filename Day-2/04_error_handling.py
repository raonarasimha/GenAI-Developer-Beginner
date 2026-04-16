if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        result = 10 / num
    except ValueError:
        print("You must enter a valid integer!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    else:
        print(f"10 divided by {num} is {result}")
    finally:
        print("This block always runs (cleanup, logging, etc.)")

    # Example: FileNotFoundError
    try:
        with open("nonexistent_file.txt", "r") as f:
            content = f.read()
    except FileNotFoundError:
        print("File not found error caught!")

    # Example: IndexError
    try:
        my_list = [1, 2, 3]
        print(my_list[5])
    except IndexError:
        print("Index out of range error caught!")

    # Example: KeyError
    try:
        my_dict = {"a": 1, "b": 2}
        print(my_dict["c"])
    except KeyError:
        print("Key not found error caught!")