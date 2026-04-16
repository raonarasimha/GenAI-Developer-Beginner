if __name__ == "__main__":
    numbers = input("Enter numbers separated by spaces: ")
    num_list = [int(n) for n in numbers.split()]
    if num_list:
        print("Largest number:", max(num_list))
    else:
        print("No numbers provided.")