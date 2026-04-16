# 1. if, elif, else statements
temperature = 25

if temperature > 30:
    print("It's a hot day!")
elif temperature > 20:
    print("It's a nice day.")
else:
    print("It's cold.")

print("-" * 20)

# 2. for loop
# Looping through a list
fruits = ["apple", "banana", "cherry"]
print("Fruits in the list:")
for fruit in fruits:
    print(fruit)

print("-" * 20)

# Looping with range()
print("Counting from 0 to 4:")
for i in range(5):
    print(i)

print("-" * 20)

# 3. while loop
# The loop continues as long as the condition is True
count = 0
print("While loop counting to 3:")
while count < 3:
    print(f"Count is {count}")
    count += 1

print("-" * 20)

# 4. break and continue
print("Using break and continue in a loop:")
for num in range(10):
    if num == 3:
        print("Skipping number 3.")
        continue  # Skip the rest of this iteration
    if num == 7:
        print("Breaking the loop at number 7.")
        break  # Exit the loop completely
    print(f"Current number is {num}") 