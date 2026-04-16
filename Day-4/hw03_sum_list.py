if __name__ == "__main__":
    numbers = input("Enter numbers separated by spaces: ")
    num_list = [int(n) for n in numbers.split()]
    total = sum(num_list)
    print("Sum of numbers:", total)